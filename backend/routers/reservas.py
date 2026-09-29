from fastapi import APIRouter, HTTPException, BackgroundTasks
import uuid
from database import get_db_connection
from schemas import SolicitudReserva, ListaEsperaCreate
from utils.email_service import (
    enviar_correo_reserva,
    enviar_correo_cancelacion,
    enviar_correo_modificacion,
    enviar_correo_oferta_plaza
)
from datetime import datetime, timedelta

# Importación segura por si aún no has añadido la plantilla al servicio de email
try:
    from utils.email_service import enviar_correo_lista_espera
except ImportError:
    enviar_correo_lista_espera = None

router = APIRouter(tags=["Reservas"])

# ==============================================================================
# 1. CREAR RESERVA CONFIRMADA (CON ASIGNACIÓN DE PLAZAS)
# ==============================================================================
@router.post("/reservas")
def crear_reserva(datos: SolicitudReserva, background_tasks: BackgroundTasks):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # 1. Evitar duplicados confirmados con el mismo email o teléfono
        cursor.execute("""
            SELECT id FROM reservas 
            WHERE actividad_id = ? AND (phone = ? OR email = ?) AND estado = 'confirmada'
        """, (datos.actividad_id, datos.phone, datos.email))
        
        if cursor.fetchone():
            raise HTTPException(
                status_code=400,
                detail="Ya existe una reserva confirmada registrada con este teléfono o correo electrónico."
            )

        # 2. Comprobar que la actividad existe
        cursor.execute("""
            SELECT titulo, descripcion, fecha, hora, ubicacion, plazas_totales, plazas_ocupadas 
            FROM actividades WHERE id = ?
        """, (datos.actividad_id,))
        actividad = cursor.fetchone()
        
        if not actividad:
            raise HTTPException(status_code=404, detail="La actividad no existe.")
        
        # 3. Transacción atómica anti-sobreventa (reserva de plazas)
        cursor.execute("""
            UPDATE actividades 
            SET plazas_ocupadas = plazas_ocupadas + ? 
            WHERE id = ? 
              AND (plazas_totales - plazas_ocupadas) >= ?
        """, (datos.num_personas, datos.actividad_id, datos.num_personas))
        
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=400, 
                detail="Lo sentimos, no quedan suficientes plazas libres para esta actividad."
            )
            
        token_seguro = str(uuid.uuid4())
        
        # 4. Insertar la reserva con estado 'confirmada'
        cursor.execute("""
            INSERT INTO reservas (
                actividad_id, nombre_contacto, apellidos_contacto, 
                email, phone, num_personas, token, permiso_fotos, observaciones, estado
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'confirmada')
        """, (
            datos.actividad_id, datos.nombre_contacto, datos.apellidos_contacto, 
            datos.email, datos.phone, datos.num_personas, token_seguro,
            datos.permiso_fotos, datos.observaciones
        ))
        
        reserva_id = cursor.lastrowid
        
        # 5. Insertar todos los asistentes vinculados
        for p in datos.participantes:
            cursor.execute("""
                INSERT INTO participantes (reserva_id, nombre, apellidos, edad)
                VALUES (?, ?, ?, ?)
            """, (reserva_id, p.nombre, p.apellidos, p.edad))
            
        conn.commit()
        
        # 6. Despachar email de confirmación
        background_tasks.add_task(
            enviar_correo_reserva,
            email_destino=datos.email,
            actividad=dict(actividad),
            token=token_seguro,
            num_personas=datos.num_personas
        )
        
        return {
            "status": "success",
            "message": "Reserva realizada correctamente",
            "reserva_id": reserva_id,
            "token": token_seguro
        }
        
    except HTTPException as he:
        conn.rollback()
        raise he
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
    finally:
        conn.close()

# ==============================================================================
# 2. APUNTAR A LA LISTA DE ESPERA (CON TODOS LOS ASISTENTES Y TOKEN PROPIO)
# ==============================================================================
@router.post("/lista-espera")
def apuntar_lista_espera(datos: ListaEsperaCreate, background_tasks: BackgroundTasks):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # 1. Comprobar que la actividad existe
        cursor.execute("""
            SELECT titulo, fecha, hora, ubicacion, plazas_totales, plazas_ocupadas 
            FROM actividades WHERE id = ?
        """, (datos.actividad_id,))
        actividad = cursor.fetchone()
        
        if not actividad:
            raise HTTPException(status_code=404, detail="La actividad no existe.")
            
        # 2. Comprobar si ya está en lista de espera
        cursor.execute("""
            SELECT id FROM reservas 
            WHERE actividad_id = ? AND (email = ? OR phone = ?) AND estado = 'lista_espera'
        """, (datos.actividad_id, datos.email, datos.phone))
        
        if cursor.fetchone():
            raise HTTPException(
                status_code=400, 
                detail="Ya estás en la lista de espera de esta actividad con este correo o teléfono."
            )

        token_seguro = str(uuid.uuid4())

        # 3. Insertar la reserva como 'lista_espera' (NO suma plazas ocupadas)
        cursor.execute("""
            INSERT INTO reservas (
                actividad_id, nombre_contacto, apellidos_contacto, 
                email, phone, num_personas, token, permiso_fotos, observaciones, estado
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'lista_espera')
        """, (
            datos.actividad_id, 
            datos.nombre_contacto or datos.nombre, 
            datos.apellidos_contacto or datos.apellidos, 
            datos.email, 
            datos.phone, 
            datos.num_personas, 
            token_seguro,
            datos.permiso_fotos, 
            datos.observaciones
        ))
        
        reserva_id = cursor.lastrowid

        # 4. Insertar la lista de asistentes en participantes vinculados a este reserva_id
        for p in datos.participantes:
            cursor.execute("""
                INSERT INTO participantes (reserva_id, nombre, apellidos, edad)
                VALUES (?, ?, ?, ?)
            """, (reserva_id, p.nombre, p.apellidos, p.edad))

        conn.commit()

        # 5. Enviar correo de notificación de espera si la función está definida
        if enviar_correo_lista_espera:
            background_tasks.add_task(
                enviar_correo_lista_espera,
                email_destino=datos.email,
                actividad=dict(actividad),
                token=token_seguro,
                num_personas=datos.num_personas
            )

        return {
            "status": "success", 
            "message": "Te has registrado correctamente en la lista de espera con tus acompañantes. Si se liberan plazas suficientes para tu grupo, te avisaremos.",
            "token": token_seguro
        }

    except HTTPException as he:
        conn.rollback()
        raise he
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error en el servidor: {str(e)}")
    finally:
        conn.close()

# ==============================================================================
# 3. OBTENER DATOS DE UNA RESERVA MEDIANTE TOKEN
# ==============================================================================
@router.get("/token/{token}")
def obtener_reserva_por_token(token: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, actividad_id, nombre_contacto, apellidos_contacto, email, phone, 
               num_personas, permiso_fotos, observaciones, estado 
        FROM reservas 
        WHERE token = ?
    """, (token,))
    reserva = cursor.fetchone()
    
    if not reserva:
        conn.close()
        raise HTTPException(status_code=404, detail="Reserva no encontrada o enlace no válido.")
        
    cursor.execute("""
        SELECT id, nombre, apellidos, edad 
        FROM participantes 
        WHERE reserva_id = ?
    """, (reserva["id"],))
    participantes = cursor.fetchall()
    
    cursor.execute("""
        SELECT id, titulo, fecha, hora, ubicacion, color, plazas_totales, plazas_ocupadas 
        FROM actividades 
        WHERE id = ?
    """, (reserva["actividad_id"],))
    actividad = cursor.fetchone()
    
    conn.close()
    
    return {
        "reserva": dict(reserva),
        "participantes": [dict(p) for p in participantes],
        "actividad": dict(actividad) if actividad else {}
    }

# ==============================================================================
# 4. CANCELAR RESERVA POR TOKEN (DISTINGUE CONFIRMADA VS LISTA DE ESPERA)
# ==============================================================================
@router.delete("/token/{token}")
def cancelar_reserva_por_token(token: str, background_tasks: BackgroundTasks):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # 1. Obtener la reserva antes de borrar
        cursor.execute("""
            SELECT r.id, r.actividad_id, r.nombre_contacto, r.email, r.num_personas, r.estado,
                   a.titulo, a.fecha, a.hora, a.ubicacion
            FROM reservas r
            JOIN actividades a ON r.actividad_id = a.id
            WHERE r.token = ?
        """, (token,))
        fila = cursor.fetchone()
        
        if not fila:
            raise HTTPException(status_code=404, detail="La reserva no existe o ya ha sido cancelada.")
            
        reserva_id = fila["id"]
        actividad_id = fila["actividad_id"]
        plazas_a_liberar = fila["num_personas"]
        estado_reserva = fila["estado"]
        email_contacto = fila["email"]
        nombre_contacto = fila["nombre_contacto"]
        actividad_datos = {
            "titulo": fila["titulo"],
            "fecha": fila["fecha"],
            "hora": fila["hora"],
            "ubicacion": fila["ubicacion"]
        }

        # 2. Devolver las plazas SOLO si era una reserva confirmada
        if estado_reserva == "confirmada":
            cursor.execute("""
                UPDATE actividades 
                SET plazas_ocupadas = MAX(0, plazas_ocupadas - ?) 
                WHERE id = ?
            """, (plazas_a_liberar, actividad_id))

        # 3. Eliminar participantes vinculados
        cursor.execute("DELETE FROM participantes WHERE reserva_id = ?", (reserva_id,))

        # 4. Eliminar el registro principal de la reserva
        cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))

        conn.commit()

        # 5. Despachar correo de cancelación
        background_tasks.add_task(
            enviar_correo_cancelacion,
            email_destino=email_contacto,
            actividad=actividad_datos,
            nombre_contacto=nombre_contacto
        )

        return {
            "status": "success",
            "message": "Cancelación procesada correctamente. Se ha enviado un correo de confirmación."
        }

    except HTTPException as he:
        conn.rollback()
        raise he
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error al cancelar la reserva: {str(e)}")
    finally:
        conn.close()

# ==============================================================================
# 5. MODIFICAR RESERVA POR TOKEN
# ==============================================================================
@router.put("/token/{token}")
def actualizar_reserva_por_token(token: str, datos: dict, background_tasks: BackgroundTasks):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            SELECT r.id, r.actividad_id, r.num_personas, r.estado,
                   a.titulo, a.fecha, a.hora, a.ubicacion
            FROM reservas r
            JOIN actividades a ON r.actividad_id = a.id
            WHERE r.token = ?
        """, (token,))
        fila = cursor.fetchone()
        
        if not fila:
            raise HTTPException(status_code=404, detail="Reserva no encontrada o enlace no válido.")
            
        reserva_id = fila["id"]
        actividad_id = fila["actividad_id"]
        estado_reserva = fila["estado"]
        plazas_antiguas = int(fila["num_personas"])
        plazas_nuevas = int(datos.get("num_personas", plazas_antiguas))
        diferencia = plazas_nuevas - plazas_antiguas

        actividad_datos = {
            "titulo": fila["titulo"],
            "fecha": fila["fecha"],
            "hora": fila["hora"],
            "ubicacion": fila["ubicacion"]
        }

        # Ajuste de plazas solo si ya estaba confirmada
        if estado_reserva == "confirmada":
            if diferencia > 0:
                cursor.execute("""
                    UPDATE actividades 
                    SET plazas_ocupadas = plazas_ocupadas + ? 
                    WHERE id = ? 
                      AND (plazas_totales - plazas_ocupadas) >= ?
                """, (diferencia, actividad_id, diferencia))
                
                if cursor.rowcount == 0:
                    raise HTTPException(
                        status_code=400, 
                        detail="No quedan suficientes plazas libres para ampliar la reserva."
                    )
            elif diferencia < 0:
                cursor.execute("""
                    UPDATE actividades 
                    SET plazas_ocupadas = MAX(0, plazas_ocupadas - ?) 
                    WHERE id = ?
                """, (abs(diferencia), actividad_id))

        # Actualizar datos de contacto y número de personas
        cursor.execute("""
            UPDATE reservas 
            SET nombre_contacto = ?, 
                apellidos_contacto = ?, 
                email = ?, 
                phone = ?, 
                num_personas = ?, 
                observaciones = ?
            WHERE id = ?
        """, (
            datos.get("nombre_contacto"),
            datos.get("apellidos_contacto"),
            datos.get("email"),
            datos.get("phone"),
            plazas_nuevas,
            datos.get("observaciones"),
            reserva_id
        ))

        # Actualizar lista de participantes
        participantes_nuevos = datos.get("participantes", [])
        cursor.execute("DELETE FROM participantes WHERE reserva_id = ?", (reserva_id,))
        for p in participantes_nuevos:
            cursor.execute("""
                INSERT INTO participantes (reserva_id, nombre, apellidos, edad)
                VALUES (?, ?, ?, ?)
            """, (reserva_id, p.get("nombre"), p.get("apellidos"), int(p.get("edad", 0))))

        conn.commit()

        # Enviar correo con los cambios guardados
        background_tasks.add_task(
            enviar_correo_modificacion,
            email_destino=datos.get("email"),
            actividad=actividad_datos,
            token=token,
            num_personas=plazas_nuevas,
            participantes=participantes_nuevos
        )

        return {"status": "success", "message": "Reserva modificada correctamente. Se ha enviado un correo con los cambios."}

    except HTTPException as he:
        conn.rollback()
        raise he
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error interno al actualizar: {str(e)}")
    finally:
        conn.close()

        # ==============================================================================
# 6. ACEPTAR RESRVA PENDIENTE DE CONFIRMACIÓN (CUANDO SE LIBERA UNA PLAZA)
# ==============================================================================     
@router.post("/token/{token}/aceptar-espera")
def aceptar_plaza_lista_espera(token: str, background_tasks: BackgroundTasks):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        limpiar_ofertas_expiradas(cursor, background_tasks)

        cursor.execute("""
            SELECT r.id, r.actividad_id, r.nombre_contacto, r.email, r.num_personas, r.estado, r.expiracion_oferta,
                   a.titulo, a.fecha, a.hora, a.ubicacion
            FROM reservas r
            JOIN actividades a ON r.actividad_id = a.id
            WHERE r.token = ?
        """, (token,))
        reserva = cursor.fetchone()

        if not reserva:
            raise HTTPException(status_code=404, detail="El enlace no es válido o ha expirado.")

        if reserva["estado"] == "confirmada":
            return {"status": "info", "message": "Tu reserva ya estaba confirmada previamente."}

        if reserva["estado"] != "pendiente_confirmacion":
            raise HTTPException(status_code=400, detail="Esta reserva no tiene ninguna oferta de plaza pendiente de confirmación.")

        # Comprobar que no haya expirado
        ahora = datetime.now()
        expira = datetime.fromisoformat(reserva["expiracion_oferta"])
        if ahora > expira:
            # Expiró: se borra y se pasa al siguiente
            reserva_id = reserva["id"]
            actividad_id = reserva["actividad_id"]
            plazas = reserva["num_personas"]
            cursor.execute("DELETE FROM participantes WHERE reserva_id = ?", (reserva_id,))
            cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
            reasignar_plazas_liberadas(actividad_id, plazas, cursor, background_tasks)
            conn.commit()
            raise HTTPException(status_code=400, detail="El plazo para confirmar tu plaza ha vencido y se ha ofrecido al siguiente turno.")

        # Confirmación definitiva
        cursor.execute("""
            UPDATE reservas 
            SET estado = 'confirmada', expiracion_oferta = NULL 
            WHERE id = ?
        """, (reserva["id"],))
        conn.commit()

        # Enviar correo de confirmación final
        background_tasks.add_task(
            enviar_correo_reserva,
            email_destino=reserva["email"],
            actividad={
                "titulo": reserva["titulo"],
                "fecha": reserva["fecha"],
                "hora": reserva["hora"],
                "ubicacion": reserva["ubicacion"]
            },
            token=token,
            num_personas=reserva["num_personas"]
        )

        return {"status": "success", "message": "¡Plaza confirmada con éxito! Te hemos enviado los detalles a tu correo."}

    finally:
        conn.close()
# ==============================================================================
# 7. TIEMPO LÍMITE PARA RESPONDER A UNA OFERTA DE PLAZA (48h, 6h o 2h según proximidad)
# ==============================================================================       
        
def calcular_tiempo_limite(fecha_actividad_str: str) -> tuple[datetime, str]:
    """
    Calcula un plazo razonable:
    - Si la actividad es en más de 48h -> 24h para responder.
    - Si la actividad es mañana -> 6h para responder.
    - Si es el mismo día -> 2h.
    """
    ahora = datetime.now()
    try:
        fecha_act = datetime.strptime(fecha_actividad_str, "%Y-%m-%d")
        horas_hasta_actividad = (fecha_act - ahora).total_seconds() / 3600
        
        if horas_hasta_actividad > 48:
            horas_plazo = 24
        elif horas_hasta_actividad > 12:
            horas_plazo = 6
        else:
            horas_plazo = 2
    except Exception:
        horas_plazo = 24

    limite = ahora + timedelta(hours=horas_plazo)
    limite_texto = limite.strftime("%d/%m/%Y a las %H:%M")
    return limite, limite_texto


def limpiar_ofertas_expiradas(cursor, background_tasks: BackgroundTasks):
    """
    Revisa si hay ofertas cuyo plazo venció. Las elimina y reasigna las plazas inmediatamente.
    """
    ahora_iso = datetime.now().isoformat()
    cursor.execute("""
        SELECT id, actividad_id, email, nombre_contacto, num_personas 
        FROM reservas 
        WHERE estado = 'pendiente_confirmacion' AND expiracion_oferta < ?
    """, (ahora_iso,))
    expiradas = cursor.fetchall()

    for exp in expiradas:
        reserva_id = exp["id"]
        actividad_id = exp["actividad_id"]
        plazas = exp["num_personas"]

        # Eliminar la reserva expirada
        cursor.execute("DELETE FROM participantes WHERE reserva_id = ?", (reserva_id,))
        cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))

        # Reasignar inmediatamente esas plazas al siguiente de la lista de espera
        reasignar_plazas_liberadas(actividad_id, plazas, cursor, background_tasks)
        
def reasignar_plazas_liberadas(actividad_id: int, plazas_liberadas: int, cursor, background_tasks: BackgroundTasks):
    if plazas_liberadas <= 0:
        return

    cursor.execute("""
        SELECT r.id, r.nombre_contacto, r.email, r.num_personas, r.token, a.titulo, a.fecha, a.hora, a.ubicacion
        FROM reservas r
        JOIN actividades a ON r.actividad_id = a.id
        WHERE r.actividad_id = ? AND r.estado = 'lista_espera'
        ORDER BY r.fecha_creacion ASC
    """, (actividad_id,))
    cola_espera = cursor.fetchall()

    plazas_restantes = plazas_liberadas

    for solicitante in cola_espera:
        if plazas_restantes <= 0:
            break

        cupo = solicitante["num_personas"]
        if cupo <= plazas_restantes:
            limite_dt, limite_texto = calcular_tiempo_limite(solicitante["fecha"])

            # 1. Poner en estado 'pendiente_confirmacion' con fecha límite
            cursor.execute("""
                UPDATE reservas 
                SET estado = 'pendiente_confirmacion',
                    expiracion_oferta = ?
                WHERE id = ?
            """, (limite_dt.isoformat(), solicitante["id"]))

            plazas_restantes -= cupo

            # 2. Las plazas siguen sumadas en la actividad (nadie externo puede cogerlas)
            # 3. Enviar correo de oferta con cuenta atrás
            actividad_datos = {
                "titulo": solicitante["titulo"],
                "fecha": solicitante["fecha"],
                "hora": solicitante["hora"],
                "ubicacion": solicitante["ubicacion"]
            }

            background_tasks.add_task(
                enviar_correo_oferta_plaza,
                email_destino=solicitante["email"],
                actividad=actividad_datos,
                token=solicitante["token"],
                num_personas=cupo,
                fecha_limite_texto=limite_texto,
                nombre_contacto=solicitante["nombre_contacto"]
            )

    # Si tras recorrer la lista nadie pudo usar las plazas, se liberan al aforo público
    if plazas_restantes > 0:
        cursor.execute("""
            UPDATE actividades 
            SET plazas_ocupadas = MAX(0, plazas_ocupadas - ?) 
            WHERE id = ?
        """, (plazas_restantes, actividad_id))