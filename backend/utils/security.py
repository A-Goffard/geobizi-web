from passlib.context import CryptContext

# Creamos un contexto para el hasheo de contraseñas, usando bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """Verifica una contraseña plana contra una hasheada."""
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    """Hashea una contraseña."""
    return pwd_context.hash(password)
