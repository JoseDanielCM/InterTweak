from datos import *

RUTA_USUARIOS="usuarios.json"
RUTA_SERVICIOS="servicios.json"
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

def productos_ya_vendidos():
    print("Los siguientes son los productos que ya han tenido ventas: ")
    datos_productos=traer_datos(RUTA_PRODUCTOS)

    for productos in datos_productos:
        for posicion in datos_productos[productos]:
            if posicion["vendidos"]>0:
                if productos=="celulares":
                    print("Celular "+posicion["marca"]+" "+posicion["nombre"])
                else:
                    print("Audifono "+posicion["marca"]+" "+posicion["nombre"])

def servicios_populares(datos_servicios):
    datos_servicios=traer_datos(RUTA_SERVICIOS)
    datos_servicios=dict(datos_servicios)
    print("LOS SERVICIOS CON MAS VENTAS EN INTERNET SON")
    print("")
    ################### SE GUARDA EN UNA LISTA TODAS LAS VENTAS PARA LUEGO COMPARAR ###############
    lista_vendidos_internet=[]
    for i in datos_servicios["internet"]:
        if len(datos_servicios["internet"][i])>=1:
            for j in datos_servicios["internet"][i]:
                lista_vendidos_internet.append(j["vendidos"])
        else:
            print("No hay cantidad suficiente de servicios de internet para hacer un buen analisis")
            return datos_servicios
    #################### SE TRANSFORMAN PARA QUE NO QUEDEN DUPLICADOS ###########
    lista_vendidos_internet=set(lista_vendidos_internet)
    lista_vendidos_internet=list(lista_vendidos_internet)
    lista_vendidos_internet.reverse()
    #############################################################################


    for i in datos_servicios["internet"]:
        for j in datos_servicios["internet"][i]:
            if j["vendidos"]==lista_vendidos_internet[0] or j["vendidos"]==lista_vendidos_internet[1]:
                print(i+" -> identificador: "+j["identificador"])
    print("")
                

    print("LOS SERVICIOS CON MAS VENTAS EN PLANES SON")
    print("")
    lista_vendidos_planes=[]
    for i in datos_servicios["planes"]:
        if len(datos_servicios["planes"][i])>=2:
            for j in datos_servicios["planes"][i]:
                lista_vendidos_internet.append(j["vendidos"])
        else:
            print("No hay cantidad suficiente de servicios de planes para hacer un buen analisis")
            return datos_servicios
    ################### SE TRANSFORMAN PARA QUE NO QUEDEN DUPLICADOS ###########
    lista_vendidos_planes=set(lista_vendidos_planes)
    lista_vendidos_planes=list(lista_vendidos_planes)
    lista_vendidos_planes.reverse()
    #############################################################################

    for i in datos_servicios["planes"]:
        for j in datos_servicios["planes"][i]:
            if j["vendidos"]==lista_vendidos_internet[0] or j["vendidos"]==lista_vendidos_internet[1]:
                print(i+" -> identificador: "+j["identificador"])
