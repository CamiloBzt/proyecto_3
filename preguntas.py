from mostrar_datos.carga_datos import carga_dic
from validaciones.validar import val_num, val_gen, val_nombre, val_cedula


def llenar_datos(ruta_encuesta):
    encuestados = carga_dic(ruta_encuesta)
    datos = dict()
    print('\n\nBienvenido\n\n')
    cedula = val_cedula('\tDigite su cedula:')
    nombre = val_nombre('\tIngrese su nombre: ')
    edad = val_num('\tIngrese su edad: ')
    genero = val_gen('\t Ingrese su genero (1: masculino, 0: femenino): ')


def preguntar(ruta_encuesta, ruta_preguntas):
    encuestados = carga_dic(ruta_encuesta)
    preguntas = carga_dic(ruta_preguntas)
    for pregunta in preguntas:
        print(pregunta)
        for respuestas in preguntas[pregunta]:
            print(respuestas)
