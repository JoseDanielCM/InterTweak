from datos import *

RUTA_USUARIOS="usuarios.json"
RUTA_SERVICIOS="servicios.json"
RUTA_PRODUCTOS="productos.json"

def realizar_venta():
    datos_usuarios=traer_datos(RUTA_USUARIOS)
    datos_servicios=traer_datos(RUTA_SERVICIOS)
    datos_productos=traer_datos(RUTA_PRODUCTOS)
    documento=input("Ingresa el documento del usuario que quiere comprar: ")
    objetivo=input("Que desea comprar el cliente? (servicios) o (productos): ")

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
        ################ AGREGAR 1 UNIDAD EN SERVICIOS ################
            for i in datos_servicios[servicio][opciones]:
                if i["identificador"]==indentificador:
                    i["vendidos"]+=1
                    guardar_datos(datos_servicios,RUTA_SERVICIOS)

        else:
            print("Debias ingresar una opcion valida (cable) (fibra optica) (satelital)")



    elif objetivo=="productos":
        ################# MOSTRAR PRODUCTOS QUE HAY #################
        producto=input("Que desea comprar el cliente? (celulares) o (audifonos)")
            ################################# AVISO###################################
            ######### VERIFICAR QUE PRODUCTO SEA CELULARES O AUDIFONOS ###############
            ##################### VOY ACÀ ###TODOSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
        print(f"Los siguientes son los {producto} que tenemos y sus caracteristicas:")
        for i in datos_servicios[producto]:
            print(i)
            print("********************************************************************")

        if producto=="celulares":
            opciones=input("Escriba el nombre del celular que desea: ")
        elif producto=="audifonos":
            opciones=input("Escriba el nombre del audifono que desea: ")

        for i in datos_servicios[servicio][opciones]:
            print(i)
            print("**********************************")
        indentificador=input("Ingresa el identificador del servicio que desea el cliente: ")
################ AGREGAR 1 UNIDAD EN SERVICIOS ################
        for i in datos_servicios[servicio][opciones]:
            if i["identificador"]==indentificador:
                i["vendidos"]+=1
                guardar_datos(datos_servicios,RUTA_SERVICIOS)


        if producto=="audifonos":
            None
        else:
            print("Debia escoger entre (celulares) o (audifonos)")
    else:
        print("Debes ingresar una opcion valida (servicios) o (productos)")

