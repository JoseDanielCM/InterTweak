def agregar_usuario(datos_usuario):
    datos_usuario=list(datos_usuario)
    nombre=input("Ingresa el nombre del usuario: ")
    documento=input("Ingresa el documento del usuario: ")
    edad=input("Ingresa la edad del usuario: ")
    telefono=input("Ingresa el telefono del usuario: ")
    correo=input("Ingresa el correo del usuario: ")
    datos_usuario.append({"nombre":nombre,"documento":documento,"edad":edad,"telefono":telefono,"correo":correo,"categoria":{"nuevo_cliente":True,"cliente_regular":False,"cliente_leal":False}})
    return datos_usuario

def eliminar_usuario(datos_usuario):
    datos_usuario=list(datos_usuario)
    documento=input("Ingrese el documento del usuario que desea eliminar: ")
    for i in range(len(datos_usuario)):
        if datos_usuario[i]["documento"]==documento:
            datos_usuario.pop(i)
            return datos_usuario
    print(f"No se encontró un usuario con documento: {documento}")
    return datos_usuario

def modificar_usuarios(datos_usuario):
    datos_usuario=list(datos_usuario)
    documento=input("Ingrese el documento de la persona a la que quiere realizar cambios: ")
    print("los datos_usuario que se tienen de los usuarios son los siguientes: ")
    for i in datos_usuario[0]:
        if i!="categoria":
            print(i)
    opcion=input("Que parametro deseas modificar? ")
    ################ SE RECORRE EL DICCIONARIO PARA BUSCAR LA PERSONA #####################
    for i in datos_usuario:
        if i["documento"]==documento:
            print(f"Ya encontramos su usuario, nombre: {i["nombre"]}")
            ##### SE RECORRE EL DICCIONARIO PARA BUSCAR LA OPCION A MODIFICAR ############
            for j in i:
                if j == opcion:
                    i[opcion]=input(f"Actualmente {opcion} tiene valor de {i[opcion]} escriba a que desea modificarlo: ")
                    return datos_usuario
                    ##### SI SE ENCUENTRA LA OPCION SE REEMPLAZA Y SE DEVUELVE datos_usuario
            print(f"Dentro de los datos_usuario de usuarios que tenemos no se encontró la opcion {opcion}")
            return datos_usuario
            #### SI NO SE ENCUENTRA LA OPCION SE AVISA,Y SE DEVUELVE datos_usuario
    print(f"Dentro de los usuarios de la base de datos_usuario no hay uno con documento {documento},intentelo de nuevo")
    return datos_usuario
    ### SI NO SE ENCUENTRA DOCUMENTO, SE AVISA Y SE DEVUELVE datos_usuario

def asignar_categoria_usuarios(datos_usuario):
    datos_usuario=list(datos_usuario)
    documento=input("Ingrese el documento de la persona a la que quiere asignar una categoria: ")
    ################ SE RECORRE EL DICCIONARIO PARA BUSCAR LA PERSONA #####################
    for i in datos_usuario:
        if i["documento"]==documento:
            print(f"Ya encontramos su usuario, nombre: {i["nombre"]}")
            nueva_categoria=input(f"Actualmente categoria tiene valores de {i["categoria"]} a que categoria desea cambiar el cliente: ")
            ########### SE VALIDA QUE NO ESTÉ YA EN ESA CATEGORIA PARA CAMBIARLO
            for j in i["categoria"]:
                if i["categoria"][j]==True and nueva_categoria==j:
                    print("El usuario ya está en esa categoria, debe ingresar a cual desea cambiarlo")
                    return datos_usuario
                ### SI NO ESTÁ EN ESA CATEGORIA Y A ESA SE DESEA CAMBIAR, SE HACE LA MODIFICACION
                elif i["categoria"][j]==False and nueva_categoria==j:
                    ##### SE DEJAN TODAS EN FALSE
                    i["categoria"]["nuevo_cliente"]=False
                    i["categoria"]["cliente_regular"]=False
                    i["categoria"]["cliente_leal"]=False
                    #### SE COLOCA EN TRUE,LA DESEADA
                    i["categoria"][nueva_categoria]=True
                    return datos_usuario
            print("Esa categoría no existe en nuestra base de datos_usuario, intente otra a la proxima")
            return datos_usuario
    print(f"Dentro de los usuarios de la base de datos_usuario no hay uno con documento {documento},intentelo de nuevo")
    return datos_usuario
    ### SI NO SE ENCUENTRA DOCUMENTO, SE AVISA Y SE DEVUELVE datos_usuario

