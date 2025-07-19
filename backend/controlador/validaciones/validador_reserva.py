def validar_reserva(reserva):
    if not reserva.id_persona:
        raise ValueError("El id de la persona es obligatorio.")
    if not reserva.id_actividad:
        raise ValueError("El id de la actividad es obligatorio.")
    if reserva.numero_personas <= 0:
        raise ValueError("El número de personas debe ser mayor que cero.")
