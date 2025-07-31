from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal
from database.models import Persona as PersonaModel
import logging
from controlador.gestores.persona_gestor import persona_gestor 
from schemas.persona import PersonaOut, PersonaUpdate, PersonaCreate
from controlador.validaciones.validador_persona import validar_persona_update

logger = logging.getLogger(__name__)
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/admin/personas")
def buscar_personas(telefono: str = None, db: Session = Depends(get_db)):
    if telefono:
        personas = db.query(PersonaModel).filter(PersonaModel.telefono == telefono, PersonaModel.activo == 1).all()
        return [
            {
                "id_persona": p.id_persona,
                "nombre": p.nombre,
                "apellido": p.apellido,
                "email": p.email,
                "telefono": p.telefono,
                "dni": p.dni,
                "activo": p.activo
            }
            for p in personas
        ]
    
    try:
        personas = db.query(PersonaModel).filter(PersonaModel.activo == 1).all()
        
        result = []
        for persona in personas:
            result.append({
                "id_persona": persona.id_persona,
                "nombre": persona.nombre,
                "apellido": persona.apellido,
                "email": persona.email,
                "telefono": persona.telefono,
                "dni": persona.dni,
                "activo": persona.activo
            })
        
        return result
        
    except Exception as e:
        logger.error(f"Error al listar personas: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
        
    except Exception as e:
        logger.error(f"Error al listar personas: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    return db.query(PersonaModel).filter(PersonaModel.activo == 0).all()

@router.get("/api/admin/personas/inactivas")
def listar_personas_inactivas(db: Session = Depends(get_db)):
    try:
        personas = db.query(PersonaModel).filter(PersonaModel.activo == 0).all()
        result = []
        for persona in personas:
            result.append({
                "id_persona": persona.id_persona,
                "nombre": persona.nombre,
                "apellido": persona.apellido,
                "email": persona.email,
                "telefono": persona.telefono,
                "dni": persona.dni,
                "activo": persona.activo
            })
        return result
    except Exception as e:
        logger.error(f"Error al listar personas inactivas: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@router.put("/api/admin/personas/{id_persona}", response_model=PersonaOut)
def modificar_persona(id_persona: int, persona: PersonaUpdate, db: Session = Depends(get_db)):
    persona_db = persona_gestor.obtener(db, id_persona)
    if not persona_db or persona_db.activo == 0:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    
    try:
        validar_persona_update(persona)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return persona_gestor.actualizar(db, id_persona, persona)

@router.delete("/api/admin/personas/{id_persona}")
def desactivar_persona(id_persona: int, db: Session = Depends(get_db)):
    persona_db = persona_gestor.obtener(db, id_persona)
    if not persona_db or persona_db.activo == 0:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    
    persona_gestor.eliminar(db, id_persona)
    return {"msg": "Persona desactivada"}

@router.put("/api/admin/personas/{id_persona}/reactivar", response_model=PersonaOut)
def reactivar_persona(id_persona: int, db: Session = Depends(get_db)):
    persona_db = persona_gestor.obtener(db, id_persona)
    if not persona_db:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    
    return persona_gestor.reactivar(db, id_persona)

@router.post("/api/admin/personas", response_model=PersonaOut)
def crear_persona(persona: PersonaCreate, db: Session = Depends(get_db)):
    # Validación básica
    if not persona.nombre or not persona.telefono or not persona.email or not persona.apellido:
        raise HTTPException(status_code=400, detail="Faltan campos obligatorios")
    nueva_persona = PersonaModel(
        nombre=persona.nombre,
        apellido=persona.apellido,
        email=persona.email,
        telefono=persona.telefono,
        dni=persona.dni,
        direccion=persona.direccion,
        cp=persona.cp,
        poblacion=persona.poblacion,
        pais=persona.pais,
        observaciones=persona.observaciones,
        fecha_nacimiento=persona.fecha_nacimiento,
        genero=persona.genero,
        activo=1
    )
    db.add(nueva_persona)
    db.commit()
    db.refresh(nueva_persona)
    return nueva_persona
