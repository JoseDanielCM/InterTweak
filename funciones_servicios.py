def agregar_servicio(datos_servicio):
    datos_servicio=dict(datos_servicio)
    servicio=input("Deseas agregar servicios de (internet) ,o servicios de (planes)")

    if servicio=="internet":
        print("Hay servicios de internet por:")
        ## MOSTRAR POR PANTALLA LOS TIPOS DE SERVICIO DE INTERNET##
        for i in datos_servicio[servicio]:
            print(i)
        opciones=input("De las anteriores cual deseas escoger? ")
        if opciones=="cable":

            identificador=input("Ingresa el identificador del nuevo servicio de internet por cable")
            mb_subida=input("Ingresa la cantidad de mb de SUBIDA del nuevo servicio")
            mb_bajada=input("Ingresa la cantidad de mb de BAJADA del nuevo servicio")
            precio=input("Ingresa  el percio del nuevo servicio de cable")
            datos_servicio[servicio][opciones].append({"identificador":identificador,"mb_subida":mb_subida,"mb_bajada":mb_bajada,"precio":precio})
            return datos_servicio
        
        elif opciones=="fibra_optica":

            identificador=input("Ingresa el identificador del nuevo servicio de fibra optica")
            mb_simetricos=input("Ingresa la cantidad de mb del nuevo servicio")
            precio=input("Ingresa  el percio del nuevo servicio")
            datos_servicio[servicio][opciones].append({"identificador":identificador,"mb_simetricos":mb_simetricos,"precio":precio})
            return datos_servicio

        elif opciones=="satelital":

            identificador=input("Ingresa el identificador del nuevo servicio satelital")
            mb=input("Ingresa la cantidad de mb del nuevo servicio")
            precio=input("Ingresa  el percio del nuevo servicio")
            datos_servicio[servicio][opciones].append({"identificador":identificador,"mb":mb,"precio":precio})
            return datos_servicio

        else:
            print("Debes ingresar una opcion de servicio de internet valida")
            return datos_servicio

    elif servicio=="planes":
        print("Tenemos servicio de planes: ")
        print("postpago")
        print("prepago")
        opciones=input("Ingresa a cual de las dos deseas agregar un nuevo servicio")

        if opciones=="postpago":

            identificador=input("Ingresa el identificador del nuevo servicio satelital")
            gb=input("Ingresa la cantidad de gb del nuevo servicio")
            red=input("Ingresa el tipo de red del nuevo servicio")
            precio=input("Ingresa  el percio del nuevo servicio")
            datos_servicio[servicio][opciones].append({"identificador":identificador,
                                                       "gb":gb,
                                                       "red":red,
                                                       "precio":precio})
            return datos_servicio
        
        elif opciones=="prepago":

            identificador=input("Ingresa el identificador del nuevo servicio satelital")
            contenido=input("Ingresa el contenido de el plan prepago")
            duracion=input("El plan prepago dura (horas) o (dias)")
            if duracion=="horas":
                horas=int(input("Ingresa la cantidad de horas que dura el plan "))
                dias=None
            elif duracion=="dias":
                horas=int(None)
                dias=input("Ingresa la cantidad de dìas que dura el plan")
            else:
                print("Debes ingresar una de las unidades de tiempo pedidas")
                return datos_servicio
                
            precio=input("Ingresa  el percio del nuevo servicio")
            datos_servicio[servicio][opciones].append({"identificador":identificador,
                                                       "contenido":contenido,
                                                       "horas":horas,
                                                       "dias":dias,
                                                       "precio":precio})
            return datos_servicio
        
        else:
            print("Debes ingresar una opcion de servicio de planes valida")
            return datos_servicio
    print("debes ingresar un tipo de servicio valido, internet o planes")
    return datos_servicio