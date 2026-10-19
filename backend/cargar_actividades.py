import json
import os
import sqlite3
from pathlib import Path

# 1. Determinar la ruta de la base de datos según el entorno
BASE_DIR = Path(__file__).resolve().parent

if os.path.exists("/opt/geobizi/data/geobizi.db"):
    DB_PATH = Path("/opt/geobizi/data/geobizi.db")
elif os.path.exists("/app/data"):
    DB_PATH = Path("/app/data/geobizi.db")
else:
    DB_PATH = BASE_DIR / "data" / "geobizi.db"

# Asegurar que la carpeta contenedora exista
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
JSON_PATH = BASE_DIR / "actividades.json"

print(f"--> Base de datos: {DB_PATH}")
print(f"--> Archivo JSON:  {JSON_PATH}")

if not JSON_PATH.exists():
    print(f"❌ Error: No se encontró el archivo {JSON_PATH}")
    exit(1)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 2. Crear la tabla actividades si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS actividades (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    fecha TEXT NOT NULL,
    hora TEXT NOT NULL,
    ubicacion TEXT NOT NULL,
    color TEXT,
    descripcion TEXT,
    detalles TEXT,
    publico TEXT,
    precio REAL DEFAULT 0,
    imagen1 TEXT,
    imagen2 TEXT,
    tipo TEXT,
    proyecto TEXT,
    publicar INTEGER DEFAULT 1,
    reservas INTEGER DEFAULT 0,
    link_reserva TEXT,
    plazas_totales INTEGER DEFAULT 20,
    plazas_ocupadas INTEGER DEFAULT 0,
    observaciones TEXT
)
""")

# 3. Verificar y añadir columnas que pudieran faltar si la tabla ya existía
cursor.execute("PRAGMA table_info(actividades)")
columnas_existentes = [col[1] for col in cursor.fetchall()]

columnas_requeridas = {
    "detalles": "TEXT",
    "publico": "TEXT",
    "link_reserva": "TEXT",
    "plazas_totales": "INTEGER DEFAULT 20",
    "plazas_ocupadas": "INTEGER DEFAULT 0",
    "observaciones": "TEXT"
}

for col, tipo in columnas_requeridas.items():
    if col not in columnas_existentes:
        print(f"Añadiendo columna faltante '{col}' a la tabla...")
        cursor.execute(f"ALTER TABLE actividades ADD COLUMN {col} {tipo}")

conn.commit()

# 4. Leer el JSON e insertar / actualizar
with open(JSON_PATH, "r", encoding="utf-8") as f:
    actividades = json.load(f)

insertadas = 0
actualizadas = 0

for act in actividades:
    act_id = act.get("id")
    titulo = act.get("titulo", "")
    fecha = act.get("fecha", "")
    hora = act.get("hora", "")
    ubicacion = act.get("ubicacion", "")
    color = act.get("color", "green")
    descripcion = act.get("descripcion", "")
    detalles = act.get("detalles", "")
    publico = act.get("detalles", "")  # Mantenemos ambos por compatibilidad
    precio = float(act.get("precio", 0))
    imagen1 = act.get("imagen1", "")
    imagen2 = act.get("imagen2", "")
    tipo = act.get("tipo", "actividad")
    proyecto = act.get("proyecto", "general")
    publicar = 1 if act.get("publicar", True) else 0
    reservas = 1 if act.get("reservas", False) else 0
    link_reserva = act.get("linkReserva") or act.get("link_reserva") or None
    plazas_totales = int(act.get("plazas_totales", 20))
    observaciones = act.get("oharrak") or act.get("observaciones") or None

    # Comprobar si ya existe
    cursor.execute("SELECT plazas_ocupadas FROM actividades WHERE id = ?", (act_id,))
    fila = cursor.fetchone()

    if fila is None:
        # Inserción inicial
        cursor.execute("""
            INSERT INTO actividades (
                id, titulo, fecha, hora, ubicacion, color, descripcion,
                detalles, publico, precio, imagen1, imagen2, tipo,
                proyecto, publicar, reservas, link_reserva, plazas_totales,
                plazas_ocupadas, observaciones
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?)
        """, (
            act_id, titulo, fecha, hora, ubicacion, color, descripcion,
            detalles, publico, precio, imagen1, imagen2, tipo,
            proyecto, publicar, reservas, link_reserva, plazas_totales, observaciones
        ))
        insertadas += 1
    else:
        # Actualización respetando las plazas_ocupadas existentes
        cursor.execute("""
            UPDATE actividades SET
                titulo = ?, fecha = ?, hora = ?, ubicacion = ?, color = ?,
                descripcion = ?, detalles = ?, publico = ?, precio = ?,
                imagen1 = ?, imagen2 = ?, tipo = ?, proyecto = ?,
                publicar = ?, reservas = ?, link_reserva = ?, plazas_totales = ?,
                observaciones = ?
            WHERE id = ?
        """, (
            titulo, fecha, hora, ubicacion, color, descripcion,
            detalles, publico, precio, imagen1, imagen2, tipo,
            proyecto, publicar, reservas, link_reserva, plazas_totales,
            observaciones, act_id
        ))
        actualizadas += 1

conn.commit()
conn.close()

print(f"\n✅ Proceso finalizado:")
print(f"   - Actividades nuevas insertadas: {insertadas}")
print(f"   - Actividades actualizadas:      {actualizadas}")
print(f"   - Total procesadas:              {len(actividades)}")