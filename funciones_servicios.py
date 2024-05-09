def agregar_servicio(datos_servicio):
    datos_servicio=dict(datos_servicio)
    servicio=input("Deseas agregar servicios de (internet) ,o servicios de (planes)")
    if servicio=="internet":
        print("Hay servicios de internet por:")
        ## MOSTRAR POR PANTALLA LOS TIPOS DE SERVICIO DE INTERNE T##
        for i in datos_servicio[servicio]:
            print(i)
        opciones=input("De las anteriores cual deseas escoger? ")
    elif servicio=="planes":
        print("Tenemos servicio de planes: ")
        print("postpago")
        print("prepago")
    
    

