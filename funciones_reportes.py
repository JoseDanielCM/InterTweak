from datos import *

RUTA_USUARIOS="usuarios.json"
RUTA_PRODUCTOS="productos.json"
RUTA_REPORTE_PRODUCTOS_CLIENTES="reporte_productos_clientes.json"

def productos_clientes():
    datos_usuarios=traer_datos(RUTA_USUARIOS)
    datos_usuarios=list(datos_usuarios)

    datos_productos=traer_datos(RUTA_PRODUCTOS)

    reporte_productos_clientes=[]

    ################# CELULARES ########################

    ##################### PRODUCTOS ####################
    for i in datos_productos["celulares"]:
        comprados=[]
        producto=i["nombre"]
        ##################### USUARIOS ##################
        for j in datos_usuarios:
            cantidad=0
            if len(j["compras_productos"])>0:
                ############## USUARIOS ####################
                for compras in j["compras_productos"]:
                    if j["compras_productos"][compras]["nombre"]==producto:
                        cantidad=j["compras_productos"][compras]["cantidad"]
                        comprados.append({"usuario":j["nombre"],"cantidad":cantidad})
        reporte_productos_clientes.append({"producto":"celulares","nombre":producto,"comprados":comprados})
    guardar_datos(reporte_productos_clientes,RUTA_REPORTE_PRODUCTOS_CLIENTES)

    for i in datos_productos["audifonos"]:
        comprados=[]
        producto=i["nombre"]
        ##################### USUARIOS ##################
        for j in datos_usuarios:
            cantidad=0
            if len(j["compras_productos"])>0:
                ############## USUARIOS ####################
                for compras in j["compras_productos"]:
                    if j["compras_productos"][compras]["nombre"]==producto:
                        cantidad=j["compras_productos"][compras]["cantidad"]
                        comprados.append({"usuario":j["nombre"],"cantidad":cantidad})
        reporte_productos_clientes.append({"producto":"audifonos","nombre":producto,"comprados":comprados})
    guardar_datos(reporte_productos_clientes,RUTA_REPORTE_PRODUCTOS_CLIENTES)                                           
                                                        