from pydantic import BaseModel
from typing import Optional
from .persona import PersonaOut

class EmpresaBase(BaseModel):
    id_persona: Optional[int] = None
    nombre: str
    razon_social: str
    nif: Optional[str] = None
    direccion: Optional[str] = None
    provincia: Optional[str] = None
    cp: Optional[str] = None
    sector: Optional[str] = None
    logo: Optional[str] = None
    ubicacion: Optional[str] = None

class EmpresaCreate(EmpresaBase):
    # Hacemos que los campos de dirección sean obligatorios solo en la creación
    nombre: str
    razon_social: str
    direccion: str
    provincia: str
    cp: str

class EmpresaUpdate(BaseModel):
    id_persona: Optional[int] = None
    nombre: Optional[str] = None
    razon_social: Optional[str] = None
    nif: Optional[str] = None
    direccion: Optional[str] = None
    provincia: Optional[str] = None
    cp: Optional[str] = None
    sector: Optional[str] = None
    logo: Optional[str] = None
    ubicacion: Optional[str] = None

class EmpresaOut(EmpresaBase):
    id_empresa: int
    activo: Optional[int] = None
    persona: Optional[PersonaOut] = None

    class Config:
        from_attributes = True
