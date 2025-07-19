from .base import GestorBase
from database.models import Reserva

class ReservaGestor(GestorBase):
    def crear(self, db, obj):
        reserva = Reserva(
            id_persona=obj.id_persona,
            id_actividad=obj.id_actividad,
            fecha_reserva=obj.fecha_reserva,
            aprobada=obj.aprobada,
            numero_personas=obj.numero_personas,
            confirmacion_enviada=obj.confirmacion_enviada
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
