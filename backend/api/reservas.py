from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from database.database import SessionLocal
from database.models import Reserva as ReservaModel
from schemas.reserva import ReservaCreate, ReservaOut, ReservaUpdate
from controlador.validaciones.validador_reserva import validar_reserva_create
from controlador.gestores.reserva_gestor import ReservaGestor
from utils.email_service import enviar_confirmacion_reserva
from typing import List

router = APIRouter()
reserva_gestor = ReservaGestor()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/admin/reservas", response_model=List[ReservaOut])
def listar_reservas(db: Session = Depends(get_db)):
    try:
        reservas = db.query(ReservaModel).options(
            selectinload(ReservaModel.persona),
            selectinload(ReservaModel.actividad)
        ).all()
        return reservas
    except Exception as e:
        import traceback
        print("Error en listar_reservas:", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

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
    # Enviar email de confirmación al cliente
    if reserva_db.persona and reserva_db.actividad:
        reserva_data = {
            "id_reserva": reserva_db.id_reserva,
            "nombre_cliente": reserva_db.persona.nombre + " " + (reserva_db.persona.apellido or ""),
            "email_cliente": reserva_db.persona.email,
            "telefono": reserva_db.persona.telefono,
            "actividad_nombre": reserva_db.actividad.nombre,
            "actividad_fecha": reserva_db.actividad.fecha.strftime("%Y-%m-%d") if reserva_db.actividad.fecha else "",
            "actividad_hora": reserva_db.actividad.hora,
            "numero_personas": reserva_db.numero_personas,
            "precio_total": (reserva_db.actividad.precio or 0) * (reserva_db.numero_personas or 1)
        }
        enviar_confirmacion_reserva(reserva_db.persona.email, reserva_data)
    return {"msg": "Confirmación enviada"}

@router.post("/api/admin/reservas", response_model=ReservaOut)
def crear_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    try:
        validar_reserva_create(reserva)
        nueva_reserva = reserva_gestor.crear(db, reserva)
        return nueva_reserva
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        import traceback
        print("Error en crear_reserva:", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
