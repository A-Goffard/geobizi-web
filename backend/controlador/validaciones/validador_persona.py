import re

def _validar_campos_comunes(persona):
    """Validaciones compartidas entre creación y actualización."""
    if persona.nombre and (len(persona.nombre) < 2 or len(persona.nombre) > 50):
        raise ValueError("El nombre debe tener entre 2 y 50 caracteres.")
    
    if persona.apellido and (len(persona.apellido) < 2 or len(persona.apellido) > 50):
        raise ValueError("El apellido debe tener entre 2 y 50 caracteres.")

    if persona.telefono and not re.match(r"^\+?(\d\s?){9,15}$", persona.telefono):
        raise ValueError("El formato del teléfono no es válido.")

    if persona.dni:
        dni_upper = persona.dni.upper()
        regex = r"^(\d{8}[A-Z]{1})|([XYZ]{1}\d{7}[A-Z]{1})$"
        if not re.match(regex, dni_upper):
            raise ValueError("El formato del DNI/NIE no es válido.")

    if persona.cp and not re.match(r"^\d{5}$", persona.cp):
        raise ValueError("El código postal debe tener 5 dígitos.")

def validar_persona_create(persona):
    """Valida una persona en el momento de la creación."""
    if not persona.nombre:
        raise ValueError("El nombre es obligatorio.")
    if not persona.apellido:
        raise ValueError("El apellido es obligatorio.")
    if not persona.email:
        raise ValueError("El email es obligatorio.")
    if not persona.telefono:
        raise ValueError("El teléfono es obligatorio.")
    _validar_campos_comunes(persona)

def validar_persona_update(persona):
    """Valida una persona en el momento de la actualización."""
    _validar_campos_comunes(persona)
