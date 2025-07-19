# Para ejecutar correctamente este script, usa imports relativos y ejecuta como módulo:
#   python -m database.init_db
from database.database import engine, Base, SessionLocal
from database.models import Actividad, Usuario, Persona, Empresa, Mensaje, Reserva, LogSistema, Rol

def crear_roles_iniciales():
    db = SessionLocal()
    try:
        if db.query(Rol).count() == 0:
            print("Creando roles iniciales...")
            roles = [
                Rol(id_rol=1, nombre="superusuario"),
                Rol(id_rol=2, nombre="empleado"),
                Rol(id_rol=3, nombre="visitante")
            ]
            db.add_all(roles)
            db.commit()
            print("Roles creados.")
    finally:
        db.close()

def init_db():
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas.")
    crear_roles_iniciales()

if __name__ == "__main__":
    init_db()
