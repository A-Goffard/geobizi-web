from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from database.database import SessionLocal
from database.models import Empresa as EmpresaModel
from schemas.empresa import EmpresaCreate, EmpresaUpdate, EmpresaOut
from controlador.validaciones.validador_empresa import validar_empresa_create, validar_empresa_update
from controlador.gestores.empresa_gestor import EmpresaGestor
from typing import List
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()
empresa_gestor = EmpresaGestor()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/admin/empresas", response_model=EmpresaOut)
def crear_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    try:
        validar_empresa_create(empresa)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    db_empresa = db.query(EmpresaModel).filter(EmpresaModel.nif == empresa.nif).first()
    if db_empresa:
        raise HTTPException(status_code=400, detail="El NIF ya está registrado para otra empresa.")
    
    return empresa_gestor.crear(db, empresa)

@router.get("/api/admin/empresas", response_model=List[EmpresaOut])
def listar_empresas(db: Session = Depends(get_db)):
    return db.query(EmpresaModel).options(selectinload(EmpresaModel.persona)).filter(EmpresaModel.activo == 1).all()

@router.get("/api/admin/empresas/inactivas", response_model=List[EmpresaOut])
def listar_empresas_inactivas(db: Session = Depends(get_db)):
    return db.query(EmpresaModel).options(selectinload(EmpresaModel.persona)).filter(EmpresaModel.activo == 0).all()

@router.put("/api/admin/empresas/{id_empresa}", response_model=EmpresaOut)
def modificar_empresa(id_empresa: int, empresa: EmpresaUpdate, db: Session = Depends(get_db)):
    empresa_db = db.query(EmpresaModel).filter(EmpresaModel.id_empresa == id_empresa, EmpresaModel.activo == 1).first()
    if not empresa_db:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    
    try:
        validar_empresa_update(empresa)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return empresa_gestor.actualizar(db, id_empresa, empresa)

@router.delete("/api/admin/empresas/{id_empresa}")
def desactivar_empresa(id_empresa: int, db: Session = Depends(get_db)):
    empresa_db = empresa_gestor.obtener(db, id_empresa)
    if not empresa_db or empresa_db.activo == 0:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    
    empresa_gestor.eliminar(db, id_empresa)
    return {"msg": "Empresa desactivada"}

@router.put("/api/admin/empresas/{id_empresa}/reactivar", response_model=EmpresaOut)
def reactivar_empresa(id_empresa: int, db: Session = Depends(get_db)):
    empresa_db = empresa_gestor.obtener(db, id_empresa)
    if not empresa_db:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    
    return empresa_gestor.reactivar(db, id_empresa)

@router.get("/api/admin/empresas")
def listar_empresas_admin(db: Session = Depends(get_db)):
    """Listar todas las empresas para administración"""
    try:
        empresas = db.query(EmpresaModel).filter(EmpresaModel.activo == 1).all()
        
        result = []
        for empresa in empresas:
            result.append({
                "id_empresa": empresa.id_empresa,
                "nombre": empresa.nombre,
                "razon_social": empresa.razon_social,
                "nif": empresa.nif,
                "telefono_empresa": empresa.telefono_empresa,
                "email_empresa": empresa.email_empresa,
                "activo": empresa.activo
            })
        
        return result
        
    except Exception as e:
        logger.error(f"Error al listar empresas: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
