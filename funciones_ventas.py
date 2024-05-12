from datos import *

RUTA_USUARIOS="usuarios.json"
RUTA_SERVICIOS="servicios.json"
RUTA_PRODUCTOS="productos.json"

def promocion_usuario():
    cliente_encontrado=False
    datos_usuarios=traer_datos(RUTA_USUARIOS)
    print("Actualmente contamos con promocion, si el cliente es menor de 22 años y se encuentra estudiando")
    documento=input("Ingresa el documento del usuario que quiere comprar: ")

    for i in datos_usuarios:
        if i["documento"]==documento:
            cliente_encontrado=True

    if cliente_encontrado==False:
        print("El cliente no se encontró en la base de datos, debes ingresar uno nuevo")
        return None
    
    for i in datos_usuarios:
        if i["edad"]<22 and i["documento"]==documento:
            ocupacion=input("Preguntale al cliente si actualmente se encuentra estudiando (si) (no) ")
            ocupacion.lower()
            if ocupacion=="si":
                promocion=True
            elif ocupacion=="no":
                promocion=False
            else:
                print("Se debía ingresar (si) o (no)")
    print(promocion)
    return promocion

def realizar_venta(promocion):
    encontrado=False
    cliente_encontrado=False
    datos_usuarios=traer_datos(RUTA_USUARIOS)
    datos_servicios=traer_datos(RUTA_SERVICIOS)
    datos_productos=traer_datos(RUTA_PRODUCTOS)
    documento=input("Ingresa el documento del usuario que quiere comprar: ")

    ########### COMPROBACIONES #####################

    for i in datos_usuarios:
        if i["documento"]==documento:
            cliente_encontrado=True

    if cliente_encontrado==False:
        print("El cliente no se encontró en la base de datos, debes ingresar uno nuevo")
        return None

    objetivo=input("Que desea comprar el cliente? (servicios) o (productos): ")

    ########### COMPROBACIONES #####################

    if objetivo == "servicios" or objetivo=="productos":
        None
    else:
        print("Debías escoger una de las dos opciones")
        return None
############### TODOS SERVICIOS #######################
    if objetivo=="servicios":

        servicio=input("Que servicio desea comprar? (internet) o (planes): ")

        if servicio=="internet" or servicio=="planes":

            ################# MOSTRAR SERVICIOS QUE HAY #######################
            print(f"Para servicios de {servicio} tenemos los siguientes")
            for i in datos_servicios[servicio]:
                print(i)
            opciones=input("De las anteriores opciones cual desea el cliente?: ")

        else:
            print("Debías escoger o internet o planes")
            return None

        if opciones=="cable" or opciones=="fibra optica" or opciones=="satelital" or opciones=="prepago" or opciones=="postpago":
        ############ MOSTRAR SERVICIOS DE INTERNET CABLE ##############
            print(f"Para internet de {opciones} tenemos las siguientes opciones:")
            print("*"*len(f"Para internet de {opciones} tenemos las siguientes opciones:"))
            for i in datos_servicios[servicio][opciones]:
                print(i)
                print("********************************************************************")
            indentificador=input("Ingresa el identificador del servicio que desea el cliente: ")

            aceptar=input("Ingresa la cantidad de dienero que te dió el cliente")
        ################ AGREGAR 1 UNIDAD VENDIDA EN SERVICIOS ################
            for i in datos_servicios[servicio][opciones]:
                if i["identificador"]==indentificador and aceptar>= i["precio"]:
                    encontrado=True
                    i["vendidos"]+=1
                    if aceptar ==i["precio"]:
                        print("No le debes devolver cambio")
                    else:
                        print("le debes devolver "+(aceptar-i["precio"]))
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
                
        else:
            print("Debias ingresar una opcion valida (cable) (fibra optica) (satelital) (prepago) (pospago)")
            return None
        
############### TODOS PRODUCTOS #######################
    else:

        ################# MOSTRAR PRODUCTOS QUE HAY #################
        producto=input("Que desea comprar el cliente? (celulares) o (audifonos): ")

        if producto=="celulares" or producto=="audifonos":
            None
        else:
            print("debías escoger (celulares) o (audifonos) ")
            return None

        print(f"Los siguientes son los {producto} que tenemos y sus caracteristicas:")
        
        for i in datos_productos[producto]:
            print(i)
            print("********************************************************************")

        if producto=="celulares":
            nombre=input("Escriba el nombre del celular que desea: ")
            cantidad=int(input(f"Cuantos {nombre} desea? "))
        elif producto=="audifonos":
            nombre=input("Escriba el nombre del audifono que desea: ")
            cantidad=int(input(f"Cuantos {nombre} desea? "))


        ################ GUARDAR LA POSICION DEL USUARIO PARA USARLA LUEGO EN LA VERIFICACION ########
        for i in range(len(datos_usuarios)):
            if datos_usuarios[i]["documento"]==documento:
                posicion_usuario=i
                break
        
################ AGREGAR 1 UNIDAD EN SERVICIOS ################
        producto_encontrado=False
        for i in datos_productos[producto]:
    ########### VERIFICAR QUE EL PRODUCTÓ ESTÉ ####################
            if i["nombre"]==nombre:
                producto_encontrado=True

                if datos_usuarios[posicion_usuario]["categoria"] in i["nivel"]:
        ################# VERIFICAR QUE ALCANCES LOS PRODUCTOS PARA LA VENTA #######
                    if i["unidades"]>=cantidad:
        ############## VERIFICAR QUE EL CLIENTE CUENTE CON LA CANTIDAD DE DINERO NECESARIA ####
                        precio=i["precio"]
                        if promocion==True:
                            precio=int(precio*0.7)
                        print("En total serían ",precio*cantidad)                    
                        aceptar=int(input("Cuanto dinero te entregó el cliente? "))
                        if aceptar>precio*cantidad:
                            print("Compra exitosa")
                            print("Devuelvele al cliente $",(aceptar-precio*cantidad))
                            i["vendidos"]+=cantidad
                            i["unidades"]-=cantidad
                            guardar_datos(datos_productos,RUTA_PRODUCTOS)

                        elif aceptar==precio*cantidad:
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
                else:
                    print("El cliente no posee con el nivel suficiente para adquirir este producto")
                    return None
        if producto_encontrado==False:
            print("No se encontró tal nombre de producto en nuestro catalogo")
            return None
        
        ######## TODO AGREGAR LA COMPRA AL USUARIO ################
        for i in datos_usuarios:
            if i["documento"]==documento:
                num_compra=int(len(i["compras_productos"])+1)
                i["compras_productos"]={f"compra {num_compra}":{"tipo":producto,"nombre":nombre,"cantidad":cantidad}}
                guardar_datos(datos_usuarios,RUTA_USUARIOS)
                return None
        print("No se encontró dal documento de usuario")
        return None

