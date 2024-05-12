def agregar_producto(datos_productos):
    ########### DEFINIR DATOS ###########
    datos_productos=dict(datos_productos)

    ########### OBTENER DATOS ###########
    producto=input("Deseas agregar un producto de tipo (celulares) o (audifonos): ")
    #####################################
    if producto=="celulares":

        nombre=input("Ingresa el nombre del celular (sin la marca): ")
        marca=input("Ingresa la marca del celular: ")
        gb=int(input("Ingresa la capacidad de almacenamiento del celular,en gb: "))
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
            return datos_productos
        precio=int(input("Ingresa el precio del celular: "))
        unidades=int(input(f"Ingresa cuantas unidades hay de este celular {marca} {nombre}"))

    ########### AGREGAR DATOS ###########
        datos_productos[producto].append({"nombre":nombre,"marca":marca,"gb":gb,"nivel":nivel,"precio":precio,"unidades":unidades})
        return datos_productos
    
    elif producto=="audifonos":
        nombre=input("Ingresa el nombre del audifono (sin la marca): ")
        marca=input("Ingresa la marca del audifono: ")
        clase=input("Ingresa la clase de audifonos (inalambricos) o (cable): ")
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
            return datos_productos
        precio=input("Ingresa el precio del audifono: ")
        unidades=int(input(f"Ingresa cuantas unidades hay de estos audifonos {marca} {nombre}"))

    ########### AGREGAR DATOS ###########
        datos_productos[producto].append({"nombre":nombre,"marca":marca,"clase":clase,"nivel":nivel,"precio":precio,"unidades":unidades})
        return datos_productos
    else:
        print("Debías ingresar un producto valido, (celulares) o (audifonos)")
        return datos_productos
    
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
                    objetivo=int(input(f"Actualmente {objetivo} tiene valor de "+str(i[objetivo])+" a que valor desea modificarlo: "))
                else:
                    print("Debías ingresar un objetivo valido (precio) (unidades) (nivel)")
                    return datos_productos

                i[objetivo]=modificacion
                print(i[objetivo])
                print(f"{objetivo} cambiado exitosamente")
                return datos_productos
            
        print("No se encontro tal nombre en nuestra lista de celulares")
        return datos_productos
            
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
                    objetivo=int(input(f"Actualmente {objetivo} tiene valor de "+str(i[objetivo])+" a que valor desea modificarlo: "))
                else:
                    print("Debías ingresar un objetivo valido (precio) (unidades) (nivel)")
                    return datos_productos

                i[objetivo]=modificacion            
                print(f"{objetivo} cambiado exitosamente")
                return datos_productos
            
        print("No se encontro tal nombre en nuestra lista de celulares")
        return datos_productos  
    else:
        print("Debías ingresar un producto valido, (celulares) o (audifonos)")

def eliminar_productos(datos_productos):
    ########### DEFINIR DATOS ###########
    datos_productos=dict(datos_productos)

    ########### OBTENER DATOS ###########
    producto=input("Deseas eliminar un producto de tipo (celulares) o (audifonos): ")
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

        nombre=input("Cual de esos celulares deseas eliminar? (escribe el nombre): ")

        for i in range(0,len(datos_productos[producto])):
            if datos_productos[producto][i]["nombre"]==nombre:
                datos_productos[producto].pop(i)
                return datos_productos
            
        print("No se encontro tal nombre en nuestra lista de celulares")
        return datos_productos
            
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

        nombre=input("Cual de esos audifonos deseas eliminar? (escribe el nombre): ")

        for i in range(0,len(datos_productos[producto])):
            if datos_productos[producto][i]["nombre"]==nombre:
                datos_productos[producto].pop(i)
                return datos_productos
            
        print("No se encontro tal nombre en nuestra lista de celulares")
        return datos_productos  
    else:
        print("Debías ingresar un producto valido, (celulares) o (audifonos)")