def _validar_campos_comunes(actividad):
    """Validaciones compartidas entre creación y actualización."""
    if actividad.nombre and (len(actividad.nombre) < 3 or len(actividad.nombre) > 100):
        raise ValueError("El nombre de la actividad debe tener entre 3 y 100 caracteres.")
    
    if actividad.precio is not None and actividad.precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    if actividad.coste_economico is not None and actividad.coste_economico < 0:
        raise ValueError("El coste económico no puede ser negativo.")

def validar_actividad_create(actividad):
    """Valida una actividad en el momento de la creación."""
    if not actividad.nombre:
        raise ValueError("El nombre de la actividad es obligatorio.")
    _validar_campos_comunes(actividad)

def validar_actividad_update(actividad):
    """Valida una actividad en el momento de la actualización."""
    _validar_campos_comunes(actividad)
