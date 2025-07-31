import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Determinar la ruta de la base de datos según el entorno
def get_database_url():
    # Si hay una variable de entorno DATABASE_URL, úsala
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        print(f"Usando DATABASE_URL desde entorno: {database_url}")
        return database_url
    
    # Si estamos en Docker (detectar por variables o archivos)
    if os.path.exists("/.dockerenv") or os.getenv("DOCKER_CONTAINER"):
        print("Entorno Docker detectado")
        db_path = "/app/database/data/geobizi.db"
        # Crear directorio si no existe
        os.makedirs("/app/database/data", exist_ok=True)
        return f"sqlite:///{db_path}"
    
    # Configuración local (desarrollo)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")
    
    # Crear directorio data si no existe
    os.makedirs(data_dir, exist_ok=True)
    
    db_path = os.path.join(data_dir, "geobizi.db")
    database_url = f"sqlite:///{db_path}"
    
    print(f"Configuración local detectada")
    print(f"Directorio actual: {current_dir}")
    print(f"Directorio de datos: {data_dir}")
    print(f"Ruta de BD: {db_path}")
    print(f"DATABASE_URL: {database_url}")
    
    return database_url

# Configurar la base de datos
DATABASE_URL = get_database_url()

print(f"Usando base de datos: {DATABASE_URL}")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

