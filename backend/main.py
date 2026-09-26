import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from routers import actividades, reservas

app = FastAPI(title="Geobizi TIK API de Reservas", version="1.0")

# CORS SEGURO: En lugar de usar ["*"], leemos los dominios permitidos de la variable de entorno o fijamos los locales
origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:8080,http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE"],  # Solo permitimos lo estrictamente necesario
    allow_headers=["Content-Type", "Authorization"],
)

# Inicializar la base de datos y volcar JSON si procede
init_db()

# Registrar los módulos (routers)
# Registrar los módulos (routers) con el prefijo /api
app.include_router(actividades.router, prefix="/api")
app.include_router(reservas.router, prefix="/api")