from pydantic import BaseModel
from typing import Optional
from .rol import RolOut

class UsuarioBase(BaseModel):
    id_persona: Optional[int] = None
    id_rol: Optional[int] = None
    email: str

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioUpdate(UsuarioBase):
    password: Optional[str] = None

class UsuarioOut(BaseModel):
    id_usuario: int
    id_persona: Optional[int] = None
    email: str
    is_superuser: Optional[bool] = None
    activo: Optional[int] = None
    rol: Optional[RolOut] = None

    class Config:
        from_attributes = True
