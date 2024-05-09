import json

def traer_datos(archivo):
    datos=[]
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos

def guardar_datos(datos,archivo):
    datos=list(datos)
    lista=json.dumps(datos,indent=4)
    file=open(archivo,"w")
    file.write(lista)
    file.close()