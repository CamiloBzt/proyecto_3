
def val_num(mensaje):
    numero = input(mensaje)
    while not numero.isnumeric():
        numero = input(mensaje)
    return int(numero)

def val_gen(mensaje):
    numero = input(mensaje)
    while numero != 0 or numero != 1:
        numero = input(mensaje)
    return int(numero)

def val_nombre(mensaje):
    nombre = input(mensaje)
    while not nombre.isalpha():
        nombre = input(mensaje)
    return nombre

def val_cedula(mensaje):
    cedula = input(mensaje)
    while not cedula.isnumeric():
        cedula = input(mensaje)
    return cedula