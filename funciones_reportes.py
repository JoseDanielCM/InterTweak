from datos import *
from funciones_interaciones import txt_fecha_actual
RUTA_USUARIOS="usuarios.json"
RUTA_SERVICIOS="servicios.json"
RUTA_PRODUCTOS="productos.json"
RUTA_REPORTE_PRODUCTOS_CLIENTES="reporte_productos_clientes.json"
RUTA_YA_VENDIDOS="productos_ya_vendidos.json"
RUTA_SERVICIOS_POPULARES="servicios_populares.json"

def productos_clientes():
    datos_usuarios=traer_datos(RUTA_USUARIOS)
    datos_usuarios=list(datos_usuarios)

    datos_productos=traer_datos(RUTA_PRODUCTOS)

    reporte_productos_clientes=[]
    try:
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
        print("reporte realizado correctamente, revisa el archivo de 'reporte_productos_clientes.json'")
    except:
        print("Productos y clientes deben tener elementos")
        txt_fecha_actual("Productos y clientes deben tener elementos (reporte productos clientes)")

def productos_ya_vendidos(ya_vendidos):
    ya_vendidos=traer_datos(RUTA_YA_VENDIDOS)
    ya_vendidos=list(ya_vendidos)
    try:    
        datos_productos=traer_datos(RUTA_PRODUCTOS)

        for productos in datos_productos:
            for posicion in datos_productos[productos]:
                if posicion["vendidos"]>0:

                    if productos=="celulares":
                        print(posicion["marca"])
                        ya_vendidos.append({"Celular":posicion["marca"],"nombre":posicion["nombre"]})
                    else:
                        ya_vendidos.append({"audifonos":posicion["marca"],"nombre":posicion["nombre"]})
        print("Datos guardados correctamente revisar json de (productos ya vendidos) ")
        guardar_datos(ya_vendidos,RUTA_YA_VENDIDOS)
    except:
        print("Debe haber productos ya vendidos")
        txt_fecha_actual("Debe haber productos ya vendidos (reporte productos ya vendidos)")

def servicios_populares(datos_servicios):
    datos_populares=traer_datos(RUTA_SERVICIOS_POPULARES)
    datos_servicios=traer_datos(RUTA_SERVICIOS)
    datos_servicios=dict(datos_servicios)
    try:
        ################### SE GUARDA EN UNA LISTA TODAS LAS VENTAS PARA LUEGO COMPARAR ###############
        lista_vendidos_internet=[]
        for i in datos_servicios["internet"]:
            if len(datos_servicios["internet"][i])>=1:
                for j in datos_servicios["internet"][i]:
                    lista_vendidos_internet.append(j["vendidos"])
            else:
                print("No hay cantidad suficiente de servicios de internet para hacer un buen analisis \n")
                return datos_servicios
        #################### SE TRANSFORMAN PARA QUE NO QUEDEN DUPLICADOS ###########
        lista_vendidos_internet=set(lista_vendidos_internet)
        lista_vendidos_internet=list(lista_vendidos_internet)
        lista_vendidos_internet.reverse()
        #############################################################################

        for i in datos_servicios["internet"]:
            for j in datos_servicios["internet"][i]:
                if j["vendidos"]==lista_vendidos_internet[0] or j["vendidos"]==lista_vendidos_internet[1]:
                    datos_populares["internet"].append({"tipo":i,"identificador":j["identificador"]})
                    guardar_datos(datos_populares,RUTA_SERVICIOS_POPULARES)
                    
        lista_vendidos_planes=[]
        for i in datos_servicios["planes"]:
            if len(datos_servicios["planes"][i])>=2:
                for j in datos_servicios["planes"][i]:
                    lista_vendidos_planes.append(j["vendidos"])
            else:
                print("No hay cantidad suficiente de servicios de planes para hacer un buen analisis")
                return None
        ################### SE TRANSFORMAN PARA QUE NO QUEDEN DUPLICADOS ###########
        lista_vendidos_planes=set(lista_vendidos_planes)
        lista_vendidos_planes=list(lista_vendidos_planes)
        lista_vendidos_planes.reverse()
        #############################################################################
        for i in datos_servicios["planes"]:
            for j in datos_servicios["planes"][i]:
                if j["vendidos"]==lista_vendidos_planes[0] or j["vendidos"]==lista_vendidos_planes[1]:
                    datos_populares["planes"].append({"tipo":i,"identificador":j["identificador"]})
                    guardar_datos(datos_populares,RUTA_SERVICIOS_POPULARES)
        print("Mirar el json de servicios populares, cargados con exito \n")
    except:
        print("Debe haber servicios ya vendidos")
        txt_fecha_actual("Debe haber servicios ya vendidos de internet y planes (reporte servicios populares)")

