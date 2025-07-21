from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal
from database.models import Persona as PersonaModel
from schemas.persona import PersonaCreate, PersonaUpdate, PersonaOut
from controlador.validaciones.validador_persona import validar_persona_create, validar_persona_update
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/admin/personas", response_model=PersonaOut)
def crear_persona(persona: PersonaCreate, db: Session = Depends(get_db)):
    try:
        validar_persona_create(persona)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    db_persona = db.query(PersonaModel).filter(PersonaModel.email == persona.email).first()
    if db_persona:
        raise HTTPException(status_code=400, detail="El email ya está registrado.")
        
    nueva_persona = PersonaModel(**persona.model_dump())
    db.add(nueva_persona)
    db.commit()
    db.refresh(nueva_persona)
    return nueva_persona

@router.get("/admin/personas", response_model=List[PersonaOut])
def listar_personas(db: Session = Depends(get_db)):
    return db.query(PersonaModel).filter(PersonaModel.activo == 1).all()

@router.get("/admin/personas/inactivas", response_model=List[PersonaOut])
def listar_personas_inactivas(db: Session = Depends(get_db)):
    return db.query(PersonaModel).filter(PersonaModel.activo == 0).all()

@router.put("/admin/personas/{id_persona}", response_model=PersonaOut)
def modificar_persona(id_persona: int, persona: PersonaUpdate, db: Session = Depends(get_db)):
    persona_db = db.query(PersonaModel).filter(PersonaModel.id_persona == id_persona, PersonaModel.activo == 1).first()
    if not persona_db:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    
    try:
        validar_persona_update(persona)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    update_data = persona.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(persona_db, key, value)
    
    db.commit()
    db.refresh(persona_db)
    return persona_db

@router.delete("/admin/personas/{id_persona}")
def desactivar_persona(id_persona: int, db: Session = Depends(get_db)):
    persona_db = db.query(PersonaModel).filter(PersonaModel.id_persona == id_persona, PersonaModel.activo == 1).first()
    if not persona_db:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    persona_db.activo = 0
    db.commit()
    return {"msg": "Persona desactivada"}

@router.put("/admin/personas/{id_persona}/reactivar", response_model=PersonaOut)
def reactivar_persona(id_persona: int, db: Session = Depends(get_db)):
    persona_db = db.query(PersonaModel).filter(PersonaModel.id_persona == id_persona).first()
    if not persona_db:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    persona_db.activo = 1
    db.commit()
    db.refresh(persona_db)
    return persona_db
