from datos import traer_datos,guardar_datos
RUTA_SERVICIO_CLIENTE="servicio_cliente.json"
RUTA_SUGERENCIAS="sugerencias.json"
RUTA_RECLAMACIONES="reclamaciones.json"


def servicio_cliente():
    datos_servicio_cliente=traer_datos(RUTA_SERVICIO_CLIENTE)
    tipo=input("Deseas realizar una consulta al cliente por (servicios) (productos) o (general) ")

    if tipo=="servicios":
        opcion=input("En servicios hay de (internet) o de (planes) ")
        opcion.lower()
        if opcion=="internet" or opcion=="planes":
            mensaje=input("Escribe el mensaje que quiere dejar el cliente en servicio al cliente de servicios: ")
            datos_servicio_cliente.append({"numero":len(datos_servicio_cliente)+1,"tipo":tipo,"servicio":opcion,"pregunta":mensaje,"respuesta":"sin respuesta"})
            print("Gracias por su consulta, le responderemos tan pronto sea posible")
            guardar_datos(datos_servicio_cliente,RUTA_SERVICIO_CLIENTE)
        else:
            print("Debías escoger (internet) o (planes)")

    elif tipo=="productos":
        opcion=input("En productos hay de (celulares) o de (audifonos) ")
        opcion.lower()
        if opcion=="celulares" or opcion=="audifonos":
            mensaje=input("Escribe el mensaje que quiere dejar el cliente en servicio al cliente de productos")
            datos_servicio_cliente.append({"numero":len(datos_servicio_cliente)+1,"tipo":tipo,"servicio":opcion,"pregunta":mensaje,"respuesta":"sin respuesta"})
            guardar_datos(datos_servicio_cliente,RUTA_SERVICIO_CLIENTE)
            print("Gracias por su consulta, le responderemos tan pronto sea posible")
        else:
            print("Debías escoger (internet) o (planes)")

    elif tipo=="general":
        mensaje=input("Escribe el mensaje que quiere dejar el cliente en servicio al cliente de productos")
        datos_servicio_cliente.append({"numero":len(datos_servicio_cliente)+1,"tipo":"pregunta general","pregunta":mensaje,"respuesta":"sin respuesta"})
        print("Gracias por su consulta, le responderemos tan pronto sea posible")
        guardar_datos(datos_servicio_cliente,RUTA_SERVICIO_CLIENTE)
    else:
        print("Se debía escoger una de las opciones dichas")
        return None
    
def reclamacion():
    datos_reclamaciones=traer_datos(RUTA_RECLAMACIONES)
    tipo=input("Deseas realizar una reclamacion por (servicios) (productos) o (atencion al cliente)")

    if tipo=="servicios":
        opcion=input("En servicios hay de (internet) o de (planes)")
        opcion.lower()
        if opcion=="internet" or opcion=="planes":
            mensaje=input("Escribe el mensaje que quiere dejar el cliente en servicio al cliente de servicios: ")
            datos_reclamaciones.append({"numero":len(datos_reclamaciones)+1,"tipo":tipo,"servicio":opcion,"pregunta":mensaje,"respuesta":"sin respuesta"})
            print("Le responderemos tan pronto sea posible")
        else:
            print("Debías escoger (internet) o (planes)")

    elif tipo=="productos":
        opcion=input("En productos hay de (celulares) o de (audifonos)")
        opcion.lower()
        if opcion=="celulares" or opcion=="audifonos":
            mensaje=input("Escribe el mensaje que quiere dejar el cliente en reclamaciones de productos: ")
            datos_reclamaciones.append({"numero":len(datos_reclamaciones)+1,"tipo":tipo,"servicio":opcion,"pregunta":mensaje,"respuesta":"sin respuesta"})
            print("Le responderemos tan pronto sea posible")
        else:
            print("Debías escoger (internet) o (planes)")
            return None

    elif tipo=="atencion al cliente":
        mensaje=input("Escribe el mensaje que quiere dejar el cliente en reclamaciones por atencion al cliente")
        datos_reclamaciones.append({"numero":len(datos_reclamaciones)+1,"tipo":"pregunta general","pregunta":mensaje,"respuesta":"sin respuesta"})
        print("Le responderemos tan pronto sea posible")

    else:
        print("Se debía escoger una de las opciones dichas")
        return None
    guardar_datos(datos_reclamaciones,RUTA_RECLAMACIONES)

    
def sugerencia():
    datos_sugerencias=traer_datos(RUTA_SUGERENCIAS)
    mensaje=input("Escribe la sugerencia que quiere dejar el cliente ")
    datos_sugerencias.append({"numero":len(datos_sugerencias)+1,"sugerencia":mensaje,"respuesta":"sin respuesta"})
    print("Gracias por la sugerencia, le responderemos tan pronto sea posible")
    guardar_datos(datos_sugerencias,RUTA_SUGERENCIAS)
    
def responder_servicio_cliente():
    user="admin"
    password="admin123"
    intento_user=input("Para acceder a responder las preguntas, ingresa el usuario: ")
    intento_password=input("Ingresa la contraseña: ")
    if intento_user==user and intento_password==password:
        print("Ingreso exitoso")
        datos_servicio_cliente=traer_datos(RUTA_SERVICIO_CLIENTE)
    else:
        print("El usuario o contraseña son incorrectos")
        return None
    
    for preguntas in datos_servicio_cliente:
        print(preguntas)
    opcion=int(input("Ingresa el numero de la pregunta que deseas responder: "))

    for preguntas in datos_servicio_cliente:
        if preguntas["numero"]==opcion:
            print(preguntas)
            respuesta=input("Que deseas responder, a esta pregunta")
            preguntas["respuesta"]=respuesta
    guardar_datos(datos_servicio_cliente,RUTA_SERVICIO_CLIENTE)

def responder_reclamacion():
    user="admin"
    password="admin123"
    intento_user=input("Para acceder a responder las reclamaciones, ingresa el usuario: ")
    intento_password=input("Ingresa la contraseña: ")
    if intento_user==user and intento_password==password:
        print("Ingreso exitoso")
        print("******************************************************")
        datos_reclamacion=traer_datos(RUTA_RECLAMACIONES)
    else:
        print("El usuario o contraseña son incorrectos")
        return None
    
    for preguntas in datos_reclamacion:
        print(preguntas)
    opcion=int(input("Ingresa el numero de la reclamacion que deseas responder: "))

    for preguntas in datos_reclamacion:
        if preguntas["numero"]==opcion:
            print(preguntas)
            respuesta=input("Que deseas responder, a esta reclamacion")
            preguntas["respuesta"]=respuesta
            guardar_datos(datos_reclamacion,RUTA_RECLAMACIONES)
            return None
    print("Ingresaste un numero de pregunta que no se encuentra")
    
def responder_sugerencia():
    user="admin"
    password="admin123"
    intento_user=input("Para acceder a responder las sugerencias, ingresa el usuario: ")
    intento_password=input("Ingresa la contraseña: ")
    if intento_user==user and intento_password==password:
        print("Ingreso exitoso")
        datos_sugerencias=traer_datos(RUTA_SUGERENCIAS)
    else:
        print("El usuario o contraseña son incorrectos")
        return None
    
    for preguntas in datos_sugerencias:
        print(preguntas)
    opcion=int(input("Ingresa el numero de la sugerencia que deseas responder: "))

    for preguntas in datos_sugerencias:
        if preguntas["numero"]==opcion:
            print(preguntas)
            respuesta=input("Que deseas responder, a esta sugerencia")
            preguntas["respuesta"]=respuesta
    guardar_datos(datos_sugerencias,RUTA_SUGERENCIAS)
