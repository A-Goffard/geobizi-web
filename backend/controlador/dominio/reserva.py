from datetime import datetime

class Reserva:
    def __init__(self, id_persona: int, id_actividad: int, numero_personas: int, fecha_reserva: datetime = None, aprobada: bool = False, confirmacion_enviada: bool = False):
        self._id_persona = id_persona
        self._id_actividad = id_actividad
        self._numero_personas = numero_personas
        self._fecha_reserva = fecha_reserva or datetime.now()
        self._aprobada = aprobada
        self._confirmacion_enviada = confirmacion_enviada

    # Getters y setters para todos los atributos
    @property
    def id_persona(self):
        return self._id_persona
    
    @id_persona.setter
    def id_persona(self, value):
        self._id_persona = value
        
    @property
    def id_actividad(self):
        return self._id_actividad

    @id_actividad.setter
    def id_actividad(self, value):
        self._id_actividad = value

    @property
    def numero_personas(self):
        return self._numero_personas

    @numero_personas.setter
    def numero_personas(self, value):
        self._numero_personas = value

    @property
    def fecha_reserva(self):
        return self._fecha_reserva

    @fecha_reserva.setter
    def fecha_reserva(self, value):
        self._fecha_reserva = value

    @property
    def aprobada(self):
        return self._aprobada

    @aprobada.setter
    def aprobada(self, value):
        self._aprobada = value

    @property
    def confirmacion_enviada(self):
        return self._confirmacion_enviada

    @confirmacion_enviada.setter
    def confirmacion_enviada(self, value):
        self._confirmacion_enviada = value

    def to_dict(self):
        return {
            "id_persona": self._id_persona,
            "id_actividad": self._id_actividad,
            "numero_personas": self._numero_personas,
            "fecha_reserva": self._fecha_reserva,
            "aprobada": self._aprobada,
            "confirmacion_enviada": self._confirmacion_enviada,
        }
