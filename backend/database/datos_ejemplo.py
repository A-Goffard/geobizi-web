from sqlalchemy.orm import Session
from datetime import datetime, date
import sys
import os

# Agregar el directorio actual al path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Importaciones directas desde el mismo directorio
import database as db_module
import models as models_module
from passlib.context import CryptContext

# Asignar variables para facilitar el uso
SessionLocal = db_module.SessionLocal
engine = db_module.engine
Base = models_module.Base
Actividad = models_module.Actividad
Rol = models_module.Rol
Usuario = models_module.Usuario
Persona = models_module.Persona
Empresa = models_module.Empresa
Mensaje = models_module.Mensaje
Reserva = models_module.Reserva
LogSistema = models_module.LogSistema

# Configuración para el hash de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def recrear_base_datos():
    """Recrear toda la base de datos con la nueva estructura"""
    print("=== RECREANDO BASE DE DATOS ===")
    
    try:
        # Eliminar todas las tablas
        Base.metadata.drop_all(bind=engine)
        print("Tablas eliminadas")
        
        # Crear todas las tablas con la nueva estructura
        Base.metadata.create_all(bind=engine)
        print("Tablas creadas con nueva estructura")
        
        return True
    except Exception as e:
        print(f"Error recreando base de datos: {e}")
        return False

def crear_datos_ejemplo():
    # Verificar que el directorio de datos existe
    if "sqlite" in str(engine.url):
        db_path = str(engine.url).replace("sqlite:///", "")
        db_dir = os.path.dirname(db_path)
        
        if db_dir and not os.path.exists(db_dir):
            print(f"Creando directorio: {db_dir}")
            os.makedirs(db_dir, exist_ok=True)
    
    # Crear todas las tablas
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Verificar si ya existen datos
        if db.query(Persona).first():
            print("Los datos de ejemplo ya existen.")
            return
        
        # 1. Crear Roles
        roles = [
            Rol(nombre="Administrador"),
            Rol(nombre="Gestor"),
            Rol(nombre="Cliente"),
            Rol(nombre="Empresa")
        ]
        db.add_all(roles)
        db.commit()
        print("Roles creados")
        
        # 2. Crear Personas
        personas = [
            Persona(
                nombre="Ana", apellido="García López",
                email="ana.garcia@email.com", telefono="666111222",
                dni="12345678A", direccion="Calle Mayor 123",
                cp="48001", poblacion="Bilbao", pais="España",
                fecha_nacimiento=date(1985, 3, 15), genero="F"
            ),
            Persona(
                nombre="Carlos", apellido="Martínez Ruiz",
                email="carlos.martinez@email.com", telefono="666333444",
                dni="87654321B", direccion="Avenida Libertad 456",
                cp="20004", poblacion="San Sebastián", pais="España",
                fecha_nacimiento=date(1978, 7, 22), genero="M"
            ),
            Persona(
                nombre="María", apellido="López Fernández",
                email="maria.lopez@email.com", telefono="666555777",
                dni="11223344C", direccion="Plaza del Carmen 789",
                cp="01005", poblacion="Vitoria", pais="España",
                fecha_nacimiento=date(1992, 11, 8), genero="F"
            ),
            Persona(
                nombre="Javier", apellido="Rodríguez Sánchez",
                email="javier.rodriguez@email.com", telefono="666888999",
                dni="55667788D", direccion="Calle Urquijo 321",
                cp="48013", poblacion="Bilbao", pais="España",
                fecha_nacimiento=date(1989, 4, 12), genero="M"
            ),
            Persona(
                nombre="Laura", apellido="Pérez Vázquez",
                email="laura.perez@email.com", telefono="666222333",
                dni="99887766E", direccion="Gran Vía 654",
                cp="48011", poblacion="Bilbao", pais="España",
                fecha_nacimiento=date(1995, 9, 3), genero="F"
            )
        ]
        db.add_all(personas)
        db.commit()
        print("Personas creadas")
        
        # 3. Crear Usuarios
        usuarios = [
            Usuario(
                id_persona=1, id_rol=1,
                email="admin@geobizi.com",
                password=hash_password("admin123"),
                is_superuser=True
            ),
            Usuario(
                id_persona=2, id_rol=2,
                email="gestor@geobizi.com",
                password=hash_password("gestor123")
            ),
            Usuario(
                id_persona=3, id_rol=3,
                email="maria.lopez@email.com",
                password=hash_password("cliente123")
            ),
            Usuario(
                id_persona=4, id_rol=3,
                email="javier.rodriguez@email.com",
                password=hash_password("cliente123")
            )
        ]
        db.add_all(usuarios)
        db.commit()
        print("Usuarios creados")
        
        # 4. Crear Empresas
        empresas = [
            Empresa(
                nombre="EcoTurismo Euskadi",
                razon_social="EcoTurismo Euskadi S.L.",
                nif="B48123456", direccion="Polígono Industrial 123",
                provincia="Bizkaia", cp="48940",
                nombre_contacto="Laura Pérez",
                email_contacto="laura.perez@email.com",
                telefono_empresa="944123456",
                email_empresa="info@ecoturismo.com",
                sector="Turismo Sostenible", ubicacion="Leioa"
            ),
            Empresa(
                nombre="Aventuras Cantábricas",
                razon_social="Aventuras Cantábricas S.A.",
                nif="A39654321", direccion="Puerto Deportivo 45",
                provincia="Cantabria", cp="39004",
                nombre_contacto="Roberto Silva",
                email_contacto="roberto.silva@email.com",
                telefono_empresa="942987654",
                email_empresa="contacto@aventurascantabricas.com",
                sector="Deportes de Aventura", ubicacion="Santander"
            )
        ]
        db.add_all(empresas)
        db.commit()
        print("Empresas creadas")
        
        # 5. Crear Actividades
        actividades = [
            Actividad(
                nombre="Senderismo Urkiola",
                tipo="Senderismo", lugar="Parque Natural de Urkiola",
                fecha=datetime(2024, 6, 15, 9, 0),
                hora="09:00", descripcion="Ruta circular por el Parque Natural de Urkiola",
                responsable="Ana García", duracion=4.5, precio=25.0,
                coste_economico=15.0, coste_horas=8.0, estado="confirmada",
                num_participantes=12, categoria="Naturaleza", visible_publico=True
            ),
            Actividad(
                nombre="Kayak en Urdaibai",
                tipo="Deportes Acuáticos", lugar="Reserva de Urdaibai",
                fecha=datetime(2024, 6, 20, 10, 30),
                hora="10:30", descripcion="Excursión en kayak por la ría de Urdaibai",
                responsable="Carlos Martínez", duracion=3.0, precio=35.0,
                coste_economico=20.0, coste_horas=6.0, estado="pendiente",
                num_participantes=8, categoria="Deportes", visible_publico=True
            ),
            Actividad(
                nombre="Visita Guggenheim",
                tipo="Cultural", lugar="Museo Guggenheim Bilbao",
                fecha=datetime(2024, 6, 25, 11, 0),
                hora="11:00", descripcion="Visita guiada al Museo Guggenheim",
                responsable="María López", duracion=2.0, precio=18.0,
                coste_economico=12.0, coste_horas=4.0, estado="confirmada",
                num_participantes=15, categoria="Cultura", visible_publico=True
            ),
            Actividad(
                nombre="Escalada en Peñas de Aia",
                tipo="Escalada", lugar="Peñas de Aia",
                fecha=datetime(2024, 7, 5, 8, 0),
                hora="08:00", descripcion="Jornada de escalada en roca",
                responsable="Javier Rodríguez", duracion=6.0, precio=45.0,
                coste_economico=25.0, coste_horas=10.0, estado="pendiente",
                num_participantes=6, categoria="Deportes", visible_publico=True
            ),
            Actividad(
                nombre="Cata de Txakoli",
                tipo="Gastronómico", lugar="Bodega Txomin Etxaniz",
                fecha=datetime(2024, 7, 10, 17, 0),
                hora="17:00", descripcion="Cata de txakoli con maridaje",
                responsable="Ana García", duracion=2.5, precio=30.0,
                coste_economico=18.0, coste_horas=5.0, estado="confirmada",
                num_participantes=20, categoria="Gastronomía", visible_publico=True
            )
        ]
        db.add_all(actividades)
        db.commit()
        print("Actividades creadas")
        
        # 6. Crear Reservas (ACTUALIZADO con nuevos campos)
        reservas = [
            Reserva(
                id_persona=3, id_actividad=1, numero_personas=2,
                fecha_reserva=datetime(2024, 5, 10, 14, 30),
                aprobada=True, confirmacion_enviada=True,
                mensaje="¿Incluye transporte desde Bilbao?",
                forma_pago="tarjeta"
            ),
            Reserva(
                id_persona=4, id_actividad=1, numero_personas=1,
                fecha_reserva=datetime(2024, 5, 12, 16, 45),
                aprobada=True, confirmacion_enviada=True,
                mensaje="Tengo experiencia en senderismo",
                forma_pago="transferencia"
            ),
            Reserva(
                id_persona=3, id_actividad=2, numero_personas=2,
                fecha_reserva=datetime(2024, 5, 15, 10, 20),
                aprobada=False, confirmacion_enviada=False,
                mensaje="¿Qué incluye el equipo de kayak?",
                forma_pago="paypal"
            ),
            Reserva(
                id_persona=5, id_actividad=3, numero_personas=4,
                fecha_reserva=datetime(2024, 5, 18, 12, 0),
                aprobada=True, confirmacion_enviada=True,
                mensaje="Reserva para grupo empresarial",
                forma_pago="transferencia"
            ),
            Reserva(
                id_persona=4, id_actividad=5, numero_personas=3,
                fecha_reserva=datetime(2024, 5, 20, 18, 30),
                aprobada=True, confirmacion_enviada=False,
                mensaje="¿Hay descuentos para grupos?",
                forma_pago="tarjeta"
            )
        ]
        db.add_all(reservas)
        db.commit()
        print("Reservas creadas")
        
        # 7. Crear Mensajes
        mensajes = [
            Mensaje(
                id_persona=3, contenido="¿Hay descuentos para grupos?",
                fecha_envio=datetime(2024, 5, 8, 15, 30)
            ),
            Mensaje(
                id_persona=4, contenido="¿Incluye el equipo de escalada?",
                fecha_envio=datetime(2024, 5, 12, 11, 15)
            ),
            Mensaje(
                id_persona=5, contenido="Necesito factura para la empresa",
                fecha_envio=datetime(2024, 5, 16, 9, 45)
            )
        ]
        db.add_all(mensajes)
        db.commit()
        print("Mensajes creados")
        
        # 8. Crear Logs del Sistema
        logs = [
            LogSistema(
                usuario_id=1, accion="CREAR_ACTIVIDAD",
                descripcion="Nueva actividad de senderismo creada",
                actividad_agregada="Senderismo Urkiola",
                fecha=datetime(2024, 5, 1, 9, 0)
            ),
            LogSistema(
                usuario_id=2, accion="APROBAR_RESERVA",
                descripcion="Reserva aprobada para senderismo",
                fecha=datetime(2024, 5, 11, 14, 30)
            ),
            LogSistema(
                usuario_id=1, accion="MODIFICAR_ACTIVIDAD",
                descripcion="Precio actualizado para kayak",
                actividad_modificada="Kayak en Urdaibai",
                fecha=datetime(2024, 5, 14, 10, 15)
            ),
            LogSistema(
                usuario_id=2, accion="CREAR_USUARIO",
                descripcion="Nuevo usuario cliente registrado",
                fecha=datetime(2024, 5, 16, 16, 20)
            )
        ]
        db.add_all(logs)
        db.commit()
        print("Logs del sistema creados")
        
        print("¡Todos los datos de ejemplo han sido creados exitosamente!")
        
    except Exception as e:
        print(f"Error al crear datos de ejemplo: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

def verificar_datos():
    """Función para verificar que los datos se crearon correctamente"""
    db = SessionLocal()
    
    try:
        print("\n=== INFORMACIÓN DE BASE DE DATOS ===")
        print(f"Archivo de base de datos: {engine.url}")
        
        # Verificar si el archivo existe y su ubicación
        import os
        if "sqlite" in str(engine.url):
            db_path = str(engine.url).replace("sqlite:///", "")
            db_full_path = os.path.abspath(db_path)
            print(f"Ubicación completa: {db_full_path}")
            print(f"¿Archivo existe?: {os.path.exists(db_full_path)}")
            if os.path.exists(db_full_path):
                size = os.path.getsize(db_full_path)
                print(f"Tamaño del archivo: {size} bytes")
        
        print("\n=== VERIFICACIÓN DE DATOS ===")
        
        # Verificar cada tabla
        personas_count = db.query(Persona).count()
        print(f"Personas: {personas_count}")
        
        roles_count = db.query(Rol).count()
        print(f"Roles: {roles_count}")
        
        usuarios_count = db.query(Usuario).count()
        print(f"Usuarios: {usuarios_count}")
        
        empresas_count = db.query(Empresa).count()
        print(f"Empresas: {empresas_count}")
        
        actividades_count = db.query(Actividad).count()
        print(f"Actividades: {actividades_count}")
        
        reservas_count = db.query(Reserva).count()
        print(f"Reservas: {reservas_count}")
        
        mensajes_count = db.query(Mensaje).count()
        print(f"Mensajes: {mensajes_count}")
        
        logs_count = db.query(LogSistema).count()
        print(f"Logs: {logs_count}")
        
        print("\n=== DATOS DE MUESTRA ===")
        
        # Mostrar algunas actividades
        actividades = db.query(Actividad).filter(Actividad.activo == 1).all()
        print(f"\nActividades activas ({len(actividades)}):")
        for act in actividades[:3]:
            print(f"  - {act.nombre} (ID: {act.id_actividad}, Estado: {act.estado})")
        
        # Mostrar algunos usuarios
        usuarios = db.query(Usuario).filter(Usuario.activo == 1).all()
        print(f"\nUsuarios activos ({len(usuarios)}):")
        for user in usuarios:
            print(f"  - {user.email} (ID: {user.id_usuario})")
            
        # Verificar filtros de activo
        actividades_inactivas = db.query(Actividad).filter(Actividad.activo == 0).count()
        print(f"\nActividades inactivas: {actividades_inactivas}")
        
        print("\n=== INFORMACIÓN ADICIONAL ===")
        print("Para usar estos datos en Docker, asegúrate de que:")
        print("1. Docker monte el mismo directorio donde está geobizi.db")
        print("2. La configuración de DATABASE_URL en Docker apunte al mismo archivo")
        print("3. No hay variables de entorno que cambien la configuración de BD")
        
    except Exception as e:
        print(f"Error al verificar datos: {e}")
    finally:
        db.close()

def crear_datos_en_docker():
    """Función específica para crear datos cuando se ejecuta desde Docker"""
    print("\n=== MODO DOCKER DETECTADO ===")
    print("Verificando configuración de base de datos para Docker...")
    
    # Aquí puedes agregar lógica específica para Docker
    # Por ejemplo, verificar variables de entorno
    import os
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        print(f"DATABASE_URL desde entorno: {database_url}")
    else:
        print("No se encontró DATABASE_URL en variables de entorno")
    
    # Ejecutar creación normal
    crear_datos_ejemplo()

def ejecutar_en_docker():
    """Función para ejecutar los datos de ejemplo desde Docker"""
    print("\n=== EJECUTANDO DESDE DOCKER ===")
    print("Este comando creará datos de ejemplo en el contenedor Docker")
    
    # Verificar variables de entorno
    import os
    print(f"DATABASE_URL: {os.getenv('DATABASE_URL', 'No configurada')}")
    print(f"Directorio actual: {os.getcwd()}")
    
    # Asegurar que el directorio de datos existe en Docker
    data_dir = "/app/database/data"
    os.makedirs(data_dir, exist_ok=True)
    print(f"Directorio de datos Docker: {data_dir}")
    
    crear_datos_ejemplo()
    verificar_datos()

if __name__ == "__main__":
    import sys
    
    print("=== INFORMACIÓN DEL ENTORNO ===")
    print(f"Python executable: {sys.executable}")
    print(f"Directorio actual: {os.getcwd()}")
    print(f"DATABASE_URL env: {os.getenv('DATABASE_URL', 'No configurada')}")
    print(f"¿Docker detectado?: {os.path.exists('/.dockerenv') or os.getenv('DOCKER_CONTAINER')}")
    
    # Agregar opción para recrear BD
    if len(sys.argv) > 1 and sys.argv[1] == 'recrear':
        print("RECREANDO BASE DE DATOS...")
        if recrear_base_datos():
            crear_datos_ejemplo()
        verificar_datos()
    # Verificar si se ejecuta con argumento 'docker'
    elif len(sys.argv) > 1 and sys.argv[1] == 'docker':
        ejecutar_en_docker()
    # Detectar si estamos en Docker por variables de entorno  
    elif os.path.exists("/.dockerenv") or os.getenv("DOCKER_CONTAINER") or os.getenv("DATABASE_URL"):
        crear_datos_en_docker()
    else:
        crear_datos_ejemplo()
    
    verificar_datos()


