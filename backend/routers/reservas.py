from fastapi import APIRouter, HTTPException
import uuid
from database import get_db_connection
from schemas import SolicitudReserva

router = APIRouter(tags=["Reservas"])

@router.post("/reservas")
def crear_reserva(datos: SolicitudReserva):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Acotamos la selección para comprobar aforo
        cursor.execute("SELECT plazas_totales, plazas_ocupadas FROM actividades WHERE id = ?", (datos.actividad_id,))
        actividad = cursor.fetchone()
        
        if not actividad:
            raise HTTPException(status_code=404, detail="La actividad no existe.")
        
        # Transacción atómica anti-sobreventa segura
        cursor.execute("""
            UPDATE actividades 
            SET plazas_ocupadas = plazas_ocupadas + ? 
            WHERE id = ? 
              AND (plazas_totales - plazas_ocupadas) >= ?
        """, (datos.num_personas, datos.actividad_id, datos.num_personas))
        
        conn.commit()
        
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=400, 
                detail="Lo sentimos, no quedan suficientes plazas libres para esta actividad."
            )
            
        token_seguro = str(uuid.uuid4())
        
        cursor.execute("""
            INSERT INTO reservas (actividad_id, nombre_contacto, apellidos_contacto, email, phone, num_personas, token, permiso_fotos, observaciones)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
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


@router.get("/token/{token}")
def obtener_reserva_por_token(token: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Acotamos los campos de la reserva
    cursor.execute("""
        SELECT id, actividad_id, nombre_contacto, apellidos_contacto, email, phone, num_personas, permiso_fotos, observaciones 
        FROM reservas 
        WHERE token = ?
    """, (token,))
    reserva = cursor.fetchone()
    
    if not reserva:
        conn.close()
        raise HTTPException(status_code=404, detail="Reserva no encontrada o enlace no válido.")
        
    # Acotamos los campos de los participantes
    cursor.execute("""
        SELECT id, nombre, apellidos, edad 
        FROM participantes 
        WHERE reserva_id = ?
    """, (reserva["id"],))
    participantes = cursor.fetchall()
    
    # Acotamos los campos de la actividad relacionada
    cursor.execute("""
        SELECT id, titulo, fecha, hora, ubicacion, color 
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


@router.delete("/token/{token}")
def cancelar_reserva(token: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id, actividad_id, num_personas FROM reservas WHERE token = ?", (token,))
        reserva = cursor.fetchone()
        
        if not reserva:
            raise HTTPException(status_code=404, detail="Reserva no encontrada.")
            
        reserva_id = reserva["id"]
        actividad_id = reserva["actividad_id"]
        num_personas = reserva["num_personas"]
        
        # Devolver las plazas ocupadas a la actividad de forma segura
        cursor.execute("""
            UPDATE actividades 
            SET plazas_ocupadas = MAX(0, plazas_ocupadas - ?) 
            WHERE id = ?
        """, (num_personas, actividad_id))
        
        cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
        conn.commit()
        
        return {
            "status": "success",
            "message": "Reserva cancelada con éxito. Las plazas han quedado liberadas."
        }
        
    except HTTPException as he:
        conn.rollback()
        raise he
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error interno al cancelar: {str(e)}")
    finally:
        conn.close()