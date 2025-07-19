from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ActividadBase(BaseModel):
    nombre: str
    tipo: Optional[str] = None
    lugar: Optional[str] = None
    fecha: Optional[datetime] = None
    hora: Optional[str] = None
    descripcion: Optional[str] = None
    responsable: Optional[str] = None
    duracion: Optional[float] = None
    precio: Optional[float] = None
    coste_economico: Optional[float] = None
    coste_horas: Optional[float] = None
    facturacion: Optional[float] = None
    resultados: Optional[str] = None
    valoracion: Optional[str] = None
    observaciones: Optional[str] = None
    estado: Optional[str] = "pendiente"
    num_participantes: Optional[int] = 0
    categoria: Optional[str] = None
    visible_publico: Optional[bool] = True

class ActividadCreate(BaseModel):
    nombre: str
    tipo: Optional[str] = None
    lugar: Optional[str] = None
    fecha: Optional[datetime] = None
    hora: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = "pendiente"
    categoria: Optional[str] = None
    precio: Optional[float] = None

class ActividadUpdate(BaseModel):
    nombre: Optional[str] = None
    tipo: Optional[str] = None
    lugar: Optional[str] = None
    fecha: Optional[datetime] = None
    hora: Optional[str] = None
    descripcion: Optional[str] = None
    responsable: Optional[str] = None
    duracion: Optional[float] = None
    precio: Optional[float] = None
    coste_economico: Optional[float] = None
    coste_horas: Optional[float] = None
    facturacion: Optional[float] = None
    resultados: Optional[str] = None
    valoracion: Optional[str] = None
    observaciones: Optional[str] = None
    estado: Optional[str] = None
    num_participantes: Optional[int] = None
    categoria: Optional[str] = None
    visible_publico: Optional[bool] = None

class ActividadOut(ActividadBase):
    id_actividad: int
    activo: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
        from_attributes = True
