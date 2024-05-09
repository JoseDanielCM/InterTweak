from funciones_usuarios import *
from funciones_servicios import *
from datos import *

RUTA_USUARIOS="usuarios.json"

datos=traer_datos(RUTA_USUARIOS)

while True:
    datos=agregar_usuario(datos)

    guardar_datos(datos,RUTA_USUARIOS)


