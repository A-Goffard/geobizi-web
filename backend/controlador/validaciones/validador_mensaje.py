def validar_mensaje(mensaje):
    if not mensaje.id_persona:
        raise ValueError("El id de la persona es obligatorio.")
    if not mensaje.contenido or len(mensaje.contenido.strip()) == 0:
        raise ValueError("El contenido del mensaje no puede estar vacío.")
    if len(mensaje.contenido) > 1000:
        raise ValueError("El contenido del mensaje es demasiado largo.")
