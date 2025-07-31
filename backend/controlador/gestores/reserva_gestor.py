from .base import GestorBase
from database.models import Reserva
from datetime import datetime

class ReservaGestor(GestorBase):
    def crear(self, db, obj):
        reserva = Reserva(
            id_persona=obj.id_persona,
            id_actividad=obj.id_actividad,
            numero_personas=obj.numero_personas,
            fecha_reserva=obj.fecha_reserva if obj.fecha_reserva else datetime.now(),
            mensaje=getattr(obj, "mensaje", None),
            forma_pago=getattr(obj, "forma_pago", None),
            aprobada=True,
            confirmacion_enviada=False,
            activo=1
        )
        db.add(reserva)
        db.commit()
        db.refresh(reserva)
        return reserva

    def obtener(self, db, id):
        return db.query(Reserva).filter(Reserva.id_reserva == id).first()

    def actualizar(self, db, id, obj):
        reserva = db.query(Reserva).filter(Reserva.id_reserva == id).first()
        if reserva:
            reserva.aprobada = obj.aprobada
            reserva.numero_personas = obj.numero_personas
            reserva.confirmacion_enviada = obj.confirmacion_enviada
            db.commit()
            db.refresh(reserva)
        return reserva

    def eliminar(self, db, id):
        reserva = db.query(Reserva).filter(Reserva.id_reserva == id).first()
        if reserva:
            db.delete(reserva)
            db.commit()
        return reserva
