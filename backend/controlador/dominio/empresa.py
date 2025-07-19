class Empresa:
    def __init__(self, nombre: str, razon_social: str, id_persona: int = None, nif: str = None, direccion: str = None, provincia: str = None, cp: str = None, sector: str = None, logo: str = None, ubicacion: str = None):
        self._nombre = nombre
        self._id_persona = id_persona
        self._razon_social = razon_social
        self._nif = nif
        self._direccion = direccion
        self._provincia = provincia
        self._cp = cp
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
    def id_persona(self):
        return self._id_persona
    
    @id_persona.setter
    def id_persona(self, value):
        self._id_persona = value
        
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
            "id_persona": self._id_persona,
            "razon_social": self._razon_social,
            "nif": self._nif,
            "direccion": self._direccion,
            "provincia": self._provincia,
            "cp": self._cp,
            "sector": self._sector,
            "logo": self._logo,
            "ubicacion": self._ubicacion,
            "activo": self._activo
        }
