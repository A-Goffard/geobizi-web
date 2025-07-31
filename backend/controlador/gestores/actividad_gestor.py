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
            actividad.tipo = obj.tipo
            actividad.nombre = obj.nombre
            actividad.lugar = obj.lugar
            actividad.fecha = obj.fecha
            actividad.hora = obj.hora
            actividad.descripcion = obj.descripcion
            actividad.responsable = obj.responsable
            actividad.duracion = obj.duracion
            actividad.coste_economico = obj.coste_economico
            actividad.coste_horas = obj.coste_horas
            actividad.facturacion = obj.facturacion
            actividad.resultados = obj.resultados
            actividad.valoracion = obj.valoracion
            actividad.observaciones = obj.observaciones
            actividad.estado = obj.estado
            actividad.num_participantes = obj.num_participantes
            actividad.categoria = obj.categoria
            actividad.visible_publico = obj.visible_publico
            actividad.created_at = obj.created_at
            actividad.updated_at = obj.updated_at
            db.commit()
            db.refresh(actividad)
        return actividad

    def eliminar(self, db, id):
        actividad = db.query(Actividad).filter(Actividad.id_actividad == id).first()
        db.delete(actividad)
        db.commit()
        return actividad
