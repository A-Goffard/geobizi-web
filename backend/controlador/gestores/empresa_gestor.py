from .base import GestorBase
from database.models import Empresa

class EmpresaGestor(GestorBase):
    def crear(self, db, obj):
        # Comprobar duplicados por nombre, NIF o email_empresa
        existe = db.query(Empresa).filter(
            (Empresa.nombre == obj.nombre) |
            (Empresa.nif == obj.nif) |
            (Empresa.email_empresa == obj.email_empresa)
        ).first()
        if existe:
            raise ValueError("Ya existe una empresa con ese nombre, NIF o email.")

        empresa = Empresa(
            nombre=obj.nombre,
            razon_social=obj.razon_social,
            nif=obj.nif,
            direccion=obj.direccion,
            provincia=obj.provincia,
            cp=obj.cp,
            nombre_contacto=getattr(obj, "nombre_contacto", None),
            email_contacto=getattr(obj, "email_contacto", None),
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
