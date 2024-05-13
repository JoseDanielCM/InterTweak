from funciones_ventas import promocion_usuario,realizar_venta
from funciones_interaciones import *
from funciones_usuarios import *
from funciones_servicios import *
from funciones_productos import *
from funciones_reportes import *
from datos import *

RUTA_USUARIOS="usuarios.json"
RUTA_SERVICIOS="servicios.json"
RUTA_PRODUCTOS="productos.json"
RUTA_SERVICIO_CLIENTE="servicio_cliente.json"
RUTA_SUGERENCIAS="sugerencias.json"
RUTA_RECLAMACIONES="reclamaciones.json"

def menu_modulos():
    print("***************************************")
    print("Digite a que menu desea ingresar")
    print("1. para modulo de usuarios")
    print("2. para modulo de gestion de servicios")
    print("3. para modulo de gestion de productos")
    print("4. para modulo de ventas")
    print("5. para modulo de reportes")
    print("6. para modulo de interacciones con el usuario")
    print("7. para salir")
    print("***************************************")
    
def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("***************************************")
        return opc
    except Exception:
        print("***************************************")
        return -1

def mod_usuario():
    datos_usuario = traer_datos(RUTA_USUARIOS)

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
            agregar_usuario(datos_usuario)
        elif opc==2:
            eliminar_usuario(datos_usuario)
        elif opc==3:
            modificar_usuarios(datos_usuario)
        elif opc==4:
            asignar_categoria_usuarios(datos_usuario)
        elif opc==5:
            print("Regresaste a menu prinipal")
            break
        else:
            print("Ingresa una opcion valida, ")

def mod_servicios():
    datos_servicio = traer_datos(RUTA_SERVICIOS)

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
            agregar_servicio(datos_servicio)

        elif opc==2:
            eliminar_servicios(datos_servicio)

        elif opc==3:
            modificar_servicios(datos_servicio)

        elif opc==4:
            print("Regresaste a menu prinipal")
            break
        else:
            print("Ingresa una opcion valida, ")

def mod_productos():
    datos_producto=traer_datos(RUTA_PRODUCTOS)

    while True:
        print("Digite a que sub-menú de usuarios desea ingresar")
        print("1. para agregar un producto")
        print("2. para eliminar un producto")
        print("3. para modificar datos de un producto")
        print("4. para volver al menú principal")
        print("***************************************")
        opc=pedir_opcion()
        if opc==1:
            agregar_producto(datos_producto)
        elif opc==2:
            eliminar_productos(datos_producto)
        elif opc==3:
            modificar_productos(datos_producto)
        elif opc==4:
            print("Regresaste a menu prinipal")
            break
        else:
            print("Ingresa una opcion valida, ")

def mod_reportes():
    datos_servicios=traer_datos(RUTA_SERVICIOS)
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
            productos_clientes()
        elif opc==2:
            productos_ya_vendidos()
        elif opc==3:
            servicios_populares(datos_servicios)
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
            if promocion!=None:
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
        print("1. realizar una consulta de servicio al cliente ")
        print("2. realizar una reclamacion")
        print("3. realizar una sugerencia")
        print("************************************************************")
        print("4. si se desea responder una consulta de servicio al cliente")
        print("5. si se desea responder una reclamacion")
        print("6. si se desea leer las sugerencias")
        print("7. para volver al menú principal")
        print("***************************************")
        opc=pedir_opcion()
        if opc==1:
            servicio_cliente()
        elif opc==2:
            reclamacion()
        elif opc==3:
            sugerencia()
        elif opc==4:
            responder_servicio_cliente()
        elif opc==5:
            responder_reclamacion()
        elif opc==6:
            responder_sugerencia()
        elif opc==7:
            print("Regresaste a menu prinipal")
            break
        else:
            print("Ingresa una opcion valida, ")
