from preguntas import preguntar, llenar_datos
from validaciones.validar import val_opcion


def main():
    """
    Función principal
    """
    ruta = "./datos/datos.json"
    ruta_preguntas = "./datos/respuestas.json"
    print('\n\n\t\tTest Vocacional\n\n')
    opcion = val_opcion('Presione enter para empezar con la encuesta 0 de lo contrario --->')
    while opcion == '':
        llenar_datos(ruta)
        preguntar(ruta, ruta_preguntas)
        opcion = val_opcion('Presione enter para empezar con la encuesta 0 de lo contrario --->')

    print('Hasta luego')
main()
