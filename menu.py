from funciones_ventas import promocion_usuario,realizar_venta
from funciones_interaciones import *

def menu_principal():
    while True:
        menu_modulos()
        opc=pedir_opcion()
        if opc==1:
            mod_usuario()
        elif opc==2:
            mod_servicios()
        elif opc==3:
            mod_ventas()
        elif opc==4:
            mod_reportes()
        elif opc==5:
            print("Saliste exitosamente")
            break
        else:
            print("Ingresa una opcion valida, ")

def menu_modulos():
    print("***************************************")
    print("Digite a que menu desea ingresar")
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
    while True:
        print("Digite a que sub-menú de usuarios desea ingresar")
        print("1. para agregar a un usuarios")
        print("2. para eliminar a  un usuarios")
        print("3. para modificar datos de un usuarios")
        print("4. para asignar una categoria a un usuarios")
        print("5. para volver al menú principal")
        print("***************************************")
        opc=pedir_opcion()
        if opc==1:
            print("MODULO USUARIOS")
        elif opc==2:
            print("MODULO SERVICIOS")
        elif opc==3:
            print("MODULO REPORTES")
        elif opc==4:
            print("MODULO VENTAS")
        elif opc==5:
            print("Regresaste a menu prinipal")
            break
        else:
            print("Ingresa una opcion valida, ")

def mod_servicios():
    while True:
        print("MODULO SERVICIOS")
        print("Digite a que sub-menú de servicios desea ingresar")
        print("1. para agregar un servicio")
        print("2. para eliminar un servicio")
        print("3. para modificar datos de un servicio")
        print("4. para volver al menú principal")
        print("***************************************")
        opc=pedir_opcion()
        if opc==1:
            print("MODULO USUARIOS")
        elif opc==2:
            print("MODULO SERVICIOS")
        elif opc==3:
            print("MODULO REPORTES")
        elif opc==4:
            print("Regresaste a menu prinipal")
            break
        else:
            print("Ingresa una opcion valida, ")

def mod_reportes():
    while True:
        print("MODULO DE SERVICIOS")
        print("Digite a que sub-menú de servicios desea ingresar")
        print("1. para realizar un reporte de, con cada producto, cuales clientes lo han comprado")
        print("2. para realizar un reporte de los productos que ya han tenido ventas")
        print("3. para realizar un reporte de los productos más populares / con más ventas")
        print("4. para volver al menú principal")
        print("***************************************")
        opc=pedir_opcion()
        if opc==1:
            print("MODULO USUARIOS")
        elif opc==2:
            print("MODULO SERVICIOS")
        elif opc==3:
            print("MODULO REPORTES")
        elif opc==4:
            print("Regresaste a menu prinipal")
            break
        else:
            print("Ingresa una opcion valida, ")

def mod_ventas():
    while True:
        print("MODULO DE VENTAS")
        print("Digite (1) para realizar una venta")
        print("Digite (2) para salir y regresar al menú principal")
        print("***************************************")
        opc=pedir_opcion()
        if opc==1:
            promocion=promocion_usuario()
            realizar_venta(promocion)
        elif opc==2:
            print("Regresaste a menu prinipal")
            break
        else:
            print("Ingresa una opcion valida, ")
    
def mod_mas_opciones():
    user="admin"
    password="admin123"
    while True:
        print("MODULO OPCIONES EXTRA")
        print("Digite a que sub-menú de otras opciones desea ingresar")
        print("1. si el cliente desea realizar una consulta de servicio al cliente ")
        print("2. si el cliente desea realizar una reclamacion")
        print("3. si el cliente desea realizar una sugerencia")
        print("***************************************")
        print("4. si se desea responder una consulta de servicio al cliente")
        print("5. si se desea responder una reclamacion")
        print("6. si se desea leer las sugerencias")
        print("7. para volver al menú principal")
        print("***************************************")
        opc=pedir_opcion()
        if opc==1:
            print("MODULO USUARIOS")
        elif opc==2:
            print("MODULO SERVICIOS")
        elif opc==3:
            print("MODULO REPORTES")
        elif opc==4:
            print("MODULO REPORTES")
        elif opc==5:
            print("MODULO REPORTES")
        elif opc==6:
            print("MODULO REPORTES")
        elif opc==7:
            print("Regresaste a menu prinipal")
            break
        else:
            print("Ingresa una opcion valida, ")

    user="admin"
    password="admin123"
    intento_user=input("Para acceder a responder las preguntas, escribe el usuario: ")
    intento_password=input("Ingresa la contraseña: ")