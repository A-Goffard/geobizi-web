from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .persona import PersonaOut
from .actividad import ActividadOut

class ReservaBase(BaseModel):
    id_persona: int
    id_actividad: int
    numero_personas: int

class ReservaCreate(ReservaBase):
    pass

class ReservaUpdate(BaseModel):
    id_persona: Optional[int] = None
    id_actividad: Optional[int] = None
    numero_personas: Optional[int] = None
    aprobada: Optional[bool] = None
    confirmacion_enviada: Optional[bool] = None

class ReservaOut(ReservaBase):
    id_reserva: int
    fecha_reserva: datetime
    aprobada: bool
    confirmacion_enviada: bool
    persona: Optional[PersonaOut] = None
    actividad: Optional[ActividadOut] = None

    class Config:
        from_attributes = True
