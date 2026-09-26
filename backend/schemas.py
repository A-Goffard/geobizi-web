from pydantic import BaseModel, EmailStr
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