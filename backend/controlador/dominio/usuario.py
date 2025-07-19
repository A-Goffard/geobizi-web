class Usuario:
    def __init__(self, email: str, password: str, id_rol: int = None, id_persona: int = None):
        self._email = email
        self._password = password
        self._id_rol = id_rol
        self._id_persona = id_persona
        self._activo = True

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def id_rol(self):
        return self._id_rol

    @id_rol.setter
    def id_rol(self, value):
        self._id_rol = value

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, value):
        self._id_persona = value
        
    @property
    def activo(self):
        return self._activo
    
    @activo.setter
    def activo(self, value: bool):
        self._activo = value

    def to_dict(self):
        return {
            "email": self._email,
            "password": self._password,
            "id_rol": self._id_rol,
            "id_persona": self._id_persona,
            "activo": self._activo
        }
