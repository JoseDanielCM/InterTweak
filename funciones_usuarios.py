def agregar_usuario(datos):
    datos=list(datos)
    nombre=input("Ingresa el nombre del usuario: ")
    documento=input("Ingresa el documento del usuario: ")
    edad=input("Ingresa la edad del usuario: ")
    telefono=input("Ingresa el telefono del usuario: ")
    correo=input("Ingresa el correo del usuario: ")
    datos.append({"nombre":nombre,"documento":documento,"edad":edad,"telefono":telefono,"correo":correo,"categoria":{"nuevo_cliente":True,"cliente_regular":False,"cliente_leal":False}})
    return datos

def modificar_usuarios(datos):
    datos=list(datos)
    print("los datos que se tienen de los usuarios son los siguientes: ")
    for i in datos[0]:
        if i!="categoria":
            print(i)
    opcion=input("Que parametro deseas modificar?")
