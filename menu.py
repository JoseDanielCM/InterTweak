def menu_principal():
    print("***************************************")
    print("Ingrese a que menu desea ingresar")
    print("1. para modulo de usuarios")
    print("2. para modulo de gestion de servicios")
    print("3. para modulo de reportes")
    print("4. para modulo de ventas")
    print("5. para salir")
    print("***************************************")
    
def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("***************************************")
        return opc
    except Exception:
        print("Valor inválido")
        print("***************************************")
        return -1
    
def mod_usuario():
    print("")

def mod_servicios():
    None

def mod_resportes():
    None

def mod_ventas():
    None