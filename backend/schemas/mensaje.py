from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MensajeBase(BaseModel):
    id_persona: int
    contenido: str

class MensajeCreate(MensajeBase):
    pass

class MensajeOut(MensajeBase):
    id_mensaje: int
    fecha_envio: datetime
    activo: Optional[int] = None

    class Config:
        from_attributes = True
