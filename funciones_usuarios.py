from datos import guardar_datos
RUTA_USUARIOS="usuarios.json"


def agregar_usuario(datos_usuario):
    datos_usuario=list(datos_usuario)
    nombre=input("Ingresa el nombre del usuario: ")
    documento=input("Ingresa el documento del usuario: ")
    edad=input("Ingresa la edad del usuario: ")
    telefono=input("Ingresa el telefono del usuario: ")
    correo=input("Ingresa el correo del usuario: ")
    datos_usuario.append({"nombre":nombre,
                          "documento":documento,
                          "edad":edad,
                          "telefono":telefono,
                          "correo":correo,
                          "categoria":"nuevo_cliente",
                          "compras_servicios":{},
                          "compras_productos":{}
                          })
    guardar_datos(datos_usuario,RUTA_USUARIOS)
    return None

def eliminar_usuario(datos_usuario):
    datos_usuario=list(datos_usuario)
    documento=input("Ingrese el documento del usuario que desea eliminar: ")
    for i in range(len(datos_usuario)):
        if datos_usuario[i]["documento"]==documento:
            datos_usuario.pop(i)
            return datos_usuario
    print(f"No se encontró un usuario con documento: {documento}")
    guardar_datos(datos_usuario,RUTA_USUARIOS)
    return None

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
            print("Ya encontramos su usuario, nombre:", i["nombre"] )
            ##### SE RECORRE EL DICCIONARIO PARA BUSCAR LA OPCION A MODIFICAR ############
            for j in i:
                if j == opcion:
                    i[opcion]=input(f"Actualmente {opcion} tiene valor de {i[opcion]} escriba a que desea modificarlo: ")
                    guardar_datos(datos_usuario,RUTA_USUARIOS)
                    return None
                    ##### SI SE ENCUENTRA LA OPCION SE REEMPLAZA Y SE DEVUELVE datos_usuario
            print(f"Dentro de los datos_usuario de usuarios que tenemos no se encontró la opcion {opcion}")
            return None
            #### SI NO SE ENCUENTRA LA OPCION SE AVISA,Y SE DEVUELVE datos_usuario
    print(f"Dentro de los usuarios de la base de datos_usuario no hay uno con documento {documento},intentelo de nuevo")
    return None
    ### SI NO SE ENCUENTRA DOCUMENTO, SE AVISA Y SE DEVUELVE datos_usuario

def asignar_categoria_usuarios(datos_usuario):
    datos_usuario=list(datos_usuario)
    documento=input("Ingrese el documento de la persona a la que quiere asignar una categoria: ")
    ################ SE RECORRE EL DICCIONARIO PARA BUSCAR LA PERSONA #####################
    for i in datos_usuario:
        if i["documento"]==documento:
            print("Ya encontramos su usuario, nombre:" , i["nombre"] )
            print("Las categorias son (nuevo_cliente) (cliente_regular) (cliente_leal)")
            nueva_categoria=input("Actualmente categoria tiene valores de " +str(i["categoria"])+ " a que categoria desea cambiar el cliente: (1) (2) o (3) ")
            ########### SE VALIDA QUE NO ESTÉ YA EN ESA CATEGORIA PARA CAMBIARLO

            if nueva_categoria=="1" or nueva_categoria=="2" or nueva_categoria=="3":
                None
            else:
                print("Debías escoger entre las tres categorias")
                return None

            if nueva_categoria=="1":
                nueva_categoria="nuevo_cliente"
            elif nueva_categoria=="2":
                nueva_categoria="cliente_regular"
            else:
                nueva_categoria="cliente_leal"

            if i["categoria"]==nueva_categoria:
                print("El usuario ya está en esa categoria, debe ingresar a cual desea cambiarlo")
                return None
                ### SI NO ESTÁ EN ESA CATEGORIA Y A ESA SE DESEA CAMBIAR, SE HACE LA MODIFICACION
            elif i["categoria"]!=nueva_categoria:
                i["categoria"]=nueva_categoria
                guardar_datos(datos_usuario,RUTA_USUARIOS)
                return None
            print("Esa categoría no existe en nuestra base de datos_usuario, intente otra a la proxima")
            return None
    print(f"Dentro de los usuarios de la base de datos_usuario no hay uno con documento {documento},intentelo de nuevo")
    return None
    ### SI NO SE ENCUENTRA DOCUMENTO, SE AVISA Y SE DEVUELVE datos_usuario

