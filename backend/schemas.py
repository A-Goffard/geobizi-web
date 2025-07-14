from pydantic import BaseModel
from datetime import datetime

# Esquema para Actividad
class ActividadBase(BaseModel):
    nombre: str
    descripcion: str | None = None
    fecha: datetime

class ActividadCreate(ActividadBase):
    pass

class Actividad(ActividadBase):
    id: int

    class Config:
        orm_mode = True

# Esquema para Usuario
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
