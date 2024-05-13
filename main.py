from funciones_usuarios import *
from funciones_servicios import *
from funciones_productos import *
from funciones_reportes import *
from funciones_ventas import realizar_venta, promocion_usuario
from menu import *
from datos import *

RUTA_USUARIOS="usuarios.json"
RUTA_SERVICIOS="servicios.json"
RUTA_PRODUCTOS="productos.json"

datos_usuarios = traer_datos(RUTA_USUARIOS)
datos_servicio = traer_datos(RUTA_SERVICIOS)
datos_productos = traer_datos(RUTA_PRODUCTOS)

while True:
    menu_modulos()
    opc=pedir_opcion()
    if opc==1:
        mod_usuario()
    elif opc==2:
        mod_servicios()
    elif opc==3:
        mod_servicios()
    elif opc==4:
        mod_ventas()
    elif opc==5:
        mod_reportes()
    elif opc==6:
        mod_mas_opciones()
    elif opc==7:
        print("Saliste exitosamente")
        break
    else:
        print("Ingresa una opcion valida, ")



