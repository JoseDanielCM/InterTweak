from funciones_interaciones import txt_fecha_actual
from datos import guardar_datos

RUTA_PRODUCTOS="productos.json"


def agregar_producto(datos_productos):
    ########### DEFINIR DATOS ###########
    datos_productos=dict(datos_productos)

    ########### OBTENER DATOS ###########
    producto=input("Deseas agregar un producto de tipo (celulares) o (audifonos): ")
    #####################################
    if producto=="celulares":

        nombre=input("Ingresa el nombre del celular (sin la marca): ")
        marca=input("Ingresa la marca del celular: ")
        try:
            gb=int(input("Ingresa la capacidad de almacenamiento del celular,en gb: "))
        except Exception:
            print("*Los gb deben ser un numero\n")
            txt_fecha_actual("Se trato de ingresar en (agregar_producto) en (gb) un valor no entero")
            return None
        print("Ingresa el nivel ('1' si todos lo pueden comprar)")
        print("'2' si solo lo pueden comprar clientes regulares")
        print("'3' si solo lo pueden comprar clientes leales")
        nivel=input()
        if nivel=="1" or nivel=="2" or nivel=="3":
            nivel=["nuevo_cliente","cliente_regular","cliente_leal"]
        elif nivel=="2":
            nivel=["cliente_regular","cliente_leal"]
        elif nivel=="3":
            nivel=["cliente_leal"]
        else:
            print("Debías ingresar un nivel entre los tres")
            txt_fecha_actual("Se trato de ingresar en (agregar_producto) en (nivel) un valor no pedido")
            return None
        try:
            precio=int(input("Ingresa el precio del celular: "))
        except Exception:
            print("*el precio debe ser un numero entero\n")
            txt_fecha_actual("Se trato de ingresar en (agregar_producto) en (precio) un valor no entero")
            return None
        try:
            unidades=int(input(f"Ingresa cuantas unidades hay de este celular {marca} {nombre}"))
        except Exception:
            print("*Las unidades deben ser un valor numerico entero\n")
            txt_fecha_actual("Se trato de ingresar en (agregar_producto) en (gb) un valor no entero")
            return None

    ########### AGREGAR DATOS ###########
        datos_productos[producto].append({"nombre":nombre,"marca":marca,"gb":gb,"nivel":nivel,"precio":precio,"unidades":unidades})
        guardar_datos(datos_productos,RUTA_PRODUCTOS)
        return None
    
    elif producto=="audifonos":
        nombre=input("Ingresa el nombre del audifono (sin la marca): ")
        marca=input("Ingresa la marca del audifono: ")
        clase=input("Ingresa la clase de audifonos (inalambricos) o (cable): ")
        if clase=="inalambricos" or clase=="cable":
            None
        else:
            print("Se debía ingresar (inalambricos) o (cable)")
            txt_fecha_actual("en (agregar_producto) en (clase) se intento agregar un valor no correspondiente (inalambricos) o (cable)")
            return None
        print("Ingresa el nivel ('1' si todos lo pueden comprar)")
        print("'2' si solo lo pueden comprar clientes regulares")
        print("'3' si solo lo pueden comprar clientes leales")
        nivel=input()
        if nivel=="1":
            nivel=["nuevo_cliente","cliente_regular","cliente_leal"]
        elif nivel=="2":
            nivel=["cliente_regular","cliente_leal"]
        elif nivel=="3":
            nivel=["cliente_leal"]
        else:
            print("Debías ingresar un nivel entre los tres")
            txt_fecha_actual("En (agregar productos) se ingreso en (nivel) un dato diferente a (1) (2) o (3)")
            return None
        try:
            precio=int(input("Ingresa el precio del audifono: "))
        except Exception:
            print("*El precio del audifono debe ser un numero entero\n")
            txt_fecha_actual("Se intento colocar en (funcion agregar producto) en valor (precio) un valor no entero")
            return None
        try:
            unidades=int(input(f"Ingresa cuantas unidades hay de estos audifonos {marca} {nombre}"))
        except Exception:
            print("*La cantidad de unidades debe ser un numero entero\n")
            txt_fecha_actual("Se intento colocar en (funcion agregar producto) en valor (unidades) un valor no entero")
            return None
    ########### AGREGAR DATOS ###########
        datos_productos[producto].append({"nombre":nombre,"marca":marca,"clase":clase,"nivel":nivel,"precio":precio,"unidades":unidades})
        guardar_datos(datos_productos,RUTA_PRODUCTOS)
        return None
    else:
        print("Debías ingresar un producto valido, (celulares) o (audifonos)")
        txt_fecha_actual("En (agregar producto) en producto se ingreso un valor diferente a (celulares) y (audifonos)")
        return None
    
def modificar_productos(datos_productos):

    datos_productos=dict(datos_productos)

    ########### OBTENER DATOS ###########
    producto=input("Deseas modificar un producto de tipo (celulares) o (audifonos): ")
    #####################################
    if producto=="celulares":
    
        ###### MOSTRAR LOS PRODUCTOS QUE SE TIENEN DE CELULARES ########
        print("Actualmente hay estos celulares: ")
        print("*"*len("Actualmente hay estos celulares: "))
        for i in datos_productos[producto]:
            print("marca: "+i["marca"])
            print("nombre: "+i["nombre"])
            ###### ASTERISCOS DEL TAMAÑO DEL TEXTO #########
            print("*"*(len(i["nombre"])+8))
            ################################################

        nombre=input("Cual de esos celulares deseas modificar? (escribe el nombre): ")
        try:
            for i in datos_productos[producto]:
                if i["nombre"]==nombre:
                    objetivo=input("deseas modificar el (precio), las (unidades) o el (nivel)? ")
                    
                    if objetivo=="nivel":
                        modificacion=input("A que nivel deseas cambiarlo (1) (2) o (3) ")
                        if modificacion=="1":
                            modificacion=["nuevo_cliente","cliente_regular","cliente_leal"]
                        elif modificacion=="2":
                            modificacion=["cliente_regular","cliente_leal"]
                        elif modificacion=="3":
                            modificacion=["cliente_leal"]
                        else:
                            print("Debías ingresar un nivel entre los tres")
                            return None
                    elif objetivo=="precio" or objetivo=="unidades":
                        try:
                            modificacion=int(input(f"Actualmente {objetivo} tiene valor de "+str(i[objetivo])+" a que valor desea modificarlo: "))
                        except Exception:
                            print("*se intento ingresar un precio o unidades con valor no entero\n")
                            txt_fecha_actual("Se intento colocar en (funcion modificar productos) en valores (precio o unidades) un valor no entero")
                            return None

                    else:
                        print("Debías ingresar un objetivo valido (precio) (unidades) (nivel)")
                        return None

                    i[objetivo]=modificacion
                    print(f"{objetivo} cambiado exitosamente")
                    guardar_datos(datos_productos,RUTA_PRODUCTOS)
                    return None
        except Exception:
            print("No se han ingresado productos")
            txt_fecha_actual("Se intento modificar productos de celulares y no se encontro alguno, ingresar productos primero")
            
        print("No se encontro tal nombre en nuestra lista de celulares")
        return None
            
    elif producto=="audifonos":
    
        ###### MOSTRAR LOS PRODUCTOS QUE SE TIENEN DE AUDIFONOS ########
        print("Actualmente hay estos audifonos: ")
        print("*"*len("Actualmente hay estos audifonos: "))
        for i in datos_productos[producto]:
            print("marca: "+i["marca"])
            print("nombre: "+i["nombre"])
            ###### ASTERISCOS DEL TAMAÑO DEL TEXTO #########
            print("*"*(len(i["nombre"])+8))
            ################################################

        nombre=input("Cual de esos audifonos deseas modificar? (escribe el nombre)")
        try:
            for i in datos_productos[producto]:
                if i["nombre"]==nombre:
                    objetivo=input("deseas modificar el (precio), las (unidades) o el (nivel)? ")
                    
                    if objetivo=="nivel":
                        modificacion=input("A que nivel deseas cambiarlo (1) (2) o (3) ")
                        if modificacion=="1":
                            modificacion=["nuevo_cliente","cliente_regular","cliente_leal"]
                        elif modificacion=="2":
                            modificacion=["cliente_regular","cliente_leal"]
                        elif modificacion=="3":
                            modificacion=["cliente_leal"]
                        else:
                            print("Debías ingresar un nivel entre los tres")
                            return datos_productos
                    elif objetivo=="precio" or objetivo=="unidades":
                        try:
                            modificacion=int(input(f"Actualmente {objetivo} tiene valor de "+str(i[objetivo])+" a que valor desea modificarlo: "))
                        except Exception:
                            print("*se intento ingresar un precio o unidades con valor no entero\n")
                            txt_fecha_actual("Se intento colocar en (funcion modificar productos) en valores (precio o unidades) un valor no entero")
                            return None
                    else:
                        print("Debías ingresar un objetivo valido (precio) (unidades) (nivel)")
                        return datos_productos

                    i[objetivo]=modificacion            
                    print(f"{objetivo} cambiado exitosamente")
                    return None
                
        except Exception:
            print("No se han ingresado productos")
            txt_fecha_actual("Se intento modificar productos de celulares y no se encontro alguno, ingresar productos primero")
            
        print("No se encontro tal nombre en nuestra lista de celulares")
        return None  
    else:
        print("Debías ingresar un producto valido, (celulares) o (audifonos)")
        txt_fecha_actual("En (agregar producto) en producto se ingreso un valor diferente a (celulares) y (audifonos)")

def eliminar_productos(datos_productos):
    ########### DEFINIR DATOS ###########
    datos_productos=dict(datos_productos)

    ########### OBTENER DATOS ###########
    producto=input("Deseas eliminar un producto de tipo (celulares) o (audifonos): ")
    #####################################
    if producto=="celulares":
        try:
            ###### MOSTRAR LOS PRODUCTOS QUE SE TIENEN DE CELULARES ########
            print("Actualmente hay estos celulares: ")
            print("*"*len("Actualmente hay estos celulares: "))
            for i in datos_productos[producto]:
                print("marca: "+i["marca"])
                print("nombre: "+i["nombre"])
                ###### ASTERISCOS DEL TAMAÑO DEL TEXTO #########
                print("*"*(len(i["nombre"])+8))
                ################################################

            nombre=input("Cual de esos celulares deseas eliminar? (escribe el nombre): ")


            for i in range(0,len(datos_productos[producto])):
                if datos_productos[producto][i]["nombre"]==nombre:
                    datos_productos[producto].pop(i)
                    guardar_datos(datos_productos,RUTA_PRODUCTOS)
                    return None
        except Exception:
            print("Aun no se han ingresado productos")
            txt_fecha_actual("Se debian haber ingresado productos antes (eliminar productos)")

        print("No se encontro tal nombre en nuestra lista de celulares")
        return None
            
    elif producto=="audifonos":
        try:
            ###### MOSTRAR LOS PRODUCTOS QUE SE TIENEN DE AUDIFONOS ########
            print("Actualmente hay estos audifonos: ")
            print("*"*len("Actualmente hay estos audifonos: "))
            for i in datos_productos[producto]:
                print("marca: "+i["marca"])
                print("nombre: "+i["nombre"])
                ###### ASTERISCOS DEL TAMAÑO DEL TEXTO #########
                print("*"*(len(i["nombre"])+8))
                ################################################

            nombre=input("Cual de esos audifonos deseas eliminar? (escribe el nombre): ")

            for i in range(0,len(datos_productos[producto])):
                if datos_productos[producto][i]["nombre"]==nombre:
                    datos_productos[producto].pop(i)
                    return datos_productos
                
            print("No se encontro tal nombre en nuestra lista de celulares")
            return None  
        except Exception:
            print("Aun no se han ingresado productos")
            txt_fecha_actual("Se debian haber ingresado productos antes (eliminar productos)")
    else:
        print("Debías ingresar un producto valido, (celulares) o (audifonos)")
        txt_fecha_actual("Se debía ingresar (celulares) o (audifonos)")
