from pydantic import BaseModel, field_validator
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
    nombre_contacto: Optional[str] = None
    telefono_empresa: Optional[str] = None
    email_empresa: Optional[str] = None
    observaciones: Optional[str] = None
    sector: Optional[str] = None
    logo: Optional[str] = None
    ubicacion: Optional[str] = None

    @field_validator('nif')
    @classmethod
    def nif_to_uppercase(cls, v: str) -> str:
        if v:
            return v.upper()
        return v

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
    nombre_contacto: Optional[str] = None
    telefono_empresa: Optional[str] = None
    email_empresa: Optional[str] = None
    observaciones: Optional[str] = None
    sector: Optional[str] = None
    logo: Optional[str] = None
    ubicacion: Optional[str] = None

class EmpresaOut(EmpresaBase):
    id_empresa: int
    activo: Optional[int] = None
    persona: Optional[PersonaOut] = None

    class Config:
        from_attributes = True
