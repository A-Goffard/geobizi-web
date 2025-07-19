from .base import GestorBase
from database.models import LogSistema

class LogSistemaGestor(GestorBase):
    def crear(self, db, obj):
        log = LogSistema(
            fecha=obj.fecha,
            usuario_id=obj.usuario_id,
            accion=obj.accion,
            descripcion=obj.descripcion,
            actividad_modificada=obj.actividad_modificada,
            actividad_agregada=obj.actividad_agregada
        )
        db.add(log)
        db.commit()
        db.refresh(log)
        return log

    def obtener(self, db, id):
        return db.query(LogSistema).filter(LogSistema.id_log_sistema == id).first()

    def actualizar(self, db, id, obj):
        # Generalmente los logs no se actualizan, pero se implementa por completitud
        log = db.query(LogSistema).filter(LogSistema.id_log_sistema == id).first()
        if log:
            log.descripcion = obj.descripcion
            db.commit()
            db.refresh(log)
        return log

    def eliminar(self, db, id):
        # Generalmente los logs no se eliminan
        log = db.query(LogSistema).filter(LogSistema.id_log_sistema == id).first()
        if log:
            db.delete(log)
            db.commit()
        return log
