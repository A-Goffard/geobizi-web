import re


def _validar_campos_comunes(empresa):
    """Validaciones compartidas entre creación y actualización."""
    if empresa.nombre and (len(empresa.nombre) < 2 or len(empresa.nombre) > 100):
        raise ValueError("El nombre de la empresa debe tener entre 2 y 100 caracteres.")

    if empresa.razon_social and (len(empresa.razon_social) < 2 or len(empresa.razon_social) > 100):
        raise ValueError("La razón social debe tener entre 2 y 100 caracteres.")

    if empresa.nif:
        nif_upper = empresa.nif.upper()
        # Regex mejorada para DNI, NIE y NIF de personas jurídicas
        regex = r"^([A-Z]{1}\d{7}[A-Z0-9]{1})|(\d{8}[A-Z]{1})|([XYZ]{1}\d{7}[A-Z]{1})$"
        if not re.match(regex, nif_upper):
            raise ValueError("El formato del NIF no es válido.")

    if empresa.direccion and (len(empresa.direccion) < 5 or len(empresa.direccion) > 150):
        raise ValueError("La dirección debe tener entre 5 y 150 caracteres.")

    if empresa.cp and not re.match(r"^\d{5}$", empresa.cp):
        raise ValueError("El código postal debe tener 5 dígitos.")


def validar_empresa_create(empresa):
    """Valida una empresa en el momento de la creación."""
    if not empresa.nombre:
        raise ValueError("El nombre de la empresa es obligatorio.")
    if not empresa.razon_social:
        raise ValueError("La razón social es obligatoria.")
    if not empresa.direccion:
        raise ValueError("La dirección es obligatoria.")
    if not empresa.cp:
        raise ValueError("El código postal es obligatorio.")
    _validar_campos_comunes(empresa)


def validar_empresa_update(empresa):
    """Valida una empresa en el momento de la actualización."""
    _validar_campos_comunes(empresa)
