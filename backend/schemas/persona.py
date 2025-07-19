from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PersonaBase(BaseModel):
    nombre: str
    apellido: Optional[str] = None
    email: str
    telefono: Optional[str] = None
    dni: Optional[str] = None
    direccion: Optional[str] = None
    cp: Optional[str] = None
    poblacion: Optional[str] = None
    pais: Optional[str] = None
    observaciones: Optional[str] = None
    fecha_nacimiento: Optional[datetime] = None
    genero: Optional[str] = None

class PersonaCreate(PersonaBase):
    pass

class PersonaUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    dni: Optional[str] = None
    direccion: Optional[str] = None
    cp: Optional[str] = None
    poblacion: Optional[str] = None
    pais: Optional[str] = None
    observaciones: Optional[str] = None
    fecha_nacimiento: Optional[datetime] = None
    genero: Optional[str] = None

class PersonaOut(PersonaBase):
    id_persona: int
    activo: Optional[int] = None

    class Config:
        from_attributes = True
