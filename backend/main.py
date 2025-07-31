from fastapi import FastAPI, Depends, HTTPException, status
from database.init_db import init_db
from sqlalchemy.orm import Session
from database.database import SessionLocal
from database.models import Usuario
import time
from api.admin import router as admin_router
from api.usuarios import router as usuarios_router
from api.actividades import router as actividades_router
from api.empresas import router as empresas_router
from api.personas import router as personas_router
from api.reservas import router as reservas_router

try:
    init_db()
except Exception as e:
    print(f"No se pudo inicializar la base de datos: {e}")
    print("Reintentando en 5 segundos...")
    time.sleep(5)
    try:
        init_db()
    except Exception as e_retry:
        print(f"Fallo en el reintento de inicialización de la BD: {e_retry}")


app = FastAPI()

# Incluye los routers con y sin el prefijo /api
app.include_router(admin_router)
app.include_router(usuarios_router, prefix="/api")
app.include_router(usuarios_router)  # <-- Añadido sin prefix
app.include_router(actividades_router, prefix="/api")
app.include_router(actividades_router)  # <-- Añadido sin prefix
app.include_router(empresas_router, prefix="/api")
app.include_router(empresas_router)  # <-- Añadido sin prefix
app.include_router(personas_router, prefix="/api")
app.include_router(personas_router)  # <-- Añadido sin prefix
app.include_router(reservas_router, prefix="/api")
app.include_router(reservas_router)  # <-- Añadido sin prefix

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_superuser(db: Session = Depends(get_db), email: str = None):
    user = db.query(Usuario).filter(Usuario.email == email, Usuario.is_superuser == True).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No autorizado")
    return user

@app.get("/")
def read_root():
    return {"Hello": "Database is set up!"}
    return {"Hello": "Database is set up!"}
