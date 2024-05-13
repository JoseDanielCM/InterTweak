from funciones_interaciones import txt_fecha_actual
from datos import guardar_datos

RUTA_SERVICIOS="servicios.json"

def agregar_servicio(datos_servicio):
    datos_servicio=dict(datos_servicio)
    servicio=input("Deseas agregar servicios de (internet) ,o servicios de (planes): ")

    if servicio=="internet":
        print("Hay servicios de internet por:")
        ## MOSTRAR POR PANTALLA LOS TIPOS DE SERVICIO DE INTERNET####
        try:
            for i in datos_servicio[servicio]:
                print(i)
            opciones=input("De las anteriores cual deseas escoger? ")
            if opciones=="cable":
                contador=len(datos_servicio[servicio][opciones])
                if len(contador)==1:
                    contador="0"+contador
                
                identificador=("C"+str(contador))
                try:
                    mb_subida=int(input("Ingresa la cantidad de mb de SUBIDA del nuevo servicio: "))
                    mb_bajada=int(input("Ingresa la cantidad de mb de BAJADA del nuevo servicio: "))
                    precio=int(input("Ingresa  el precio del nuevo servicio de cable: "))
                except Exception:
                    print("*Los mb y el precio deben ser un numero entero\n")
                    txt_fecha_actual("Se intento colocar en (funcion agregar servicio) en valores (mb o precio) un valor no entero")
                    return None
                datos_servicio[servicio][opciones].append({"identificador":identificador,"mb_subida":mb_subida,"mb_bajada":mb_bajada,"precio":precio})
                guardar_datos(datos_servicio,RUTA_SERVICIOS)
                return None
            
            elif opciones=="fibra_optica":
                contador=len(datos_servicio[servicio][opciones])
                if len(contador)==1:
                    contador="0"+contador
                
                identificador=("F"+str(contador))
                try:
                    mb_simetricos=int(input("Ingresa la cantidad de mb del nuevo servicio: "))
                    precio=int(input("Ingresa  el percio del nuevo servicio: "))
                except Exception:
                    print("*Los mb y el precio deben ser un numero entero\n")
                    txt_fecha_actual("Se intento colocar en (funcion agregar servicio) en valores (mb o precio) un valor no entero")
                    return None
                datos_servicio[servicio][opciones].append({"identificador":identificador,"mb_simetricos":mb_simetricos,"precio":precio})
                guardar_datos(datos_servicio,RUTA_SERVICIOS)
                return None

            elif opciones=="satelital":
                contador=len(datos_servicio[servicio][opciones])
                if len(contador)==1:
                    contador="0"+contador
                
                identificador=("S"+str(contador))
                mb=int(input("Ingresa la cantidad de mb del nuevo servicio: "))
                precio=int(input("Ingresa  el precio del nuevo servicio: "))
                datos_servicio[servicio][opciones].append({"identificador":identificador,"mb":mb,"precio":precio})
                guardar_datos(datos_servicio,RUTA_SERVICIOS)
                return None

            else:
                print("Debes ingresar una opcion de servicio de internet valida")
                guardar_datos(datos_servicio,RUTA_SERVICIOS)
                return None
        except Exception:
            print("No se puede continuar, se borró datos de forma no permitida del json servicios")
            txt_fecha_actual("Se debio haber borrado datos de forma no permitida del json servicios")

    elif servicio=="planes":
        print("Tenemos servicio de planes: ")
        print("postpago")
        print("prepago")
        opciones=input("Ingresa a cual de las dos deseas agregar un nuevo servicio: ")
        try:
            if opciones=="postpago":
                contador=len(datos_servicio[servicio][opciones])
                if len(contador)==1:
                    contador="0"+contador    
                identificador=("PT"+str(contador))

                gb=input("Ingresa la cantidad de gb del nuevo servicio: ")
                red=input("Ingresa el tipo de red del nuevo servicio: ")
                precio=input("Ingresa  el percio del nuevo servicio: ")
                datos_servicio[servicio][opciones].append({"identificador":identificador,
                                                        "gb":gb,
                                                        "red":red,
                                                        "precio":precio})
                guardar_datos(datos_servicio,RUTA_SERVICIOS)
                return None
            
            elif opciones=="prepago":
                contador=len(datos_servicio[servicio][opciones])
                if len(contador)==1:
                    contador="0"+contador    
                identificador=("PR"+str(contador))
                contenido=input("Ingresa el contenido de el plan prepago: ")
                duracion=input("El plan prepago dura (horas) o (dias): ")
                if duracion=="horas":
                    horas=int(input("Ingresa la cantidad de horas que dura el plan: "))
                    dias=None
                elif duracion=="dias":
                    horas=None
                    dias=input("Ingresa la cantidad de dìas que dura el plan: ")
                else:
                    print("Debes ingresar una de las unidades de tiempo pedidas")
                    guardar_datos(datos_servicio,RUTA_SERVICIOS)
                    return None
                    
                precio=input("Ingresa  el percio del nuevo servicio: ")
                datos_servicio[servicio][opciones].append({"identificador":identificador,
                                                        "contenido":contenido,
                                                        "horas":horas,
                                                        "dias":dias,
                                                        "precio":precio})
                guardar_datos(datos_servicio,RUTA_SERVICIOS)
            
            else:
                print("Debes ingresar una opcion de servicio de planes valida")
                guardar_datos(datos_servicio,RUTA_SERVICIOS)
                return None
        except Exception:
            print("No se puede continuar, se debio borrar algun dato inicial necesario en")
            txt_fecha_actual("Se debio haber borrado datos de forma no permitida del json servicios")
    print("debes ingresar un tipo de servicio valido, internet o planes")
    guardar_datos(datos_servicio,RUTA_SERVICIOS)

def eliminar_servicios(datos_servicio):
    try:    
        datos_servicio=dict(datos_servicio)
        servicio=input("El servicio que deseas eliminar pertenece a (internet) o (planes)")
        identificador=input("Ingrese el identificador del servicio de internet que desea eliminar: ")
        ############## MODIFICAR SERVICIOS DE INTERNET ##########
        if servicio=="internet":
            if identificador[0]=="C":
                opcion="cable"
            elif identificador[0]=="F":
                opcion="fibra optica"
            elif identificador[0]=="S":
                opcion="satelital"
            else:
                print("Ese identificador no se encuentra en nuestros servicios")
                guardar_datos(datos_servicio,RUTA_SERVICIOS)
                return None

            for i in range(len(datos_servicio["internet"][opcion])):
                if datos_servicio["internet"][opcion][i]["identificador"]==identificador:
                    datos_servicio["internet"][opcion].pop(i)
                    guardar_datos(datos_servicio,RUTA_SERVICIOS)
                    return None
            print(f"El identificador {identificador} no se encuentra en nuestros servicios")
            guardar_datos(datos_servicio,RUTA_SERVICIOS)
            return None
        ################## MODIFICAR PLANES #################
        elif servicio=="planes":
            if identificador[:2]=="PR":
                opcion="prepago"
            elif identificador[:2]=="PT":
                opcion="postpago"
            else:
                print("Ese identificador no se encuentra en nuestros servicios")
                guardar_datos(datos_servicio,RUTA_SERVICIOS)
                return None

            for i in range(len(datos_servicio["internet"][opcion])):
                if datos_servicio["planes"][opcion][i]["identificador"]==identificador:
                    datos_servicio["planes"][opcion].pop(i)
                    guardar_datos(datos_servicio,RUTA_SERVICIOS)
                    return None
            print(f"El identificador {identificador} no se encuentra en nuestros servicios")
            guardar_datos(datos_servicio,RUTA_SERVICIOS)
            return None
        ################ CASO INGRESO INVALIDO ################
        else:
            print("Debías escoger en servicio: internet o planes")
            guardar_datos(datos_servicio,RUTA_SERVICIOS)
            return None
    except Exception:
        print("Deben haber registrados servicios para eliminar o se borraron datos iniciales de estos")
        txt_fecha_actual("No hay servicios registradoso o se borraron datos iniciales de estos")

def modificar_servicios(datos_servicio):
    try: 
        datos_servicio=dict(datos_servicio)
        servicio=input("El servicio que deseas modificar pertenece a (internet) o (planes)")
        identificador=input("Ingrese el identificador del servicio de internet que desea modificar: ")
        ############## MODIFICAR SERVICIOS DE INTERNET ##########
        if servicio=="internet":
            if identificador[0]=="C":
                opcion="cable"
            elif identificador[0]=="F":
                opcion="fibra optica"
            elif identificador[0]=="S":
                opcion="satelital"
            else:
                print("Ese identificador no se encuentra en nuestros servicios")
                txt_fecha_actual("Ingreso de identificador no usado en (modificar servicios)")
                guardar_datos(datos_servicio,RUTA_SERVICIOS)
                return None

            print("Los valores que se pueden modificar son:")
            for i in datos_servicio["internet"][opcion][0]:
                print(i)

            for i in range(len(datos_servicio["internet"][opcion])):
                if datos_servicio["internet"][opcion][i]["identificador"]==identificador:
                    objetivo=input("Ingresa que parametro desea modificar:")
                    cambio=input("Actualmente "+identificador+" en "+objetivo+" tiene valor de "+str(datos_servicio["internet"][opcion][i][objetivo])+" a que valor desea modificarlo")
                    datos_servicio["internet"][opcion][i][objetivo]=int(cambio)
                    guardar_datos(datos_servicio,RUTA_SERVICIOS)
                    return None
            print(f"El identificador {identificador} no se encuentra en nuestros servicios")
            guardar_datos(datos_servicio,RUTA_SERVICIOS)
            return None
        ################## MODIFICAR PLANES #################
        elif servicio=="planes":
            if identificador[:2]=="PR":
                opcion="prepago"
            elif identificador[:2]=="PT":
                opcion="postpago"
            else:
                print("Ese identificador no se encuentra en nuestros servicios")
                txt_fecha_actual("Ingreso de identificador no usado en (modificar servicios)")
                guardar_datos(datos_servicio,RUTA_SERVICIOS)
                return None

            print("Los valores que se pueden modificar son:")
            for i in datos_servicio["planes"][opcion][0]:
                print(i)
            try: 
                for i in range(len(datos_servicio["planes"][opcion])):
                    if datos_servicio["planes"][opcion][i]["identificador"]==identificador:
                        objetivo=input("Ingresa que parametro desea modificar:")
                        cambio=input("Actualmente "+identificador+" en "+objetivo+" tiene valor de "+str(datos_servicio["internet"][opcion][i][objetivo])+" a que valor desea modificarlo")
                        datos_servicio["planes"][opcion][i][objetivo]=cambio
                        guardar_datos(datos_servicio,RUTA_SERVICIOS)
                        return None
            except Exception:
                print("Se debía ingresar un parametro valido en los valores modificables ")
                txt_fecha_actual("Ingreso de identificador no usado en (modificar servicios)")

            print(f"El identificador {identificador} no se encuentra en nuestros servicios")
            guardar_datos(datos_servicio,RUTA_SERVICIOS)
            return None
        ################ CASO INGRESO INVALIDO ################
        else:
            print("Debías escoger en servicio: internet o planes")
            guardar_datos(datos_servicio,RUTA_SERVICIOS)
            return None
    except Exception:
        print("Deben haber registrados servicios para eliminar o se borraron datos iniciales de estos")
        txt_fecha_actual("No hay servicios registradoso o se borraron datos iniciales de estos")
