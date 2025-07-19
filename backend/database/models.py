from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Actividad(Base):
    __tablename__ = "actividades"

    id_actividad = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tipo = Column(String, index=True)
    nombre = Column(String, index=True)
    lugar = Column(String)
    fecha = Column(DateTime)
    hora = Column(String)
    descripcion = Column(String)
    responsable = Column(String)
    duracion = Column(Float)
    precio = Column(Float) # Precio por persona para el cliente
    coste_economico = Column(Float) # Gasto interno de la actividad
    coste_horas = Column(Float)
    facturacion = Column(Float)
    resultados = Column(String)
    valoracion = Column(String)
    observaciones = Column(String)
    estado = Column(String, default="pendiente") # ejemplo de estado
    num_participantes = Column(Integer, default=0)
    categoria = Column(String)
    visible_publico = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    activo = Column(Integer, default=1)

    reservas = relationship("Reserva", back_populates="actividad")

class Rol(Base):
    __tablename__ = "roles"
    id_rol = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)

    usuarios = relationship("Usuario", back_populates="rol")

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_persona = Column(Integer, ForeignKey("personas.id_persona"), index=True, nullable=True)
    id_rol = Column(Integer, ForeignKey("roles.id_rol"))
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_superuser = Column(Boolean, default=False)
    activo = Column(Integer, default=1)

    rol = relationship("Rol", back_populates="usuarios")
    persona = relationship("Persona", back_populates="usuarios")
    logs = relationship("LogSistema", back_populates="usuario")

class Persona(Base):
    __tablename__ = "personas"

    id_persona = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefono = Column(String)
    dni = Column(String, unique=True)
    direccion = Column(String)
    cp = Column(String)
    poblacion = Column(String)
    pais = Column(String)
    observaciones = Column(String)
    fecha_nacimiento = Column(DateTime)
    genero = Column(String)
    activo = Column(Integer, default=1)

    usuarios = relationship("Usuario", back_populates="persona")
    empresas = relationship("Empresa", back_populates="persona")
    mensajes = relationship("Mensaje", back_populates="persona")
    reservas = relationship("Reserva", back_populates="persona")

class Empresa(Base):
    __tablename__ = "empresas"

    id_empresa = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_persona = Column(Integer, ForeignKey("personas.id_persona"), index=True)
    nombre = Column(String, index=True)
    razon_social = Column(String)
    nif = Column(String, unique=True)
    direccion = Column(String)
    provincia = Column(String)
    cp = Column(String)
    sector = Column(String)
    logo = Column(String)
    ubicacion = Column(String)
    activo = Column(Integer, default=1)

    persona = relationship("Persona", back_populates="empresas")

class Mensaje(Base):
    __tablename__ = "mensajes"
    id_mensaje = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_persona = Column(Integer, ForeignKey("personas.id_persona"), index=True)
    contenido = Column(String)
    fecha_envio = Column(DateTime)

    persona = relationship("Persona", back_populates="mensajes")

class Reserva(Base):
    __tablename__ = "reservas"
    id_reserva = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_persona = Column(Integer, ForeignKey("personas.id_persona"), index=True)
    id_actividad = Column(Integer, ForeignKey("actividades.id_actividad"), index=True)
    fecha_reserva = Column(DateTime)
    aprobada = Column(Boolean, default=False)
    numero_personas = Column(Integer)
    confirmacion_enviada = Column(Boolean, default=False)

    persona = relationship("Persona", back_populates="reservas")
    actividad = relationship("Actividad", back_populates="reservas")

class LogSistema(Base):
    __tablename__ = "logs_sistema"
    id_log_sistema = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fecha = Column(DateTime)
    usuario_id = Column(Integer, ForeignKey("usuarios.id_usuario"), index=True)
    accion = Column(String)
    descripcion = Column(String)
    actividad_modificada = Column(String)
    actividad_agregada = Column(String)

    usuario = relationship("Usuario", back_populates="logs")

# Revisa que el campo 'activo' esté en todas las clases y que los ids sean autoincrementales.
