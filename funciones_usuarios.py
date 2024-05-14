from datos import guardar_datos
from funciones_interaciones import txt_fecha_actual

RUTA_USUARIOS="usuarios.json"

def agregar_usuario(datos_usuario):
    datos_usuario=list(datos_usuario)
    nombre=input("Ingresa el nombre del usuario: ")
    if nombre.isdigit():
        print("El nombre solo debe tener caracteres alfanumericos")
        return None
    documento=input("Ingresa el documento del usuario: ")
    if (not documento.isdigit()) or len(documento)!=10:
        print("*El documento solo debe constar de digitos, y deben ser 10 \n")
        return None
    try:
        edad=int(input("Ingresa la edad del usuario: "))
    except Exception:
        print("*La edad debe ser un numero\n")
        txt_fecha_actual("Se intento colocar en (funcion agregar usuario) en valor (edad) un valor no entero")
        return None
    telefono=input("Ingresa el telefono del usuario: ")
    if (not telefono.isdigit()) or len(telefono)!=10:
        print("*El telefono solo debe constar de digitos, y deben ser 10 \n")
        return None
    correo=input("Ingresa el correo del usuario: ")
    if "@" in correo and ".com" in correo:
        None
    else:
        print("El correo debe tener '@' y finalizar con '.com' ")
        return None
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
    if ( not documento.isdigit()) or len(documento)!=10:
        print("*El documento solo debe constar de digitos, y deben ser 10 \n")
        return None
    for i in range(len(datos_usuario)):
        if datos_usuario[i]["documento"]==documento:
            datos_usuario.pop(i)
            print("Se elimino exitosamente")
            guardar_datos(datos_usuario,RUTA_USUARIOS)
            return None
    print(f"No se encontró un usuario con documento: {documento}")
    guardar_datos(datos_usuario,RUTA_USUARIOS)
    return None

def modificar_usuarios(datos_usuario):
    datos_usuario=list(datos_usuario)
    documento=input("Ingrese el documento de la persona a la que quiere realizar cambios: ")
    if (not documento.isdigit()) or len(documento)!=10:
        print("*El documento solo debe constar de digitos, y deben ser 10 \n")
        return None
    print("los datos_usuario que se tienen de los usuarios son los siguientes: ")
    if len(datos_usuario)>0:
        for i in datos_usuario[0]:
            if i!="categoria":
                print(i)
    else:
        print("No hay usuarios registrados aún, registra uno")
        txt_fecha_actual("Se intento realizar la funcion (modificar_usuarios) cuando no hay usuarios registrados")
        return None
    opcion=input("Que parametro deseas modificar? ")
    ################ SE RECORRE EL DICCIONARIO PARA BUSCAR LA PERSONA #####################
    for i in datos_usuario:
        try:
            if i["documento"]==documento:
                print("Ya encontramos su usuario, nombre:", i["nombre"] )
                ##### SE RECORRE EL DICCIONARIO PARA BUSCAR LA OPCION A MODIFICAR ############
                for j in i:
                    if j == opcion:
                        if opcion=="edad":
                            try:
                                i[opcion]=int(input(f"Actualmente {opcion} tiene valor de {i[opcion]} escriba a que desea modificarlo: "))
                                print("*Modificacion exitosa \n")
                            except Exception:
                                print("*La edad debe ser un numero\n")
                                txt_fecha_actual("Se intento colocar en (funcion modificar usuario) en valor (edad) un valor no entero")
                                return None
                        else:
                            i[opcion]=input(f"Actualmente {opcion} tiene valor de {i[opcion]} escriba a que desea modificarlo: ")
                            print("*Modificacion exitosa \n")
                        guardar_datos(datos_usuario,RUTA_USUARIOS)
                        return None
                        ##### SI SE ENCUENTRA LA OPCION SE REEMPLAZA Y SE DEVUELVE datos_usuario
                print(f"Dentro de los datos_usuario de usuarios que tenemos no se encontró la opcion {opcion}")
                return None
                #### SI NO SE ENCUENTRA LA OPCION SE AVISA,Y SE DEVUELVE datos_usuario
        except Exception:
            txt_fecha_actual("No se puede continuar, se borró datos de forma no permitida del json usuarios")
    print(f"Dentro de los usuarios de la base de datos_usuario no hay uno con documento {documento},intentelo de nuevo")
    return None

def asignar_categoria_usuarios(datos_usuario):
    datos_usuario=list(datos_usuario)
    documento=input("Ingrese el documento de la persona a la que quiere asignar una categoria: ")
    if (not documento.isdigit()) or len(documento)!=10:
        print("*El documento solo debe constar de digitos, y deben ser 10 \n")
        return None

    ################ SE RECORRE EL DICCIONARIO PARA BUSCAR LA PERSONA #####################
    for i in datos_usuario:
        try:
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
                    print("*El usuario ya está en esa categoria, debe ingresar a cual desea cambiarlo \n")
                    return None
                    ### SI NO ESTÁ EN ESA CATEGORIA Y A ESA SE DESEA CAMBIAR, SE HACE LA MODIFICACION
                elif i["categoria"]!=nueva_categoria:
                    i["categoria"]=nueva_categoria
                    guardar_datos(datos_usuario,RUTA_USUARIOS)
                    return None
                print("Esa categoría no existe en nuestra base de datos_usuario, intente otra a la proxima")
                return 
        except:
            txt_fecha_actual("No se puede continuar, se borró datos de forma no permitida del json usuarios")
    print(f"Dentro de los usuarios de la base de datos_usuario no hay uno con documento {documento},intentelo de nuevo")
    return None
    ### SI NO SE ENCUENTRA DOCUMENTO, SE AVISA Y SE DEVUELVE datos_usuario

