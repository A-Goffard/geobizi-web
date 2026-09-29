from fastapi import APIRouter, HTTPException, BackgroundTasks
import uuid
from datetime import datetime

from core.database import get_db_connection
from schemas import SolicitudReserva, ListaEsperaCreate
from services.email_service import (
    enviar_correo_reserva,
    enviar_correo_cancelacion,
    enviar_correo_modificacion,
    enviar_correo_lista_espera
)
from services.reserva_service import (
    reasignar_plazas_liberadas,
    limpiar_ofertas_expiradas
)

router = APIRouter(tags=["Reservas"])

# ==============================================================================
# 1. CREAR RESERVA CONFIRMADA
# ==============================================================================
@router.post("/reservas")
def crear_reserva(datos: SolicitudReserva, background_tasks: BackgroundTasks):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        limpiar_ofertas_expiradas(cursor, background_tasks)

        # Evitar duplicados activos en la misma actividad
        cursor.execute("""
            SELECT id FROM reservas 
            WHERE actividad_id = ? AND (phone = ? OR email = ?) AND estado = 'confirmada'
        """, (datos.actividad_id, datos.phone, datos.email))
        
        if cursor.fetchone():
            raise HTTPException(
                status_code=400,
                detail="Ya existe una reserva confirmada registrada con este teléfono o correo electrónico."
            )

        cursor.execute("""
            SELECT titulo, descripcion, fecha, hora, ubicacion, plazas_totales, plazas_ocupadas 
            FROM actividades WHERE id = ?
        """, (datos.actividad_id,))
        actividad = cursor.fetchone()
        
        if not actividad:
            raise HTTPException(status_code=404, detail="La actividad no existe.")
        
        # Transacción atómica anti-sobreventa
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
        
        for p in datos.participantes:
            cursor.execute("""
                INSERT INTO participantes (reserva_id, nombre, apellidos, edad)
                VALUES (?, ?, ?, ?)
            """, (reserva_id, p.nombre, p.apellidos, p.edad))
            
        conn.commit()
        
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
# 2. APUNTAR A LA LISTA DE ESPERA
# ==============================================================================
@router.post("/lista-espera")
def apuntar_lista_espera(datos: ListaEsperaCreate, background_tasks: BackgroundTasks):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        limpiar_ofertas_expiradas(cursor, background_tasks)

        cursor.execute("""
            SELECT titulo, fecha, hora, ubicacion, plazas_totales, plazas_ocupadas 
            FROM actividades WHERE id = ?
        """, (datos.actividad_id,))
        actividad = cursor.fetchone()
        
        if not actividad:
            raise HTTPException(status_code=404, detail="La actividad no existe.")
            
        cursor.execute("""
            SELECT id FROM reservas 
            WHERE actividad_id = ? AND (email = ? OR phone = ?) AND estado IN ('lista_espera', 'pendiente_confirmacion')
        """, (datos.actividad_id, datos.email, datos.phone))
        
        if cursor.fetchone():
            raise HTTPException(
                status_code=400, 
                detail="Ya estás en la lista de espera de esta actividad con este correo o teléfono."
            )

        token_seguro = str(uuid.uuid4())

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

        for p in datos.participantes:
            cursor.execute("""
                INSERT INTO participantes (reserva_id, nombre, apellidos, edad)
                VALUES (?, ?, ?, ?)
            """, (reserva_id, p.nombre, p.apellidos, p.edad))

        conn.commit()

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
# 3. CONSULTAR DATOS POR TOKEN
# ==============================================================================
@router.get("/token/{token}")
def obtener_reserva_por_token(token: str, background_tasks: BackgroundTasks):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Limpieza de expiradas con commit garantizado
        limpiar_ofertas_expiradas(cursor, background_tasks)
        conn.commit()
        
        cursor.execute("""
            SELECT id, actividad_id, nombre_contacto, apellidos_contacto, email, phone, 
                   num_personas, permiso_fotos, observaciones, estado, expiracion_oferta 
            FROM reservas 
            WHERE token = ?
        """, (token,))
        reserva = cursor.fetchone()
        
        if not reserva:
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
        
        return {
            "reserva": dict(reserva),
            "participantes": [dict(p) for p in participantes],
            "actividad": dict(actividad) if actividad else {}
        }
    finally:
        conn.close()


# ==============================================================================
# 4. ACEPTAR OFERTA TEMPORAL DE PLAZA (DESDE CORREO)
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
            raise HTTPException(status_code=400, detail="Esta reserva no tiene ninguna oferta pendiente de confirmación.")

        if not reserva["expiracion_oferta"]:
            raise HTTPException(status_code=400, detail="No se encontró fecha de caducidad para esta oferta.")

        # Verificar plazo límite
        ahora = datetime.now()
        expira = datetime.fromisoformat(reserva["expiracion_oferta"])
        if ahora > expira:
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
# 5. CANCELAR RESERVA O SALIR DE LISTA DE ESPERA
# ==============================================================================
@router.delete("/token/{token}")
def cancelar_reserva_por_token(token: str, background_tasks: BackgroundTasks):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
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

        # 1. Eliminar datos vinculados
        cursor.execute("DELETE FROM participantes WHERE reserva_id = ?", (reserva_id,))
        cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))

        # 2. Si estaba ocupando plaza (confirmada o pendiente), la reasignamos a la cola de espera
        if estado_reserva in ("confirmada", "pendiente_confirmacion"):
            reasignar_plazas_liberadas(actividad_id, plazas_a_liberar, cursor, background_tasks)

        conn.commit()

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
        raise HTTPException(status_code=500, detail=f"Error al cancelar: {str(e)}")
    finally:
        conn.close()


# ==============================================================================
# 6. MODIFICAR RESERVA (CON REASIGNACIÓN SI SE REDUCEN PLAZAS)
# ==============================================================================
@router.put("/token/{token}")
def actualizar_reserva_por_token(token: str, datos: dict, background_tasks: BackgroundTasks):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            SELECT r.id, r.actividad_id, r.num_personas, r.estado,
                   r.nombre_contacto, r.apellidos_contacto, r.email, r.phone, r.observaciones,
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

        # Detectar el nuevo número de plazas a partir de la lista de asistentes
        participantes_nuevos = datos.get("participantes", [])
        if participantes_nuevos:
            plazas_nuevas = len(participantes_nuevos)
        elif "num_personas" in datos and datos["num_personas"] is not None:
            plazas_nuevas = int(datos["num_personas"])
        else:
            plazas_nuevas = plazas_antiguas

        diferencia = plazas_nuevas - plazas_antiguas
        print(f"\n[ACTUALIZAR RESERVA] Antiguas: {plazas_antiguas} | Nuevas: {plazas_nuevas} | Diferencia: {diferencia}")

        actividad_datos = {
            "titulo": fila["titulo"],
            "fecha": fila["fecha"],
            "hora": fila["hora"],
            "ubicacion": fila["ubicacion"]
        }

        # Gestión de aforo si la reserva estaba ocupando plazas
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
                plazas_liberadas = abs(diferencia)
                print(f"[ACTUALIZAR RESERVA] Se redujeron {plazas_liberadas} plaza(s). Iniciando reasignación a la lista de espera...")
                reasignar_plazas_liberadas(actividad_id, plazas_liberadas, cursor, background_tasks)

        # Campos de contacto protegidos contra sobreescrituras nulas
        nombre_contacto = datos.get("nombre_contacto") or fila["nombre_contacto"]
        apellidos_contacto = datos.get("apellidos_contacto") or fila["apellidos_contacto"]
        email_contacto = datos.get("email") or fila["email"]
        phone_contacto = datos.get("phone") or fila["phone"]
        observaciones_contacto = datos.get("observaciones") if "observaciones" in datos else fila["observaciones"]

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
            nombre_contacto,
            apellidos_contacto,
            email_contacto,
            phone_contacto,
            plazas_nuevas,
            observaciones_contacto,
            reserva_id
        ))

        # Actualizar fichas de asistentes
        cursor.execute("DELETE FROM participantes WHERE reserva_id = ?", (reserva_id,))
        for p in participantes_nuevos:
            cursor.execute("""
                INSERT INTO participantes (reserva_id, nombre, apellidos, edad)
                VALUES (?, ?, ?, ?)
            """, (reserva_id, p.get("nombre"), p.get("apellidos"), int(p.get("edad", 0))))

        conn.commit()

        background_tasks.add_task(
            enviar_correo_modificacion,
            email_destino=email_contacto,
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