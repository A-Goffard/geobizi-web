from .base import GestorBase
from database.models import Empresa

class EmpresaGestor(GestorBase):
    def crear(self, db, obj):
        empresa = Empresa(
            id_persona=obj.id_persona,
            nombre=obj.nombre,
            razon_social=obj.razon_social,
            nif=obj.nif,
            sector=obj.sector,
            logo=obj.logo,
            ubicacion=obj.ubicacion
        )
        db.add(empresa)
        db.commit()
        db.refresh(empresa)
        return empresa

    def obtener(self, db, id):
        return db.query(Empresa).filter(Empresa.id_empresa == id).first()

    def actualizar(self, db, id, obj):
        empresa = db.query(Empresa).filter(Empresa.id_empresa == id).first()
        if empresa:
            empresa.id_persona = obj.id_persona
            empresa.nombre = obj.nombre
            empresa.razon_social = obj.razon_social
            empresa.nif = obj.nif
            empresa.sector = obj.sector
            empresa.logo = obj.logo
            empresa.ubicacion = obj.ubicacion
            db.commit()
            db.refresh(empresa)
        return empresa

    def eliminar(self, db, id):
        empresa = db.query(Empresa).filter(Empresa.id_empresa == id).first()
        db.delete(empresa)
        db.commit()
        return empresa
