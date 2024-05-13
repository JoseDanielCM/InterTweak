import json

def traer_datos(archivo):
    datos=[]
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos

def guardar_datos(datos,archivo):
    archivos_listas=["usuarios.json","reporte_productos_clientes.json","servicio_cliente.json","sugerencias.json","reclamaciones.json"]
    if archivo in archivos_listas:
        datos=list(datos)
    else:
        datos=dict(datos)
    lista=json.dumps(datos,indent=3)
    file=open(archivo,"w")
    file.write(lista)
    file.close()