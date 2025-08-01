from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal
from database.models import Actividad as ActividadModel
from schemas.actividad import ActividadCreate, ActividadUpdate, ActividadOut
from controlador.validaciones.validador_actividad import validar_actividad_create, validar_actividad_update
from controlador.gestores.actividad_gestor import ActividadGestor
from typing import List
from datetime import datetime
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()
actividad_gestor = ActividadGestor()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/admin/actividades")
def crear_actividad(actividad: ActividadCreate, db: Session = Depends(get_db)):
    print("Datos recibidos para crear actividad:", actividad)
    # Comprobación de duplicados
    existente = db.query(ActividadModel).filter(
        ActividadModel.nombre == actividad.nombre,
        ActividadModel.lugar == actividad.lugar,
        ActividadModel.fecha == actividad.fecha,
        ActividadModel.hora == actividad.hora,
        ActividadModel.activo == 1
    ).first()
    if existente:
        raise HTTPException(
            status_code=400,
            detail="Ya existe una actividad con el mismo nombre, lugar, fecha y hora."
        )
    try:
        validar_actividad_create(actividad)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    nueva_actividad = actividad_gestor.crear(db, actividad)
    return {
        "msg": "Actividad creada correctamente.",
        "actividad": ActividadOut.model_validate(nueva_actividad)
    }

@router.get("/api/admin/actividades", response_model=List[ActividadOut])
def listar_actividades_admin(db: Session = Depends(get_db)):
    try:
        actividades = db.query(ActividadModel).filter(ActividadModel.activo == 1).all()
        return actividades
    except Exception as e:
        logger.error(f"Error al listar actividades: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@router.get("/api/admin/actividades/inactivas", response_model=List[ActividadOut])
def listar_actividades_inactivas(db: Session = Depends(get_db)):
    return db.query(ActividadModel).filter(ActividadModel.activo == 0).all()

@router.put("/api/admin/actividades/{id_actividad}", response_model=ActividadOut)
def modificar_actividad(id_actividad: int, actividad: ActividadUpdate, db: Session = Depends(get_db)):
    actividad_db = actividad_gestor.obtener(db, id_actividad)
    if not actividad_db or actividad_db.activo == 0:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    
    try:
        validar_actividad_update(actividad)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return actividad_gestor.actualizar(db, id_actividad, actividad)

@router.delete("/api/admin/actividades/{id_actividad}")
def desactivar_actividad(id_actividad: int, db: Session = Depends(get_db)):
    actividad_db = actividad_gestor.obtener(db, id_actividad)
    if not actividad_db or actividad_db.activo == 0:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    
    actividad_gestor.eliminar(db, id_actividad)
    return {"msg": "Actividad desactivada"}

@router.put("/api/admin/actividades/{id_actividad}/reactivar", response_model=ActividadOut)
def reactivar_actividad(id_actividad: int, db: Session = Depends(get_db)):
    actividad_db = actividad_gestor.obtener(db, id_actividad)
    if not actividad_db:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    
    return actividad_gestor.reactivar(db, id_actividad)
