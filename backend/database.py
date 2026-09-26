import sqlite3
import json
import os

DB_PATH = "data/geobizi.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Tabla de Actividades con todos tus campos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS actividades (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            fecha TEXT NOT NULL,
            hora TEXT NOT NULL,
            ubicacion TEXT,
            color TEXT,
            descripcion TEXT,
            detalles TEXT,
            oharrak TEXT,
            precio REAL DEFAULT 0,
            imagen1 TEXT,
            imagen2 TEXT,
            tipo TEXT,
            proyecto TEXT,
            publicar BOOLEAN DEFAULT 1,
            stripeId TEXT,
            reservas BOOLEAN DEFAULT 1,
            tipoReserva TEXT,
            linkReserva TEXT,
            estadoReserva TEXT,
            plazas_totales INTEGER DEFAULT 20,
            plazas_ocupadas INTEGER DEFAULT 0
        )
    """)
    
    # Tabla de Reservas principales
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            actividad_id INTEGER,
            nombre_contacto TEXT NOT NULL,
            apellidos_contacto TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            num_personas INTEGER NOT NULL,
            token TEXT UNIQUE NOT NULL,
            permiso_fotos BOOLEAN DEFAULT 0,
            observaciones TEXT,
            FOREIGN KEY (actividad_id) REFERENCES actividades (id)
        )
    """)

    # Tabla de Participantes (asistentes con nombre y edad)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS participantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reserva_id INTEGER,
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            edad INTEGER NOT NULL,
            FOREIGN KEY (reserva_id) REFERENCES reservas (id) ON DELETE CASCADE
        )
    """)
    
    conn.commit()
    
    # Volcado automático desde el JSON si la tabla está vacía
    cursor.execute("SELECT COUNT(*) FROM actividades")
    if cursor.fetchone()[0] == 0:
        json_path = "actividades.json"
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                acts = json.load(f)
                for a in acts:
                    cursor.execute("""
                        INSERT OR IGNORE INTO actividades (
                            id, titulo, fecha, hora, ubicacion, color, descripcion, 
                            detalles, oharrak, precio, imagen1, imagen2, tipo, proyecto, 
                            publicar, stripeId, reservas, tipoReserva, linkReserva, estadoReserva
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        a.get("id"), a.get("titulo"), a.get("fecha"), a.get("hora"),
                        a.get("ubicacion"), a.get("color"), a.get("descripcion"),
                        a.get("detalles"), a.get("oharrak"), a.get("precio", 0),
                        a.get("imagen1"), a.get("imagen2"), a.get("tipo"), a.get("proyecto"),
                        1 if a.get("publicar", True) else 0, a.get("stripeId", ""),
                        1 if a.get("reservas", False) else 0, a.get("tipoReserva"),
                        a.get("linkReserva"), a.get("estadoReserva")
                    ))
                conn.commit()
    conn.close()