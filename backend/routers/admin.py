import os
import re
import hmac
import shutil
import json
import unicodedata
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks, status, Form, UploadFile, File
from pydantic import BaseModel
from typing import Optional, List
from fastapi.responses import FileResponse

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
    fecha: Optional[str] = None
    hora: Optional[str] = None
    ubicacion: Optional[str] = None
    color: Optional[str] = None
    descripcion: Optional[str] = None
    detalles: Optional[str] = None
    oharrak: Optional[str] = None
    precio: Optional[float] = None
    imagen1: Optional[str] = None
    imagen2: Optional[str] = None
    tipo: Optional[str] = None
    proyecto: Optional[str] = None
    publicar: Optional[bool] = None
    stripeId: Optional[str] = None
    reservas: Optional[bool] = None
    tipoReserva: Optional[str] = None
    linkReserva: Optional[str] = None
    link_reserva: Optional[str] = None
    estadoReserva: Optional[str] = None
    plazas_totales: Optional[int] = None

class ActividadAdminCreate(BaseModel):
    id: Optional[int] = None
    titulo: str
    fecha: str
    hora: str
    ubicacion: Optional[str] = ""
    color: Optional[str] = "#0b8a4c"
    descripcion: Optional[str] = ""
    detalles: Optional[str] = ""
    oharrak: Optional[str] = ""
    precio: Optional[float] = 0.0
    imagen1: Optional[str] = "/imagenes/actividades/default.jpg"
    imagen2: Optional[str] = "/imagenes/actividades/default.jpg"
    tipo: Optional[str] = "general"
    proyecto: Optional[str] = "general"
    publicar: bool = True
    stripeId: Optional[str] = None
    reservas: bool = True
    tipoReserva: Optional[str] = "web"
    linkReserva: Optional[str] = None
    link_reserva: Optional[str] = None
    estadoReserva: Optional[str] = "disponible"
    plazas_totales: int = 20


# ==============================================================================
# FUNCIÓN AUXILIAR: LIMPIEZA DE NOMBRES DE ARCHIVO
# ==============================================================================
def limpiar_nombre_archivo(nombre: str) -> str:
    nombre_base, ext = os.path.splitext(nombre)
    nombre_base = unicodedata.normalize('NFKD', nombre_base).encode('ASCII', 'ignore').decode('utf-8')
    nombre_base = re.sub(r'[^a-zA-Z0-9_-]', '_', nombre_base).lower()
    return f"{nombre_base}{ext.lower()}"

# ==============================================================================
# SINCRONIZACIÓN AUTOMÁTICA DE ACTIVIDADES A JSON
# ==============================================================================
def sincronizar_json_actividades(cursor):
    """
    Vuelca el estado actual de la tabla actividades a un archivo JSON.
    Se guarda en la carpeta persistente /app/data y en la raíz del backend.
    """
    cursor.execute("""
        SELECT id, titulo, fecha, hora, ubicacion, color, descripcion, detalles, 
               oharrak, precio, imagen1, imagen2, tipo, proyecto, publicar, 
               stripeId, reservas, tipoReserva, linkReserva, estadoReserva, 
               plazas_totales, plazas_ocupadas
        FROM actividades
        ORDER BY fecha ASC, hora ASC
    """)
    filas = cursor.fetchall()
    actividades_list = []

    for f in filas:
        d = dict(f)
        # Normalizar booleanos para JSON estándar
        d["publicar"] = bool(d["publicar"])
        d["reservas"] = bool(d["reservas"])
        actividades_list.append(d)

    # 1. Ruta persistente (dentro del volumen montado en /opt/geobizi/data)
    ruta_persistente = os.path.join("data", "actividades.json")
    with open(ruta_persistente, "w", encoding="utf-8") as archivo:
        json.dump(actividades_list, archivo, ensure_ascii=False, indent=2)

    # 2. Copia local directa (si existe la raíz accesible)
    try:
        with open("actividades.json", "w", encoding="utf-8") as archivo_raiz:
            json.dump(actividades_list, archivo_raiz, ensure_ascii=False, indent=2)
    except Exception:
        pass
    
# ==============================================================================
# 1. LOGIN
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
# 2. LISTADO COMPLETO DE ACTIVIDADES
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
            ORDER BY a.fecha DESC, a.hora DESC
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
            SELECT * FROM reservas 
            WHERE actividad_id = ? AND estado IN ('confirmada', 'pendiente_confirmacion')
            ORDER BY id ASC
        """, (actividad_id,))
        reservas = [dict(r) for r in cursor.fetchall()]

        for r in reservas:
            cursor.execute("SELECT * FROM participantes WHERE reserva_id = ?", (r["id"],))
            r["participantes"] = [dict(p) for p in cursor.fetchall()]

        cursor.execute("""
            SELECT * FROM reservas 
            WHERE actividad_id = ? AND estado = 'lista_espera'
            ORDER BY id ASC
        """, (actividad_id,))
        espera = [dict(e) for e in cursor.fetchall()]

        return {
            "actividad": dict(actividad),
            "reservas": reservas,
            "lista_espera": espera
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en base de datos: {str(e)}")
    finally:
        conn.close()


# ==============================================================================
# 4. CREAR NUEVA ACTIVIDAD (COLUMNAS SINCRONIZADAS)
# ==============================================================================
@router.post("/actividades", dependencies=[Depends(verificar_token_admin)])
def crear_actividad_admin(datos: ActividadAdminCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Calcular ID autoincremental si no se envía o viene a None
        if not datos.id:
            cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM actividades")
            nuevo_id = cursor.fetchone()[0]
        else:
            nuevo_id = datos.id
            cursor.execute("SELECT id FROM actividades WHERE id = ?", (nuevo_id,))
            if cursor.fetchone():
                raise HTTPException(status_code=400, detail=f"Ya existe una actividad con el ID {nuevo_id}.")

        link_reserva_final = datos.linkReserva if datos.linkReserva is not None else datos.link_reserva

        cursor.execute("""
            INSERT INTO actividades (
                id, titulo, fecha, hora, ubicacion, color, descripcion, detalles, oharrak,
                precio, imagen1, imagen2, tipo, proyecto, publicar, stripeId,
                reservas, tipoReserva, linkReserva, estadoReserva, plazas_totales, plazas_ocupadas
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
        """, (
            nuevo_id, datos.titulo, datos.fecha, datos.hora, datos.ubicacion, datos.color,
            datos.descripcion, datos.detalles, datos.oharrak, datos.precio,
            datos.imagen1, datos.imagen2, datos.tipo, datos.proyecto,
            int(datos.publicar), datos.stripeId, int(datos.reservas),
            datos.tipoReserva, link_reserva_final, datos.estadoReserva, datos.plazas_totales
        ))
        sincronizar_json_actividades(cursor)
        conn.commit()
        return {"status": "success", "message": "Actividad guardada correctamente", "id": nuevo_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear actividad: {str(e)}")
    finally:
        conn.close()


# ==============================================================================
# 5. ACTUALIZAR ACTIVIDAD
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
            return {"status": "info", "message": "Sin cambios."}

        # Normalizar linkReserva
        if "link_reserva" in datos_dict:
            val = datos_dict.pop("link_reserva")
            if "linkReserva" not in datos_dict or datos_dict["linkReserva"] is None:
                datos_dict["linkReserva"] = val

        # Convertir booleanos
        if "publicar" in datos_dict:
            datos_dict["publicar"] = int(datos_dict["publicar"])
        if "reservas" in datos_dict:
            datos_dict["reservas"] = int(datos_dict["reservas"])

        # Filtrar exclusivamente columnas reales de la tabla
        columnas_validas = {
            "titulo", "fecha", "hora", "ubicacion", "color", "descripcion", 
            "detalles", "oharrak", "precio", "imagen1", "imagen2", "tipo", 
            "proyecto", "publicar", "stripeId", "reservas", "tipoReserva", 
            "linkReserva", "estadoReserva", "plazas_totales"
        }
        datos_limpios = {k: v for k, v in datos_dict.items() if k in columnas_validas}

        if not datos_limpios:
            return {"status": "info", "message": "No hay campos válidos para actualizar."}

        set_clause = ", ".join([f"{k} = ?" for k in datos_limpios.keys()])
        valores = list(datos_limpios.values()) + [actividad_id]

        cursor.execute(f"UPDATE actividades SET {set_clause} WHERE id = ?", valores)

        if "plazas_totales" in datos_limpios and datos_limpios["plazas_totales"] > plazas_antiguas:
            nuevas_plazas = datos_limpios["plazas_totales"] - plazas_antiguas
            reasignar_plazas_liberadas(actividad_id, nuevas_plazas, cursor, background_tasks)
        
        sincronizar_json_actividades(cursor)
        conn.commit()
        return {"status": "success", "message": "Actividad actualizada correctamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar: {str(e)}")
    finally:
        conn.close()


# ==============================================================================
# 6. CANCELAR RESERVA
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

        return {"status": "success", "message": f"Reserva #{reserva_id} cancelada correctamente."}
    finally:
        conn.close()

# ==============================================================================
# ELIMINAR ACTIVIDAD EN CASCADA (CON SUS RESERVAS Y PARTICIPANTES)
# ==============================================================================
@router.delete("/actividades/{actividad_id}", dependencies=[Depends(verificar_token_admin)])
def eliminar_actividad_admin(actividad_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, titulo FROM actividades WHERE id = ?", (actividad_id,))
        actividad = cursor.fetchone()
        if not actividad:
            raise HTTPException(status_code=404, detail="La actividad no existe.")

        # 1. Eliminar participantes de las reservas vinculadas a esta actividad
        cursor.execute("""
            DELETE FROM participantes 
            WHERE reserva_id IN (SELECT id FROM reservas WHERE actividad_id = ?)
        """, (actividad_id,))

        # 2. Eliminar las reservas de esta actividad
        cursor.execute("DELETE FROM reservas WHERE actividad_id = ?", (actividad_id,))

        # 3. Eliminar la actividad
        cursor.execute("DELETE FROM actividades WHERE id = ?", (actividad_id,))

        sincronizar_json_actividades(cursor)
        conn.commit()
        return {
            "status": "success", 
            "message": f"Actividad #{actividad_id} ('{actividad['titulo']}') eliminada con éxito."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar actividad: {str(e)}")
    finally:
        conn.close()

# ==============================================================================
# 7. SUBIR IMAGEN CON NOMBRE PERSONALIZADO Y SOPORTE AVIF
# ==============================================================================
@router.post("/upload-imagen", dependencies=[Depends(verificar_token_admin)])
def subir_imagen_actividad(
    archivo: UploadFile = File(...),
    nombre_personalizado: Optional[str] = Form(None)
):
    extension = os.path.splitext(archivo.filename)[1].lower()
    if extension not in [".jpg", ".jpeg", ".png", ".webp", ".avif"]:
        raise HTTPException(status_code=400, detail="Formato no admitido. Usa JPG, PNG, WebP o AVIF.")

    if nombre_personalizado and nombre_personalizado.strip():
        base_user, ext_user = os.path.splitext(nombre_personalizado.strip())
        if ext_user.lower() in [".jpg", ".jpeg", ".png", ".webp", ".avif"]:
            nombre_origen = nombre_personalizado.strip()
        else:
            nombre_origen = f"{nombre_personalizado.strip()}{extension}"
    else:
        nombre_origen = archivo.filename

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
# 8. BIBLIOTECA MULTIMEDIA
# ==============================================================================
@router.get("/imagenes", dependencies=[Depends(verificar_token_admin)])
def listar_imagenes_disponibles():
    carpeta = os.path.join("uploads", "actividades")
    if not os.path.exists(carpeta):
        return []

    archivos = []
    extensiones_validas = (".jpg", ".jpeg", ".png", ".webp", ".avif")
    for f in os.listdir(carpeta):
        if f.lower().endswith(extensiones_validas):
            archivos.append({
                "nombre": f,
                "url": f"/uploads/actividades/{f}"
            })
    return sorted(archivos, key=lambda x: x["nombre"])

# ==============================================================================
# DESCARGAR COPIA DE SEGURIDAD ACTIVIDADES.JSON
# ==============================================================================
@router.get("/descargar-json", dependencies=[Depends(verificar_token_admin)])
def descargar_actividades_json():
    ruta = os.path.join("data", "actividades.json")
    if not os.path.exists(ruta):
        ruta = "actividades.json"
    
    if not os.path.exists(ruta):
        raise HTTPException(status_code=404, detail="El archivo no existe todavía.")

    return FileResponse(
        path=ruta,
        filename="actividades.json",
        media_type="application/json"
    )