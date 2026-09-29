from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Optional

# ==============================================================================
# 1. ASISTENTE INDIVIDUAL
# ==============================================================================
class ParticipanteSchema(BaseModel):
    nombre: str
    apellidos: str
    edad: int


# ==============================================================================
# 2. SOLICITUD DE RESERVA CONFIRMADA
# ==============================================================================
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

    @model_validator(mode="before")
    @classmethod
    def sincronizar_num_personas(cls, data):
        if isinstance(data, dict):
            # Si vienen participantes en el array, aseguramos que num_personas sea exacto
            participantes = data.get("participantes")
            if participantes and isinstance(participantes, list) and len(participantes) > 0:
                data["num_personas"] = len(participantes)
        return data


# ==============================================================================
# 3. SOLICITUD DE LISTA DE ESPERA
# ==============================================================================
class ListaEsperaCreate(BaseModel):
    actividad_id: int
    nombre_contacto: Optional[str] = None
    nombre: Optional[str] = None
    apellidos_contacto: Optional[str] = None
    apellidos: Optional[str] = None
    email: EmailStr
    phone: str
    num_personas: int = 1
    permiso_fotos: bool = False
    observaciones: Optional[str] = None
    participantes: List[ParticipanteSchema] = []

    @model_validator(mode="before")
    @classmethod
    def normalizar_y_sincronizar(cls, data):
        if isinstance(data, dict):
            # Aceptar indistintamente 'nombre' o 'nombre_contacto'
            if "nombre" in data and not data.get("nombre_contacto"):
                data["nombre_contacto"] = data["nombre"]
            if "apellidos" in data and not data.get("apellidos_contacto"):
                data["apellidos_contacto"] = data["apellidos"]

            # Si mandaron participantes, las plazas solicitadas son exactamente la cantidad de asistentes
            participantes = data.get("participantes")
            if participantes and isinstance(participantes, list) and len(participantes) > 0:
                data["num_personas"] = len(participantes)
        return data


# ==============================================================================
# 4. MODIFICACIÓN DE RESERVA EXISTENTE
# ==============================================================================
class ActualizarReservaRequest(BaseModel):
    nombre_contacto: Optional[str] = None
    apellidos_contacto: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    num_personas: Optional[int] = None
    observaciones: Optional[str] = None
    participantes: List[ParticipanteSchema] = []

    @model_validator(mode="before")
    @classmethod
    def sincronizar_modificacion(cls, data):
        if isinstance(data, dict):
            participantes = data.get("participantes")
            if participantes and isinstance(participantes, list) and len(participantes) > 0:
                data["num_personas"] = len(participantes)
        return data