from .database import engine, Base
from .models import Actividad, User

def init_db():
    print("Creando tablas en la base de datos...")
    # create_all no recrea las tablas si ya existen
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas.")

if __name__ == "__main__":
    init_db()
