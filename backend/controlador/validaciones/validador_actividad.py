def validar_actividad(actividad):
    if not actividad.nombre:
        raise ValueError("El nombre de la actividad es obligatorio.")
    if actividad.coste_economico is not None and actividad.coste_economico < 0:
        raise ValueError("El coste no puede ser negativo.")
    # ... más validaciones ...
