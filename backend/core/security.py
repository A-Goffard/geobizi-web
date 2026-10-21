import os
import hmac
import hashlib
import time
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def generar_token_admin() -> str:
    """Genera un token firmado con HMAC y marca de tiempo (válido por 7 días)."""
    secret = os.getenv("ADMIN_TOKEN_SECRET", "geobizi_fallback_secret_key").encode()
    expira_en = int(time.time()) + (7 * 24 * 3600)
    mensaje = f"admin:{expira_en}".encode()
    firma = hmac.new(secret, mensaje, hashlib.sha256).hexdigest()
    return f"{expira_en}:{firma}"

def verificar_token_admin(credentials: HTTPAuthorizationCredentials = Security(security)) -> bool:
    """Dependencia para proteger endpoints de administración."""
    token = credentials.credentials
    secret = os.getenv("ADMIN_TOKEN_SECRET", "geobizi_fallback_secret_key").encode()
    
    try:
        expira_en_str, firma = token.split(":")
        expira_en = int(expira_en_str)
        
        if time.time() > expira_en:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="La sesión de administración ha caducado. Vuelve a iniciar sesión."
            )
            
        mensaje = f"admin:{expira_en}".encode()
        firma_esperada = hmac.new(secret, mensaje, hashlib.sha256).hexdigest()
        
        if not hmac.compare_digest(firma, firma_esperada):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token de administración inválido."
            )
        return True
    except (ValueError, AttributeError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Formato de token incorrecto."
        )