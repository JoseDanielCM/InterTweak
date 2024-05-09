from funciones_usuarios import *
from funciones_servicios import *
from datos import *

RUTA_USUARIOS="usuarios.json"
RUTA_SERVICIOS="servicios.json"

datos_usuarios=traer_datos(RUTA_USUARIOS)
datos_servicio=traer_datos(RUTA_SERVICIOS)

while True:
    asignar_categoria_usuarios(datos_usuarios)
    guardar_datos(datos_usuarios,RUTA_USUARIOS)
    agregar_servicio(datos_servicio)

    guardar_datos(datos_servicio,RUTA_SERVICIOS)


