from .base import GestorBase
from database.models import Mensaje

class MensajeGestor(GestorBase):
    def crear(self, db, obj):
        mensaje = Mensaje(
            id_persona=obj.id_persona,
            contenido=obj.contenido,
            fecha_envio=obj.fecha_envio
        )
        db.add(mensaje)
        db.commit()
        db.refresh(mensaje)
        return mensaje

    def obtener(self, db, id):
        return db.query(Mensaje).filter(Mensaje.id_mensaje == id).first()

    def actualizar(self, db, id, obj):
        mensaje = db.query(Mensaje).filter(Mensaje.id_mensaje == id).first()
        if mensaje:
            mensaje.contenido = obj.contenido
            db.commit()
            db.refresh(mensaje)
        return mensaje

    def eliminar(self, db, id):
        mensaje = db.query(Mensaje).filter(Mensaje.id_mensaje == id).first()
        if mensaje:
            db.delete(mensaje)
            db.commit()
        return mensaje
