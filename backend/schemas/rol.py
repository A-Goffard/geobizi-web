from pydantic import BaseModel
from typing import Optional

class RolBase(BaseModel):
    nombre: str

class RolCreate(RolBase):
    pass

class RolOut(RolBase):
    id_rol: int
    activo: Optional[int] = None

    class Config:
        from_attributes = True
