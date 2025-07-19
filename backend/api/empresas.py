from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from database.database import SessionLocal
from database.models import Empresa as EmpresaModel
from schemas.empresa import EmpresaCreate, EmpresaUpdate, EmpresaOut
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/admin/empresas", response_model=EmpresaOut)
def crear_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = db.query(EmpresaModel).filter(EmpresaModel.nif == empresa.nif).first()
    if db_empresa:
        raise HTTPException(status_code=400, detail="El NIF ya está registrado para otra empresa.")
    
    nueva_empresa = EmpresaModel(**empresa.model_dump())
    db.add(nueva_empresa)
    db.commit()
    db.refresh(nueva_empresa)
    return nueva_empresa

@router.get("/admin/empresas", response_model=List[EmpresaOut])
def listar_empresas(db: Session = Depends(get_db)):
    return db.query(EmpresaModel).options(selectinload(EmpresaModel.persona)).filter(EmpresaModel.activo == 1).all()

@router.get("/admin/empresas/inactivas", response_model=List[EmpresaOut])
def listar_empresas_inactivas(db: Session = Depends(get_db)):
    return db.query(EmpresaModel).options(selectinload(EmpresaModel.persona)).filter(EmpresaModel.activo == 0).all()

@router.put("/admin/empresas/{id_empresa}", response_model=EmpresaOut)
def modificar_empresa(id_empresa: int, empresa: EmpresaUpdate, db: Session = Depends(get_db)):
    empresa_db = db.query(EmpresaModel).filter(EmpresaModel.id_empresa == id_empresa, EmpresaModel.activo == 1).first()
    if not empresa_db:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    
    update_data = empresa.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(empresa_db, key, value)
    
    db.commit()
    db.refresh(empresa_db)
    return empresa_db

@router.delete("/admin/empresas/{id_empresa}")
def desactivar_empresa(id_empresa: int, db: Session = Depends(get_db)):
    empresa_db = db.query(EmpresaModel).filter(EmpresaModel.id_empresa == id_empresa, EmpresaModel.activo == 1).first()
    if not empresa_db:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    empresa_db.activo = 0
    db.commit()
    return {"msg": "Empresa desactivada"}

@router.put("/admin/empresas/{id_empresa}/reactivar", response_model=EmpresaOut)
def reactivar_empresa(id_empresa: int, db: Session = Depends(get_db)):
    empresa_db = db.query(EmpresaModel).filter(EmpresaModel.id_empresa == id_empresa).first()
    if not empresa_db:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    empresa_db.activo = 1
    db.commit()
    db.refresh(empresa_db)
    return empresa_db
