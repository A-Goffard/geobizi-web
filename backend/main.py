import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from core.database import init_db
from routers import actividades, reservas, admin

app = FastAPI(title="Geobizi TIK API de Reservas", version="1.0")

# CORS SEGURO: Limpiamos posibles espacios en blanco de cada dominio del .env
raw_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:8080,http://localhost:3000")
origins = [origin.strip() for origin in raw_origins.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

# Inicializar la base de datos y comprobar estado
init_db()

# Registrar los módulos (routers) de la API
app.include_router(actividades.router, prefix="/api")
app.include_router(reservas.router, prefix="/api")
app.include_router(admin.router, prefix="/api/admin")

# Crear y servir la carpeta de imágenes subidas
os.makedirs("uploads/actividades", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")