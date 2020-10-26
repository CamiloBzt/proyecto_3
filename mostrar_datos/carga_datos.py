import json


def carga_dic(ruta: str):
    archivo = open(ruta, "r")
    datos = json.loads(archivo.read())
    archivo.close()
    return datos
