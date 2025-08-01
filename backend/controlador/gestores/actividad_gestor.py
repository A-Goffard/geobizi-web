from .base import GestorBase
from database.models import Actividad

class ActividadGestor(GestorBase):
    def crear(self, db, obj):
        actividad = Actividad(
            tipo=obj.tipo,
            nombre=obj.nombre,
            lugar=obj.lugar,
            fecha=obj.fecha,
            hora=obj.hora,
            descripcion=obj.descripcion,
            responsable=obj.responsable,
            duracion=obj.duracion,
            coste_economico=obj.coste_economico,
            coste_horas=obj.coste_horas,
            facturacion=obj.facturacion,
            resultados=obj.resultados,
            valoracion=obj.valoracion,
            observaciones=obj.observaciones,
            estado=obj.estado,
            num_participantes=obj.num_participantes,
            categoria=obj.categoria,
            visible_publico=obj.visible_publico,
            created_at=obj.created_at,
            updated_at=obj.updated_at
        )
        db.add(actividad)
        db.commit()
        db.refresh(actividad)
        return actividad

    def obtener(self, db, id):
        return db.query(Actividad).filter(Actividad.id_actividad == id).first()

    def actualizar(self, db, id, obj):
        actividad = db.query(Actividad).filter(Actividad.id_actividad == id).first()
        if actividad:
            update_data = obj.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(actividad, key, value)
            db.commit()
            db.refresh(actividad)
        return actividad

    def eliminar(self, db, id):
        actividad = db.query(Actividad).filter(Actividad.id_actividad == id).first()
        if actividad:
            actividad.activo = 0
            db.commit()
        return actividad

    def reactivar(self, db, id):
        actividad = db.query(Actividad).filter(Actividad.id_actividad == id).first()
        if actividad:
            actividad.activo = 1
            db.commit()
            db.refresh(actividad)
        return actividad