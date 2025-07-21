from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class PersonaBase(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    telefono: str
    dni: Optional[str] = None
    direccion: Optional[str] = None
    cp: Optional[str] = None
    poblacion: Optional[str] = None
    pais: Optional[str] = None
    observaciones: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    genero: Optional[str] = None

class PersonaCreate(PersonaBase):
    pass

class PersonaUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    dni: Optional[str] = None
    direccion: Optional[str] = None
    cp: Optional[str] = None
    poblacion: Optional[str] = None
    pais: Optional[str] = None
    observaciones: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    genero: Optional[str] = None

class PersonaOut(PersonaBase):
    id_persona: int
    activo: int

    class Config:
        from_attributes = True
