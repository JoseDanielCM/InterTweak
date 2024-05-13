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

menu_principal()



