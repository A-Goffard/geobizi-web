class Empresa:
    def __init__(self, nombre: str, razon_social: str, nif: str = None, direccion: str = None, provincia: str = None, cp: str = None, sector: str = None, logo: str = None, ubicacion: str = None, nombre_contacto: str = None, email_contacto: str = None, telefono_empresa: str = None, email_empresa: str = None, observaciones: str = None):
        self._nombre = nombre
        self._razon_social = razon_social
        self._nif = nif
        self._direccion = direccion
        self._provincia = provincia
        self._cp = cp
        self._nombre_contacto = nombre_contacto
        self._email_contacto = email_contacto
        self._telefono_empresa = telefono_empresa
        self._email_empresa = email_empresa
        self._observaciones = observaciones
        self._sector = sector
        self._logo = logo
        self._ubicacion = ubicacion
        self._activo = True

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value
        
    @property
    def email_contacto(self):
        return self._email_contacto

    @email_contacto.setter
    def email_contacto(self, value):
        self._email_contacto = value

    @property
    def razon_social(self):
        return self._razon_social

    @razon_social.setter
    def razon_social(self, value):
        self._razon_social = value

    @property
    def nif(self):
        return self._nif
    
    @nif.setter
    def nif(self, value):
        self._nif = value
        
    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @property
    def provincia(self):
        return self._provincia

    @provincia.setter
    def provincia(self, value):
        self._provincia = value

    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, value):
        self._cp = value

    @property
    def nombre_contacto(self):
        return self._nombre_contacto

    @nombre_contacto.setter
    def nombre_contacto(self, value):
        self._nombre_contacto = value

    @property
    def telefono_empresa(self):
        return self._telefono_empresa

    @telefono_empresa.setter
    def telefono_empresa(self, value):
        self._telefono_empresa = value

    @property
    def email_empresa(self):
        return self._email_empresa

    @email_empresa.setter
    def email_empresa(self, value):
        self._email_empresa = value

    @property
    def observaciones(self):
        return self._observaciones

    @observaciones.setter
    def observaciones(self, value):
        self._observaciones = value

    @property
    def sector(self):
        return self._sector
    
    @sector.setter
    def sector(self, value):
        self._sector = value
        
    @property
    def logo(self):
        return self._logo
    
    @logo.setter
    def logo(self, value):
        self._logo = value
        
    @property
    def ubicacion(self):
        return self._ubicacion
    
    @ubicacion.setter
    def ubicacion(self, value):
        self._ubicacion = value
        
    @property
    def activo(self):
        return self._activo
    
    @activo.setter
    def activo(self, value: bool):
        self._activo = value
        
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "razon_social": self._razon_social,
            "nif": self._nif,
            "direccion": self._direccion,
            "provincia": self._provincia,
            "cp": self._cp,
            "nombre_contacto": self._nombre_contacto,
            "email_contacto": self._email_contacto,
            "telefono_empresa": self._telefono_empresa,
            "email_empresa": self._email_empresa,
            "observaciones": self._observaciones,
            "sector": self._sector,
            "logo": self._logo,
            "ubicacion": self._ubicacion,
            "activo": self._activo
        }
