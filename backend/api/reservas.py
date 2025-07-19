from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from database.database import SessionLocal
from database.models import Reserva as ReservaModel
from schemas.reserva import ReservaCreate, ReservaUpdate, ReservaOut
from typing import List
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/admin/reservas", response_model=ReservaOut)
def crear_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    nueva_reserva = ReservaModel(**reserva.model_dump(), fecha_reserva=datetime.utcnow())
    db.add(nueva_reserva)
    db.commit()
    db.refresh(nueva_reserva)
    return nueva_reserva

@router.get("/admin/reservas", response_model=List[ReservaOut])
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(ReservaModel).options(
        selectinload(ReservaModel.persona),
        selectinload(ReservaModel.actividad)
    ).all()

@router.put("/admin/reservas/{id_reserva}", response_model=ReservaOut)
def modificar_reserva(id_reserva: int, reserva: ReservaUpdate, db: Session = Depends(get_db)):
    reserva_db = db.query(ReservaModel).filter(ReservaModel.id_reserva == id_reserva).first()
    if not reserva_db:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    
    update_data = reserva.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(reserva_db, key, value)
    
    db.commit()
    db.refresh(reserva_db)
    return reserva_db

@router.delete("/admin/reservas/{id_reserva}")
def eliminar_reserva(id_reserva: int, db: Session = Depends(get_db)):
    reserva_db = db.query(ReservaModel).filter(ReservaModel.id_reserva == id_reserva).first()
    if not reserva_db:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    db.delete(reserva_db)
    db.commit()
    return {"msg": "Reserva eliminada"}
