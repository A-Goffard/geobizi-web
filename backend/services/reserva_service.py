from datetime import datetime, timedelta
from fastapi import BackgroundTasks
from services.email_service import (
    enviar_correo_oferta_plaza,
    enviar_correo_turno_expirado
)

def calcular_tiempo_limite(fecha_actividad_str: str, hora_actividad_str: str = "10:00") -> tuple[datetime, str]:
    """
    Calcula el plazo de respuesta según la proximidad de la actividad:
    - Más de 48h antes: 24 horas de margen.
    - Entre 12h y 48h antes: 6 horas de margen.
    - Menos de 12h (mismo día): 2 horas de margen.
    """
    ahora = datetime.now()
    horas_plazo = 24

    try:
        # Intentar parsear fecha y hora combinadas
        hora_limpia = (hora_actividad_str or "10:00").strip()[:5]
        str_completo = f"{fecha_actividad_str.strip()} {hora_limpia}"
        fecha_act = datetime.strptime(str_completo, "%Y-%m-%d %H:%M")
        horas_hasta_actividad = (fecha_act - ahora).total_seconds() / 3600
        
        if horas_hasta_actividad > 48:
            horas_plazo = 24
        elif horas_hasta_actividad > 12:
            horas_plazo = 6
        else:
            horas_plazo = 2
    except Exception as e:
        # Si el formato de hora fuera complejo (ej: '10:00 a 13:00'), parseamos solo fecha
        try:
            fecha_act = datetime.strptime(fecha_actividad_str.strip(), "%Y-%m-%d")
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


def reasignar_plazas_liberadas(actividad_id: int, plazas_liberadas: int, cursor, background_tasks: BackgroundTasks):
    """
    Revisa la cola en lista_espera (FIFO).
    Tiene en cuenta tanto las plazas recién liberadas como los huecos
    libres que ya existían previamente en la actividad.
    """
    cursor.execute("SELECT plazas_totales, plazas_ocupadas FROM actividades WHERE id = ?", (actividad_id,))
    act = cursor.fetchone()
    if not act:
        return

    plazas_totales = int(act["plazas_totales"])
    # Las plazas ocupadas actuales en BD aún contienen las que se acaban de liberar
    ocupadas_base = max(0, int(act["plazas_ocupadas"]) - int(plazas_liberadas))
    
    # Plazas totales reales disponibles para repartir entre la lista de espera
    plazas_disponibles_reales = max(0, plazas_totales - ocupadas_base)

    print(f"\n[COLA DE ESPERA] Actividad ID {actividad_id}: Aforo={plazas_totales} | Ocupadas_reales={ocupadas_base} | Libres_totales={plazas_disponibles_reales}")

    if plazas_disponibles_reales <= 0:
        cursor.execute("UPDATE actividades SET plazas_ocupadas = ? WHERE id = ?", (ocupadas_base, actividad_id))
        return

    # Consulta rigurosa FIFO por ID
    cursor.execute("""
        SELECT r.id, r.nombre_contacto, r.email, r.num_personas, r.token, 
               a.titulo, a.fecha, a.hora, a.ubicacion
        FROM reservas r
        JOIN actividades a ON r.actividad_id = a.id
        WHERE r.actividad_id = ? AND r.estado = 'lista_espera'
        ORDER BY r.id ASC
    """, (actividad_id,))
    cola_espera = cursor.fetchall()

    print(f"[COLA DE ESPERA] Encontradas {len(cola_espera)} reserva(s) en lista de espera.")

    plazas_restantes = plazas_disponibles_reales
    plazas_asignadas_a_espera = 0

    for solicitante in cola_espera:
        if plazas_restantes <= 0:
            break

        cupo = int(solicitante["num_personas"])
        print(f"[COLA DE ESPERA] Evaluando turno de: '{solicitante['nombre_contacto']}' ({solicitante['email']}) -> Solicita {cupo} plaza(s). Libres en este paso: {plazas_restantes}")

        if cupo <= plazas_restantes:
            limite_dt, limite_texto = calcular_tiempo_limite(
                solicitante["fecha"], 
                solicitante["hora"]
            )

            # 1. Poner en estado temporal
            cursor.execute("""
                UPDATE reservas 
                SET estado = 'pendiente_confirmacion',
                    expiracion_oferta = ?
                WHERE id = ?
            """, (limite_dt.isoformat(), solicitante["id"]))

            plazas_restantes -= cupo
            plazas_asignadas_a_espera += cupo

            actividad_datos = {
                "titulo": solicitante["titulo"],
                "fecha": solicitante["fecha"],
                "hora": solicitante["hora"],
                "ubicacion": solicitante["ubicacion"]
            }

            print(f"[COLA DE ESPERA] -> ¡Turno asignado! Enviando oferta por email a {solicitante['email']} válida hasta {limite_texto}")

            # 2. Despachar oferta con tiempo límite
            background_tasks.add_task(
                enviar_correo_oferta_plaza,
                email_destino=solicitante["email"],
                actividad=actividad_datos,
                token=solicitante["token"],
                num_personas=cupo,
                fecha_limite_texto=limite_texto,
                nombre_contacto=solicitante["nombre_contacto"]
            )
        else:
            print(f"[COLA DE ESPERA] -> Se omite por ahora a '{solicitante['nombre_contacto']}' porque necesita {cupo} plazas y solo hay {plazas_restantes} libre(s).")

    # 3. Actualizar aforo definitivo:
    # Plazas ocupadas = las que ya estaban ocupadas + las retenidas temporalmente para la lista de espera
    nuevas_ocupadas = ocupadas_base + plazas_asignadas_a_espera
    cursor.execute("""
        UPDATE actividades 
        SET plazas_ocupadas = ? 
        WHERE id = ?
    """, (nuevas_ocupadas, actividad_id))

    print(f"[COLA DE ESPERA] Fin de asignación. Ocupación en BD: {nuevas_ocupadas}/{plazas_totales} (Retenidas para espera: {plazas_asignadas_a_espera} | Libres públicas: {plazas_totales - nuevas_ocupadas})")


def limpiar_ofertas_expiradas(cursor, background_tasks: BackgroundTasks):
    """
    Detecta ofertas en 'pendiente_confirmacion' cuyo plazo venció.
    Las elimina, avisa al usuario por correo y cede inmediatamente su turno al siguiente grupo.
    """
    ahora_iso = datetime.now().isoformat()
    cursor.execute("""
        SELECT r.id, r.actividad_id, r.email, r.nombre_contacto, r.num_personas, a.titulo AS actividad_titulo
        FROM reservas r
        JOIN actividades a ON r.actividad_id = a.id
        WHERE r.estado = 'pendiente_confirmacion' AND r.expiracion_oferta < ?
    """, (ahora_iso,))
    expiradas = cursor.fetchall()

    for exp in expiradas:
        reserva_id = exp["id"]
        actividad_id = exp["actividad_id"]
        plazas = int(exp["num_personas"])
        email_expirado = exp["email"]
        nombre_expirado = exp["nombre_contacto"]
        titulo_actividad = exp["actividad_titulo"]

        print(f"[OFERTA EXPIRADA] La oferta para {nombre_expirado} ({email_expirado}) ha caducado. Liberando {plazas} plaza(s).")

        # 1. Eliminar oferta caducada
        cursor.execute("DELETE FROM participantes WHERE reserva_id = ?", (reserva_id,))
        cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))

        # 2. Notificar al usuario que su plazo venció
        background_tasks.add_task(
            enviar_correo_turno_expirado,
            email_destino=email_expirado,
            actividad_titulo=titulo_actividad,
            nombre_contacto=nombre_expirado
        )

        # 3. Reasignar inmediatamente esas plazas liberadas al siguiente turno
        reasignar_plazas_liberadas(actividad_id, plazas, cursor, background_tasks)