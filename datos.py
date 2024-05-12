import json

def traer_datos(archivo):
    datos=[]
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos

def guardar_datos(datos,archivo):
    if archivo=="usuarios.json" or archivo=="reporte_productos_clientes.json":
        datos=list(datos)
    else:
        datos=dict(datos)
    lista=json.dumps(datos,indent=3)
    file=open(archivo,"w")
    file.write(lista)
    file.close()