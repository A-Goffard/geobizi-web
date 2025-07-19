from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.database import SessionLocal
from database.models import Usuario
from typing import Optional # Importa Optional

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/admin/panel")
def admin_panel(email: Optional[str] = None, db: Session = Depends(get_db)):
    if not email:
        # Si no se proporciona email, devuelve una respuesta genérica en lugar de un error
        return {"msg": "Bienvenido al panel de control."}

    user = db.query(Usuario).filter(Usuario.email == email, Usuario.is_superuser == True).first()
    if not user:
        raise HTTPException(status_code=403, detail="Acceso solo para superusuarios")
    return {"msg": "Bienvenido al panel de control, superusuario"}
