def validar_reserva_create(reserva):
    # Aquí puedes poner tus validaciones, por ejemplo:
    if not hasattr(reserva, "id_persona") or not reserva.id_persona:
        raise ValueError("El campo id_persona es obligatorio")
    if not hasattr(reserva, "id_actividad") or not reserva.id_actividad:
        raise ValueError("El campo id_actividad es obligatorio")
    if not hasattr(reserva, "numero_personas") or reserva.numero_personas < 1:
        raise ValueError("El campo numero_personas debe ser mayor que 0")
    
    # Validación de número de teléfono (si está en el objeto reserva)
    telefono = getattr(reserva, "telefono", None)
    if telefono:
        import re
        # Ejemplo: acepta solo dígitos y longitud entre 7 y 15
        if not re.fullmatch(r"\d{7,15}", telefono):
            raise ValueError("El número de teléfono debe contener solo dígitos y tener entre 7 y 15 caracteres")
    # ...otras validaciones que necesites...
