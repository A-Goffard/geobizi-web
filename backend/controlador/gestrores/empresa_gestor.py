from .base import GestorBase
from database.models import Empresa

class EmpresaGestor(GestorBase):
    def crear(self, db, obj):
        empresa = Empresa(
            id_persona=obj.id_persona,
            nombre=obj.nombre,
            razon_social=obj.razon_social,
            nif=obj.nif,
            direccion=obj.direccion,
            provincia=obj.provincia,
            cp=obj.cp,
            nombre_contacto=obj.nombre_contacto,
            telefono_empresa=obj.telefono_empresa,
            email_empresa=obj.email_empresa,
            observaciones=obj.observaciones,
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
            # Usamos un bucle para actualizar solo los campos que vienen en el objeto de actualización
            update_data = obj.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(empresa, key, value)
            db.commit()
            db.refresh(empresa)
        return empresa

    def eliminar(self, db, id):
        empresa = db.query(Empresa).filter(Empresa.id_empresa == id).first()
        if empresa:
            empresa.activo = 0
            db.commit()
        return empresa

    def reactivar(self, db, id):
        empresa = db.query(Empresa).filter(Empresa.id_empresa == id).first()
        if empresa:
            empresa.activo = 1
            db.commit()
            db.refresh(empresa)
        return empresa
