from .base import GestorBase
from database.models import Usuario

class UsuarioGestor(GestorBase):
    def crear(self, db, obj):
        usuario = Usuario(
            id_persona=obj.id_persona,
            id_rol=obj.id_rol,
            email=obj.email,
            password=obj.password
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario

    def obtener(self, db, id):
        return db.query(Usuario).filter(Usuario.id_usuario == id).first()

    def actualizar(self, db, id, obj):
        usuario = db.query(Usuario).filter(Usuario.id_usuario == id).first()
        if usuario:
            usuario.id_persona = obj.id_persona
            usuario.id_rol = obj.id_rol
            usuario.email = obj.email
            usuario.password = obj.password
            db.commit()
            db.refresh(usuario)
        return usuario

    def eliminar(self, db, id):
        usuario = db.query(Usuario).filter(Usuario.id_usuario == id).first()
        db.delete(usuario)
        db.commit()
        return usuario
