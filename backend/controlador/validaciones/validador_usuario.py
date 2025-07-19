import re

def _validar_password(password):
    """Valida la fortaleza de una contraseña si se proporciona."""
    if not password:
        raise ValueError("La contraseña es obligatoria.")
    if len(password) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")
    if not re.search(r"[A-Z]", password):
        raise ValueError("La contraseña debe tener al menos una mayúscula.")
    if not re.search(r"[a-z]", password):
        raise ValueError("La contraseña debe tener al menos una minúscula.")
    if not re.search(r"[0-9]", password):
        raise ValueError("La contraseña debe tener al menos un número.")

def _validar_email(email):
    """Valida el formato y contenido de un email."""
    if not email:
        raise ValueError("El email es obligatorio.")
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        raise ValueError("El formato del email no es válido.")
    if "'" in email or '"' in email:
        raise ValueError("El email contiene caracteres no permitidos.")

def validar_usuario_create(usuario):
    """Valida un usuario en el momento de la creación."""
    _validar_email(usuario.email)
    _validar_password(usuario.password)

def validar_usuario_update(usuario):
    """Valida un usuario en el momento de la actualización."""
    _validar_email(usuario.email)
    # Si se proporciona una nueva contraseña, y solo si se proporciona, la validamos.
    if usuario.password:
        _validar_password(usuario.password)
