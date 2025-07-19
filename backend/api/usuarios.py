from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from database.database import SessionLocal
from database.models import Usuario as UsuarioModel
from controlador.dominio.usuario import Usuario as UsuarioDominio
from schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioOut
from controlador.validaciones.validador_usuario import validar_usuario_create, validar_usuario_update
from typing import List
from utils.security import hash_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/admin/usuarios", response_model=UsuarioOut)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Comprobamos si el email ya existe
    db_user = db.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    usuario_dominio = UsuarioDominio(
        email=usuario.email, 
        password=usuario.password, 
        id_rol=usuario.id_rol, 
        id_persona=usuario.id_persona
    )
    try:
        # Usamos el validador específico para la creación
        validar_usuario_create(usuario_dominio)
    except ValueError as e:
        print(f"Error de validación al crear usuario: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    nuevo_usuario = UsuarioModel(
        id_persona=usuario_dominio.id_persona,
        id_rol=usuario_dominio.id_rol,
        email=usuario_dominio.email,
        password=hash_password(usuario_dominio.password),
        is_superuser=False,
        activo=1
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.get("/admin/usuarios", response_model=List[UsuarioOut])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).options(selectinload(UsuarioModel.rol)).filter(UsuarioModel.activo == 1).all()

@router.get("/admin/usuarios/inactivos", response_model=List[UsuarioOut])
def listar_usuarios_inactivos(db: Session = Depends(get_db)):
    """Devuelve una lista de usuarios que han sido desactivados."""
    return db.query(UsuarioModel).options(selectinload(UsuarioModel.rol)).filter(UsuarioModel.activo == 0).all()

@router.put("/admin/usuarios/{id_usuario}/reactivar", response_model=UsuarioOut)
def reactivar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    """Reactiva un usuario que estaba inactivo."""
    usuario_db = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == id_usuario).first()
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    usuario_db.activo = 1
    db.commit()
    db.refresh(usuario_db)
    return usuario_db

@router.put("/admin/usuarios/{id_usuario}", response_model=UsuarioOut)
def modificar_usuario(id_usuario: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario_db = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == id_usuario, UsuarioModel.activo == 1).first()
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    usuario_dominio = UsuarioDominio(
        email=usuario.email, 
        password=usuario.password, 
        id_rol=usuario.id_rol, 
        id_persona=usuario.id_persona
    )
    try:
        # Usamos el validador específico para la actualización
        validar_usuario_update(usuario_dominio)
    except ValueError as e:
        print(f"Error de validación al modificar usuario: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    # Actualizamos los datos del usuario en la BD
    usuario_db.id_persona = usuario.id_persona
    usuario_db.id_rol = usuario.id_rol
    usuario_db.email = usuario.email
    # Solo actualizamos la contraseña si se ha proporcionado una nueva
    if usuario.password:
        usuario_db.password = hash_password(usuario.password)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db

@router.delete("/admin/usuarios/{id_usuario}")
def eliminar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario_db = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == id_usuario, UsuarioModel.activo == 1).first()
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario_db.activo = 0
    db.commit()
    return {"msg": "Usuario desactivado"}
