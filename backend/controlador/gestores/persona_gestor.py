# backend/controlador/gestores/persona_gestor.py
from .base import GestorBase
from database.models import Persona

class PersonaGestor(GestorBase):
    def crear(self, db, obj):
        persona = Persona(
            nombre=obj.nombre,
            apellido=obj.apellido,
            email=obj.email,
            telefono=obj.telefono,
            dni=obj.dni,
            direccion=obj.direccion,
            cp=obj.cp,
            poblacion=obj.poblacion,
            pais=obj.pais,
            observaciones=obj.observaciones,
            fecha_nacimiento=obj.fecha_nacimiento,
            genero=obj.genero
        )
        db.add(persona)
        db.commit()
        db.refresh(persona)
        return persona

    def obtener(self, db, id):
        return db.query(Persona).filter(Persona.id_persona == id).first()

    def actualizar(self, db, id, obj):
        persona = db.query(Persona).filter(Persona.id_persona == id).first()
        if persona:
            update_data = obj.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(persona, key, value)
            db.commit()
            db.refresh(persona)
        return persona

    def eliminar(self, db, id):
        persona = db.query(Persona).filter(Persona.id_persona == id).first()
        if persona:
            persona.activo = 0
            db.commit()
        return persona

    def reactivar(self, db, id):
        persona = db.query(Persona).filter(Persona.id_persona == id).first()
        if persona:
            persona.activo = 1
            db.commit()
            db.refresh(persona)
        return persona

persona_gestor = PersonaGestor()