from datetime import datetime

class LogSistema:
    def __init__(self, usuario_id: int, accion: str, descripcion: str = None, actividad_modificada: str = None, actividad_agregada: str = None, fecha: datetime = None):
        self._usuario_id = usuario_id
        self._accion = accion
        self._descripcion = descripcion
        self._actividad_modificada = actividad_modificada
        self._actividad_agregada = actividad_agregada
        self._fecha = fecha or datetime.now()

    # Getters y setters para todos los atributos
    @property
    def usuario_id(self):
        return self._usuario_id

    @usuario_id.setter
    def usuario_id(self, value):
        self._usuario_id = value
        
    @property
    def accion(self):
        return self._accion

    @accion.setter
    def accion(self, value):
        self._accion = value
        
    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value
        
    @property
    def actividad_modificada(self):
        return self._actividad_modificada

    @actividad_modificada.setter
    def actividad_modificada(self, value):
        self._actividad_modificada = value

    @property
    def actividad_agregada(self):
        return self._actividad_agregada

    @actividad_agregada.setter
    def actividad_agregada(self, value):
        self._actividad_agregada = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    def to_dict(self):
        return {
            "usuario_id": self._usuario_id,
            "accion": self._accion,
            "descripcion": self._descripcion,
            "actividad_modificada": self._actividad_modificada,
            "actividad_agregada": self._actividad_agregada,
            "fecha": self._fecha,
        }
