from fastapi import APIRouter
from database import get_db_connection

router = APIRouter(tags=["Actividades"])

@router.get("/actividades")
def listar_actividades():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Consulta acotada y explícita
    cursor.execute("""
        SELECT id, titulo, fecha, hora, ubicacion, color, descripcion, 
               detalles, oharrak, precio, imagen1, imagen2, tipo, proyecto, 
               publicar, stripeId, reservas, tipoReserva, linkReserva, 
               estadoReserva, plazas_totales, plazas_ocupadas 
        FROM actividades 
        WHERE publicar = 1
    """)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]