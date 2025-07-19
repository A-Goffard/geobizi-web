from datetime import datetime

class Actividad:
    def __init__(self, nombre: str, tipo: str = None, lugar: str = None, fecha: datetime = None, hora: str = None, descripcion: str = None, responsable: str = None, duracion: float = None, precio: float = None, coste_economico: float = None, coste_horas: float = None, facturacion: float = None, resultados: str = None, valoracion: str = None, observaciones: str = None, estado: str = "pendiente", num_participantes: int = 0, categoria: str = None, visible_publico: bool = True):
        self._nombre = nombre
        self._tipo = tipo
        self._lugar = lugar
        self._fecha = fecha
        self._hora = hora
        self._descripcion = descripcion
        self._responsable = responsable
        self._duracion = duracion
        self._precio = precio
        self._coste_economico = coste_economico
        self._coste_horas = coste_horas
        self._facturacion = facturacion
        self._resultados = resultados
        self._valoracion = valoracion
        self._observaciones = observaciones
        self._estado = estado
        self._num_participantes = num_participantes
        self._categoria = categoria
        self._visible_publico = visible_publico
        self._activo = True

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def lugar(self):
        return self._lugar

    @lugar.setter
    def lugar(self, value):
        self._lugar = value

    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self, value: datetime):
        self._fecha = value
    
    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, value):
        self._hora = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value
        
    @property
    def responsable(self):
        return self._responsable

    @responsable.setter
    def responsable(self, value):
        self._responsable = value
    
    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, value):
        self._duracion = value
        
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value

    @property
    def coste_economico(self):
        return self._coste_economico

    @coste_economico.setter
    def coste_economico(self, value):
        self._coste_economico = value
        
    @property
    def coste_horas(self):
        return self._coste_horas

    @coste_horas.setter
    def coste_horas(self, value):
        self._coste_horas = value

    @property
    def facturacion(self):
        return self._facturacion

    @facturacion.setter
    def facturacion(self, value):
        self._facturacion = value

    @property
    def resultados(self):
        return self._resultados

    @resultados.setter
    def resultados(self, value):
        self._resultados = value

    @property
    def valoracion(self):
        return self._valoracion

    @valoracion.setter
    def valoracion(self, value):
        self._valoracion = value

    @property
    def observaciones(self):
        return self._observaciones

    @observaciones.setter
    def observaciones(self, value):
        self._observaciones = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value

    @property
    def num_participantes(self):
        return self._num_participantes

    @num_participantes.setter
    def num_participantes(self, value):
        self._num_participantes = value

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        self._categoria = value

    @property
    def visible_publico(self):
        return self._visible_publico

    @visible_publico.setter
    def visible_publico(self, value):
        self._visible_publico = value
        
    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, value):
        self._activo = value

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "tipo": self._tipo,
            "lugar": self._lugar,
            "fecha": self._fecha,
            "hora": self._hora,
            "descripcion": self._descripcion,
            "responsable": self._responsable,
            "duracion": self._duracion,
            "precio": self._precio,
            "coste_economico": self._coste_economico,
            "coste_horas": self._coste_horas,
            "facturacion": self._facturacion,
            "resultados": self._resultados,
            "valoracion": self._valoracion,
            "observaciones": self._observaciones,
            "estado": self._estado,
            "num_participantes": self._num_participantes,
            "categoria": self._categoria,
            "visible_publico": self._visible_publico,
            "activo": self._activo,
        }
