from datos import *

RUTA_USUARIOS="usuarios.json"
RUTA_SERVICIOS="servicios.json"
RUTA_PRODUCTOS="productos.json"

def realizar_venta():
    encontrado=False
    datos_usuarios=traer_datos(RUTA_USUARIOS)
    datos_servicios=traer_datos(RUTA_SERVICIOS)
    datos_productos=traer_datos(RUTA_PRODUCTOS)
    documento=input("Ingresa el documento del usuario que quiere comprar: ")
    objetivo=input("Que desea comprar el cliente? (servicios) o (productos): ")

############### TODOS SERVICIOS #######################
    if objetivo=="servicios":
        servicio=input("Que servicio desea comprar? (internet) o (planes): ")
        ################# MOSTRAR SERVICIOS QUE HAY #######################
        print(f"Para servicios de {servicio} tenemos los siguientes")
        for i in datos_servicios[servicio]:
            print(i)
        opciones=input("De las anteriores opciones cual desea el cliente?: ")

        if opciones=="cable" or opciones=="fibra optica" or opciones=="satelital" or opciones=="prepago" or opciones=="postpago":
        ############ MOSTRAR SERVICIOS DE INTERNET CABLE ##############
            print(f"Para internet de {opciones} tenemos las siguientes opciones:")
            print("*"*len(f"Para internet de {opciones} tenemos las siguientes opciones:"))
            for i in datos_servicios[servicio][opciones]:
                print(i)
                print("********************************************************************")
            indentificador=input("Ingresa el identificador del servicio que desea el cliente: ")
        ################ AGREGAR 1 UNIDAD VENDIDA EN SERVICIOS ################
            for i in datos_servicios[servicio][opciones]:
                if i["identificador"]==indentificador:
                    encontrado=True
                    i["vendidos"]+=1
                    guardar_datos(datos_servicios,RUTA_SERVICIOS)
            if encontrado==False:
                print("No se encontró tal identificador")
                return None
        ################ AGREGAR LA VENTA AL USUARIO ##########################
            for i in datos_usuarios:
                if i["documento"]==documento:
                    num_compra=int(len(i["compras_servicios"])+1)
                    i["compras_servicios"]={f"compra {num_compra}":{"identificador":indentificador}}
                    guardar_datos(datos_usuarios,RUTA_USUARIOS)
                    return None
            print("No se encontró dal documento de usuario")
            return None
        else:
            print("Debias ingresar una opcion valida (cable) (fibra optica) (satelital)")
            return None
############### TODOS PRODUCTOS #######################
    elif objetivo=="productos":


        ################# MOSTRAR PRODUCTOS QUE HAY #################
        producto=input("Que desea comprar el cliente? (celulares) o (audifonos): ")
            ################################# AVISO###################################
            ######### VERIFICAR QUE PRODUCTO SEA CELULARES O AUDIFONOS ###############
        print(f"Los siguientes son los {producto} que tenemos y sus caracteristicas:")
        #
        for i in datos_productos[producto]:
            print(i)
            print("********************************************************************")

        if producto=="celulares":
            nombre=input("Escriba el nombre del celular que desea: ")
            cantidad=int(input(f"Cuantos {nombre} desea? "))
        elif producto=="audifonos":
            nombre=input("Escriba el nombre del audifono que desea: ")
            cantidad=int(input(f"Cuantos {nombre} desea? "))
        else:
            print("Debías escoger entre celulares o audifonos")
            return None

################ AGREGAR 1 UNIDAD EN SERVICIOS ################
        for i in datos_productos[producto]:
    ########### VERIFICAR QUE EL PRODUCTÓ ESTÉ ####################
            if i["nombre"]==nombre:
                nombre_encontrado=True
    ################# VERIFICAR QUE ALCANCES LOS PRODUCTOS PARA LA VENTA #######
                if i["unidades"]>=cantidad:
    ############## VERIFICAR QUE EL CLIENTE CUENTE CON LA CANTIDAD DE DINERO NECESARIA ####
                    print("En total serían ",i["precio"]*cantidad)                    
                    aceptar=int(input("Cuanto dinero te entregó el cliente? "))
                    if aceptar>i["precio"]*cantidad:
                        print("Compra exitosa")
                        print("Devuelvele al cliente $",(aceptar-i["precio"]*cantidad))
                        i["vendidos"]+=cantidad
                        i["unidades"]-=cantidad
                        guardar_datos(datos_productos,RUTA_PRODUCTOS)

                    elif aceptar==i["precio"]*cantidad:
                        print("Compra exitosa, se entregó la cantidad justa de dinero, no es necesario devolver cambio")
                        i["vendidos"]+=cantidad
                        i["unidades"]-=cantidad
                        guardar_datos(datos_productos,RUTA_PRODUCTOS)

                    else:
                        print("El cliente no entregó el dinero suficiente ")
                        return None
                else:
                    print("No se posee el stock suficiente para realizar")
                    return None
        if nombre_encontrado==False:
            print("No se encontró tal nombre de producto en nuestro catalogo")
        
        ######## TODO AGREGAR LA COMPRA AL USUARIO ################
        for i in datos_usuarios:
            if i["documento"]==documento:
                num_compra=int(len(i["compras_productos"])+1)
                i["compras_productos"]={f"compra {num_compra}":{"tipo":producto,"nombre":nombre,"cantidad":cantidad}}
                guardar_datos(datos_usuarios,RUTA_USUARIOS)
                return None
        print("No se encontró dal documento de usuario")
        return None

    else:
        print("Debes ingresar una opcion valida (servicios) o (productos)")

