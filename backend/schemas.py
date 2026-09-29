from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import List, Optional

class ParticipanteSchema(BaseModel):
    nombre: str
    apellidos: str
    edad: int

class SolicitudReserva(BaseModel):
    actividad_id: int
    nombre_contacto: str
    apellidos_contacto: str
    email: EmailStr
    phone: str
    num_personas: int
    permiso_fotos: bool = False
    observaciones: Optional[str] = None
    participantes: List[ParticipanteSchema]

class ListaEsperaCreate(BaseModel):
    actividad_id: int
    nombre_contacto: Optional[str] = None
    nombre: Optional[str] = None
    apellidos_contacto: Optional[str] = None
    apellidos: Optional[str] = None
    email: EmailStr
    phone: str
    num_personas: int = 1
    permiso_fotos: bool = False
    observaciones: Optional[str] = None
    participantes: List[ParticipanteSchema] = []

    # Permite aceptar tanto 'nombre' como 'nombre_contacto' de forma indistinta
    @model_validator(mode="before")
    def normalizar_campos(cls, values):
        if isinstance(values, dict):
            if "nombre" in values and not values.get("nombre_contacto"):
                values["nombre_contacto"] = values["nombre"]
            if "apellidos" in values and not values.get("apellidos_contacto"):
                values["apellidos_contacto"] = values["apellidos"]
        return values