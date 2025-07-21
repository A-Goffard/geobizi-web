from datetime import datetime

class Persona:
    def __init__(self, nombre: str, apellido: str, email: str, telefono: str, dni: str = None, direccion: str = None, cp: str = None, poblacion: str = None, pais: str = None, observaciones: str = None, fecha_nacimiento: datetime = None, genero: str = None):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._dni = dni
        self._direccion = direccion
        self._cp = cp
        self._poblacion = poblacion
        self._pais = pais
        self._observaciones = observaciones
        self._fecha_nacimiento = fecha_nacimiento
        self._genero = genero
        self._activo = True

    # Getters y Setters (ejemplo para nombre, se aplica a todos)
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value

    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, value):
        self._dni = value   
        
    @property
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self, value):
        self._direccion = value
        
    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, value):
        self._cp = value

    @property
    def poblacion(self):
        return self._poblacion
    
    @poblacion.setter
    def poblacion(self, value):
        self._poblacion = value
        
    @property
    def pais(self):
        return self._pais
    
    @pais.setter
    def pais(self, value):
        self._pais = value
        
    @property
    def observaciones(self):
        return self._observaciones
    
    @observaciones.setter
    def observaciones(self, value):
        self._observaciones = value
        
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        if isinstance(value, datetime):
            self._fecha_nacimiento = value
        else:
            raise ValueError("fecha_nacimiento debe ser una instancia de datetime")
        
    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, value):
        self._genero = value
        
    @property
    def activo(self):
        return self._activo
    
    @activo.setter
    def activo(self, value: bool):
        self._activo = value

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "dni": self._dni,
            "direccion": self._direccion,
            "cp": self._cp,
            "poblacion": self._poblacion,
            "pais": self._pais,
            "observaciones": self._observaciones,
            "fecha_nacimiento": self._fecha_nacimiento,
            "genero": self._genero,
            "activo": self._activo
        }
