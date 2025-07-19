def validar_log_sistema(log):
    if not log.usuario_id:
        raise ValueError("El id del usuario es obligatorio.")
    if not log.accion:
        raise ValueError("La acción no puede estar vacía.")
