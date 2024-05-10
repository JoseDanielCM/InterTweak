from funciones_usuarios import *
from funciones_servicios import *
from funciones_productos import *
from menu import *
from datos import *

RUTA_USUARIOS="usuarios.json"
RUTA_SERVICIOS="servicios.json"
RUTA_PRODUCTOS="productos.json"

datos_usuarios=traer_datos(RUTA_USUARIOS)
datos_servicio=traer_datos(RUTA_SERVICIOS)
datos_productos=traer_datos(RUTA_PRODUCTOS)

eliminar_productos(datos_productos)
guardar_datos(datos_productos,RUTA_PRODUCTOS)

while False:
    menu_principal()
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
        print("Saliste exitosamente")
    else:
        print("Ingresa una opcion valida, ")
    agregar_servicio(datos_servicio)
    guardar_datos(datos_servicio,RUTA_SERVICIOS)


