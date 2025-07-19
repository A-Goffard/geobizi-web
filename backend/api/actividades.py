from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal
from database.models import Actividad as ActividadModel
from schemas.actividad import ActividadCreate, ActividadUpdate, ActividadOut
from typing import List
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/admin/actividades", response_model=ActividadOut)
def crear_actividad(actividad: ActividadCreate, db: Session = Depends(get_db)):
    nueva_actividad = ActividadModel(**actividad.model_dump(), created_at=datetime.utcnow(), updated_at=datetime.utcnow())
    db.add(nueva_actividad)
    db.commit()
    db.refresh(nueva_actividad)
    return nueva_actividad

@router.get("/admin/actividades", response_model=List[ActividadOut])
def listar_actividades(db: Session = Depends(get_db)):
    return db.query(ActividadModel).filter(ActividadModel.activo == 1).all()

@router.get("/admin/actividades/inactivas", response_model=List[ActividadOut])
def listar_actividades_inactivas(db: Session = Depends(get_db)):
    return db.query(ActividadModel).filter(ActividadModel.activo == 0).all()

@router.put("/admin/actividades/{id_actividad}", response_model=ActividadOut)
def modificar_actividad(id_actividad: int, actividad: ActividadUpdate, db: Session = Depends(get_db)):
    actividad_db = db.query(ActividadModel).filter(ActividadModel.id_actividad == id_actividad, ActividadModel.activo == 1).first()
    if not actividad_db:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    
    update_data = actividad.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(actividad_db, key, value)
    
    actividad_db.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(actividad_db)
    return actividad_db

@router.delete("/admin/actividades/{id_actividad}")
def desactivar_actividad(id_actividad: int, db: Session = Depends(get_db)):
    actividad_db = db.query(ActividadModel).filter(ActividadModel.id_actividad == id_actividad, ActividadModel.activo == 1).first()
    if not actividad_db:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    actividad_db.activo = 0
    db.commit()
    return {"msg": "Actividad desactivada"}

@router.put("/admin/actividades/{id_actividad}/reactivar", response_model=ActividadOut)
def reactivar_actividad(id_actividad: int, db: Session = Depends(get_db)):
    actividad_db = db.query(ActividadModel).filter(ActividadModel.id_actividad == id_actividad).first()
    if not actividad_db:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    actividad_db.activo = 1
    db.commit()
    db.refresh(actividad_db)
    return actividad_db
