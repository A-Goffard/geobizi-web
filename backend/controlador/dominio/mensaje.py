from datetime import datetime

class Mensaje:
    def __init__(self, id_persona: int, contenido: str, fecha_envio: datetime = None):
        self._id_persona = id_persona
        self._contenido = contenido
        self._fecha_envio = fecha_envio or datetime.now()

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, value):
        self._id_persona = value

    @property
    def contenido(self):
        return self._contenido

    @contenido.setter
    def contenido(self, value):
        self._contenido = value

    @property
    def fecha_envio(self):
        return self._fecha_envio

    def to_dict(self):
        return {
            "id_persona": self.id_persona,
            "contenido": self.contenido,
            "fecha_envio": self.fecha_envio,
        }
