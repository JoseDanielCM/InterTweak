from datos import traer_datos,guardar_datos
RUTA_SERVICIO_CLIENTE="servicio_cliente.json"
RUTA_SUGERENCIAS="sugerencias.json"
RUTA_RECLAMACIONES="reclamaciones.json"


def servicio_cliente():
    datos_servicio_cliente=traer_datos(RUTA_SERVICIO_CLIENTE)
    tipo=input("Deseas realizar una consulta al cliente por (servicios) (productos) o (general)")

    if tipo=="servicios":
        opcion=input("En servicios hay de (internet) o de (planes)")
        opcion.lower()
        if opcion=="internet" or opcion=="planes":
            mensaje=input("Escribe el mensaje que quiere dejar el cliente en servicio al cliente de servicios")
            datos_servicio_cliente.append({"numero":len(datos_servicio_cliente)+1,"tipo":tipo,"servicio":opcion,"pregunta":mensaje,"respuesta":"sin respuesta"})
        else:
            print("Debías escoger (internet) o (planes)")

    elif tipo=="productos":
        opcion=input("En productos hay de (celulares) o de (audifonos)")
        opcion.lower()
        if opcion=="celulares" or opcion=="audifonos":
            mensaje=input("Escribe el mensaje que quiere dejar el cliente en servicio al cliente de productos")
            datos_servicio_cliente.append({"numero":len(datos_servicio_cliente)+1,"tipo":tipo,"servicio":opcion,"pregunta":mensaje,"respuesta":"sin respuesta"})
        else:
            print("Debías escoger (internet) o (planes)")

    elif tipo=="general":
        mensaje=input("Escribe el mensaje que quiere dejar el cliente en servicio al cliente de productos")
        datos_servicio_cliente.append({"numero":len(datos_servicio_cliente)+1,"tipo":"pregunta general","pregunta":mensaje,"respuesta":"sin respuesta"})

    else:
        print("Se debía escoger una de las opciones dichas")
        return None
    
def reclamacion():
    None
    
def sugerencia():
    None
    
def responder_servicio_cliente():
    None
    
def responder_reclamacion():
    None
    
def responder_sugerencia():
    None
