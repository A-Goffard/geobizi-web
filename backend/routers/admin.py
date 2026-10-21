import os
import re
import hmac
import shutil
import unicodedata
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks, status, Form, UploadFile, File
from pydantic import BaseModel
from typing import Optional, List

from core.database import get_db_connection
from core.security import generar_token_admin, verificar_token_admin
from services.reserva_service import reasignar_plazas_liberadas
from services.email_service import enviar_correo_cancelacion, notificar_admin_cancelacion

router = APIRouter(tags=["Administración"])

# ==============================================================================
# ESQUEMAS PYDANTIC
# ==============================================================================
class LoginRequest(BaseModel):
    password: str

class ActividadAdminUpdate(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    fecha: Optional[str] = None
    hora: Optional[str] = None
    ubicacion: Optional[str] = None
    precio: Optional[float] = None
    detalles: Optional[str] = None
    plazas_totales: Optional[int] = None
    publicar: Optional[bool] = None
    reservas: Optional[bool] = None
    link_reserva: Optional[str] = None
    color: Optional[str] = None
    proyecto: Optional[str] = None
    imagen1: Optional[str] = None
    imagen2: Optional[str] = None

class ActividadAdminCreate(BaseModel):
    id: Optional[int] = None
    titulo: str
    descripcion: Optional[str] = ""
    fecha: str
    hora: str
    ubicacion: Optional[str] = ""
    precio: Optional[float] = 0.0
    detalles: Optional[str] = ""
    plazas_totales: int = 20
    publicar: bool = True
    reservas: bool = True
    link_reserva: Optional[str] = None
    color: Optional[str] = "#0b8a4c"
    proyecto: Optional[str] = "general"
    imagen1: Optional[str] = "/imagenes/actividades/default.jpg"
    imagen2: Optional[str] = "/imagenes/actividades/default.jpg"


# ==============================================================================
# FUNCIÓN AUXILIAR: LIMPIEZA DE NOMBRES DE ARCHIVO
# ==============================================================================
def limpiar_nombre_archivo(nombre: str) -> str:
    """Convierte 'Ruta Botánica Zalla 2026.JPG' en 'ruta_botanica_zalla_2026.jpg'"""
    nombre_base, ext = os.path.splitext(nombre)
    nombre_base = unicodedata.normalize('NFKD', nombre_base).encode('ASCII', 'ignore').decode('utf-8')
    nombre_base = re.sub(r'[^a-zA-Z0-9_-]', '_', nombre_base).lower()
    return f"{nombre_base}{ext.lower()}"


# ==============================================================================
# 1. LOGIN DE ADMINISTRACIÓN
# ==============================================================================
@router.post("/login")
def admin_login(datos: LoginRequest):
    admin_pass = os.getenv("ADMIN_PASSWORD", "admin123")
    if not hmac.compare_digest(datos.password, admin_pass):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña incorrecta."
        )
    return {
        "status": "success",
        "token": generar_token_admin()
    }


# ==============================================================================
# 2. LISTADO COMPLETO DE ACTIVIDADES CON MÉTRICAS
# ==============================================================================
@router.get("/actividades", dependencies=[Depends(verificar_token_admin)])
def listar_actividades_admin():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT 
                a.*,
                COALESCE((SELECT COUNT(*) FROM reservas r WHERE r.actividad_id = a.id AND r.estado = 'confirmada'), 0) AS total_reservas,
                COALESCE((SELECT COUNT(*) FROM reservas r WHERE r.actividad_id = a.id AND r.estado = 'lista_espera'), 0) AS total_espera,
                COALESCE((SELECT SUM(num_personas) FROM reservas r WHERE r.actividad_id = a.id AND r.estado = 'confirmada'), 0) AS plazas_confirmadas
            FROM actividades a
            ORDER BY a.fecha ASC, a.hora ASC
        """)
        filas = cursor.fetchall()
        return [dict(f) for f in filas]
    finally:
        conn.close()


# ==============================================================================
# 3. LISTADO DE PARTICIPANTES POR ACTIVIDAD
# ==============================================================================
@router.get("/actividades/{actividad_id}/participantes", dependencies=[Depends(verificar_token_admin)])
def obtener_participantes_actividad(actividad_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM actividades WHERE id = ?", (actividad_id,))
        actividad = cursor.fetchone()
        if not actividad:
            raise HTTPException(status_code=404, detail="Actividad no encontrada.")

        cursor.execute("""
            SELECT id, nombre_contacto, apellidos_contacto, email, phone, num_personas, permiso_fotos, observaciones, estado, token, fecha_registro
            FROM reservas 
            WHERE actividad_id = ? AND estado IN ('confirmada', 'pendiente_confirmacion')
            ORDER BY id ASC
        """, (actividad_id,))
        reservas = [dict(r) for r in cursor.fetchall()]

        for r in reservas:
            cursor.execute("SELECT id, nombre, apellidos, edad FROM participantes WHERE reserva_id = ?", (r["id"],))
            r["participantes"] = [dict(p) for p in cursor.fetchall()]

        cursor.execute("""
            SELECT id, nombre_contacto, apellidos_contacto, email, phone, num_personas, fecha_registro, estado
            FROM reservas 
            WHERE actividad_id = ? AND estado = 'lista_espera'
            ORDER BY id ASC
        """, (actividad_id,))
        espera = [dict(e) for e in cursor.fetchall()]

        return {
            "actividad": dict(actividad),
            "reservas": reservas,
            "lista_espera": espera
        }
    finally:
        conn.close()


# ==============================================================================
# 4. CREAR NUEVA ACTIVIDAD (CON ID MANUAL O AUTOMÁTICO)
# ==============================================================================
@router.post("/actividades", dependencies=[Depends(verificar_token_admin)])
def crear_actividad_admin(datos: ActividadAdminCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if not datos.id:
            cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM actividades")
            nuevo_id = cursor.fetchone()[0]
        else:
            nuevo_id = datos.id
            cursor.execute("SELECT id FROM actividades WHERE id = ?", (nuevo_id,))
            if cursor.fetchone():
                raise HTTPException(status_code=400, detail=f"Ya existe una actividad con el ID {nuevo_id}.")

        cursor.execute("""
            INSERT INTO actividades (
                id, titulo, descripcion, fecha, hora, ubicacion, precio, detalles, 
                plazas_totales, plazas_ocupadas, publicar, reservas, link_reserva, 
                color, proyecto, imagen1, imagen2
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?, ?, ?, ?, ?, ?)
        """, (
            nuevo_id, datos.titulo, datos.descripcion, datos.fecha, datos.hora, 
            datos.ubicacion, datos.precio, datos.detalles, datos.plazas_totales, 
            int(datos.publicar), int(datos.reservas), datos.link_reserva, 
            datos.color, datos.proyecto, datos.imagen1, datos.imagen2
        ))
        conn.commit()
        return {"status": "success", "message": "Actividad creada correctamente", "id": nuevo_id}
    finally:
        conn.close()


# ==============================================================================
# 5. ACTUALIZAR ACTIVIDAD (AFORO, DATOS O ESTADO)
# ==============================================================================
@router.put("/actividades/{actividad_id}", dependencies=[Depends(verificar_token_admin)])
def actualizar_actividad_admin(actividad_id: int, datos: ActividadAdminUpdate, background_tasks: BackgroundTasks):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM actividades WHERE id = ?", (actividad_id,))
        act = cursor.fetchone()
        if not act:
            raise HTTPException(status_code=404, detail="Actividad no encontrada.")

        plazas_antiguas = int(act["plazas_totales"])
        datos_dict = datos.dict(exclude_unset=True)

        if not datos_dict:
            return {"status": "info", "message": "No se enviaron campos para actualizar."}

        if "publicar" in datos_dict:
            datos_dict["publicar"] = int(datos_dict["publicar"])
        if "reservas" in datos_dict:
            datos_dict["reservas"] = int(datos_dict["reservas"])

        set_clause = ", ".join([f"{k} = ?" for k in datos_dict.keys()])
        valores = list(datos_dict.values()) + [actividad_id]

        cursor.execute(f"UPDATE actividades SET {set_clause} WHERE id = ?", valores)

        if "plazas_totales" in datos_dict and datos_dict["plazas_totales"] > plazas_antiguas:
            nuevas_plazas = datos_dict["plazas_totales"] - plazas_antiguas
            reasignar_plazas_liberadas(actividad_id, nuevas_plazas, cursor, background_tasks)

        conn.commit()
        return {"status": "success", "message": "Actividad actualizada correctamente."}
    finally:
        conn.close()


# ==============================================================================
# 6. CANCELAR RESERVA DESDE EL PANEL DE ADMINISTRACIÓN
# ==============================================================================
@router.delete("/reservas/{reserva_id}", dependencies=[Depends(verificar_token_admin)])
def cancelar_reserva_admin(reserva_id: int, background_tasks: BackgroundTasks):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT r.id, r.actividad_id, r.nombre_contacto, r.email, r.phone, r.num_personas, r.estado,
                   a.titulo, a.fecha, a.hora, a.ubicacion
            FROM reservas r
            JOIN actividades a ON r.actividad_id = a.id
            WHERE r.id = ?
        """, (reserva_id,))
        fila = cursor.fetchone()

        if not fila:
            raise HTTPException(status_code=404, detail="La reserva no existe.")

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

        cursor.execute("DELETE FROM participantes WHERE reserva_id = ?", (reserva_id,))
        cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))

        if estado_reserva in ("confirmada", "pendiente_confirmacion"):
            reasignar_plazas_liberadas(actividad_id, plazas_a_liberar, cursor, background_tasks)

        conn.commit()

        background_tasks.add_task(
            enviar_correo_cancelacion,
            email_destino=email_contacto,
            actividad=actividad_datos,
            nombre_contacto=nombre_contacto
        )
        background_tasks.add_task(
            notificar_admin_cancelacion,
            actividad=actividad_datos,
            nombre_contacto=nombre_contacto,
            email_contacto=email_contacto,
            phone=fila["phone"],
            plazas_liberadas=plazas_a_liberar
        )

        return {"status": "success", "message": f"Reserva #{reserva_id} cancelada y plazas reasignadas."}
    finally:
        conn.close()


# ==============================================================================
# 7. SUBIR IMAGEN (CON NOMBRE PERSONALIZADO O ORIGINAL LIMPIO)
# ==============================================================================
@router.post("/upload-imagen", dependencies=[Depends(verificar_token_admin)])
def subir_imagen_actividad(
    archivo: UploadFile = File(...),
    nombre_personalizado: Optional[str] = Form(None)
):
    extension = os.path.splitext(archivo.filename)[1].lower()
    if extension not in [".jpg", ".jpeg", ".png", ".webp"]:
        raise HTTPException(status_code=400, detail="Formato no admitido. Usa JPG, PNG o WebP.")

    nombre_origen = (nombre_personalizado.strip() + extension) if nombre_personalizado else archivo.filename
    nombre_final = limpiar_nombre_archivo(nombre_origen)

    carpeta = os.path.join("uploads", "actividades")
    os.makedirs(carpeta, exist_ok=True)
    ruta_guardado = os.path.join(carpeta, nombre_final)

    with open(ruta_guardado, "wb") as buffer:
        shutil.copyfileobj(archivo.file, buffer)

    return {
        "status": "success",
        "nombre": nombre_final,
        "url": f"/uploads/actividades/{nombre_final}"
    }


# ==============================================================================
# 8. LISTAR TODAS LAS IMÁGENES DISPONIBLES PARA REUTILIZAR
# ==============================================================================
@router.get("/imagenes", dependencies=[Depends(verificar_token_admin)])
def listar_imagenes_disponibles():
    carpeta = os.path.join("uploads", "actividades")
    if not os.path.exists(carpeta):
        return []

    archivos = []
    extensiones_validas = (".jpg", ".jpeg", ".png", ".webp")
    for f in os.listdir(carpeta):
        if f.lower().endswith(extensiones_validas):
            archivos.append({
                "nombre": f,
                "url": f"/uploads/actividades/{f}"
            })
    return sorted(archivos, key=lambda x: x["nombre"])