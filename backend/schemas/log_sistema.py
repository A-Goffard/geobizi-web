from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LogSistemaBase(BaseModel):
    usuario_id: int
    accion: str
    descripcion: Optional[str] = None
    actividad_modificada: Optional[str] = None
    actividad_agregada: Optional[str] = None

class LogSistemaCreate(LogSistemaBase):
    pass

class LogSistemaOut(LogSistemaBase):
    id_log_sistema: int
    fecha: datetime

    class Config:
        from_attributes = True
