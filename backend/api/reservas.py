from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from database.database import SessionLocal
from database.models import Reserva as ReservaModel, Persona as PersonaModel, Actividad as ActividadModel
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/admin/reservas")
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(ReservaModel).options(
        selectinload(ReservaModel.persona),
        selectinload(ReservaModel.actividad)
    ).all()

@router.delete("/api/admin/reservas/{id_reserva}")
def eliminar_reserva(id_reserva: int, db: Session = Depends(get_db)):
    reserva_db = db.query(ReservaModel).filter(ReservaModel.id_reserva == id_reserva).first()
    if not reserva_db:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    db.delete(reserva_db)
    db.commit()
    return {"msg": "Reserva eliminada"}

@router.put("/api/admin/reservas/{id_reserva}/aprobar")
def aprobar_reserva(id_reserva: int, db: Session = Depends(get_db)):
    reserva_db = db.query(ReservaModel).filter(ReservaModel.id_reserva == id_reserva).first()
    if not reserva_db:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    
    reserva_db.aprobada = True
    db.commit()
    return {"msg": "Reserva aprobada"}

@router.put("/api/admin/reservas/{id_reserva}/rechazar")
def rechazar_reserva(id_reserva: int, db: Session = Depends(get_db)):
    reserva_db = db.query(ReservaModel).filter(ReservaModel.id_reserva == id_reserva).first()
    if not reserva_db:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    
    reserva_db.aprobada = False
    db.commit()
    return {"msg": "Reserva rechazada"}

@router.post("/api/admin/reservas/{id_reserva}/enviar-confirmacion")
def enviar_confirmacion(id_reserva: int, db: Session = Depends(get_db)):
    reserva_db = db.query(ReservaModel).filter(ReservaModel.id_reserva == id_reserva).first()
    if not reserva_db:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    
    reserva_db.confirmacion_enviada = True
    db.commit()
    return {"msg": "Confirmación enviada"}
