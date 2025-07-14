from fastapi import FastAPI
from . import init_db
import time

# Intenta crear las tablas de la base de datos al iniciar
# Se añade un reintento simple por si el contenedor de la BD tarda en arrancar
time.sleep(5) # Espera 5 segundos antes de intentar conectar
try:
    init_db.init_db()
except Exception as e:
    print(f"No se pudo inicializar la base de datos: {e}")
    print("Reintentando en 5 segundos...")
    time.sleep(5)
    try:
        init_db.init_db()
    except Exception as e_retry:
        print(f"Fallo en el reintento de inicialización de la BD: {e_retry}")


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Database is set up!"}
