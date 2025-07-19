import re

def validar_persona(persona):
    if not persona.nombre:
        raise ValueError("El nombre de la persona es obligatorio.")
    if not persona.email:
        raise ValueError("El email de la persona es obligatorio.")
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", persona.email):
        raise ValueError("El formato del email no es válido.")
    if persona.dni and (len(persona.dni) != 9 or not persona.dni[:-1].isdigit() or not persona.dni[-1].isalpha()):
         raise ValueError("El formato del DNI no es válido.")
    # ... más validaciones ...
