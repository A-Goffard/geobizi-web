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

@router.post("/api/admin/actividades", response_model=ActividadOut)
def crear_actividad(actividad: ActividadCreate, db: Session = Depends(get_db)):
    try:
        validar_actividad_create(actividad)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return actividad_gestor.crear(db, actividad)

@router.get("/api/admin/actividades")
def listar_actividades_admin(db: Session = Depends(get_db)):
    try:
        actividades = db.query(ActividadModel).filter(ActividadModel.activo == 1).all()
        
        result = []
        for actividad in actividades:
            result.append({
                "id_actividad": actividad.id_actividad,
                "nombre": actividad.nombre,
                "tipo": actividad.tipo,
                "lugar": actividad.lugar,
                "fecha": actividad.fecha.isoformat() if actividad.fecha else None,
                "hora": actividad.hora,
                "precio": actividad.precio,
                "activo": actividad.activo
            })
        
        return result
        
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

@router.get("/api/admin/actividades")
def listar_actividades_admin(db: Session = Depends(get_db)):
    """Listar todas las actividades para administración"""
    try:
        actividades = db.query(ActividadModel).filter(ActividadModel.activo == 1).all()
        
        result = []
        for actividad in actividades:
            result.append({
                "id_actividad": actividad.id_actividad,
                "nombre": actividad.nombre,
                "tipo": actividad.tipo,
                "lugar": actividad.lugar,
                "fecha": actividad.fecha.isoformat() if actividad.fecha else None,
                "hora": actividad.hora,
                "precio": actividad.precio,
                "activo": actividad.activo
            })
        
        return result
        
    except Exception as e:
        logger.error(f"Error al listar actividades: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
