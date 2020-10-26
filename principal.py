from preguntas import preguntar

def main():
    """
    Función principal
    """
    ruta = "./datos/datos.json"
    ruta_preguntas = "./datos/respuestas.json"
    preguntar(ruta, ruta_preguntas)
main()
