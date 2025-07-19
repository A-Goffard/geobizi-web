def validar_empresa(empresa):
    if not empresa.nombre:
        raise ValueError("El nombre de la empresa es obligatorio.")
    if empresa.nif and len(empresa.nif) != 9:
        raise ValueError("El NIF debe tener 9 caracteres.")
    # ... más validaciones ...
