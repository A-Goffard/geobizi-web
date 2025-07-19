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
            persona.nombre = obj.nombre
            persona.apellido = obj.apellido
            persona.email = obj.email
            persona.telefono = obj.telefono
            persona.dni = obj.dni
            persona.direccion = obj.direccion
            persona.cp = obj.cp
            persona.poblacion = obj.poblacion
            persona.pais = obj.pais
            persona.observaciones = obj.observaciones
            persona.fecha_nacimiento = obj.fecha_nacimiento
            persona.genero = obj.genero
            db.commit()
            db.refresh(persona)
        return persona

    def eliminar(self, db, id):
        persona = db.query(Persona).filter(Persona.id_persona == id).first()
        db.delete(persona)
        db.commit()
        return persona
