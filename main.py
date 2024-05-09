from funciones_usuarios import *
from datos import *

RUTA_USUARIOS="usuarios.json"

datos=traer_datos(RUTA_USUARIOS)


modificar_usuarios(datos)
guardar_datos(datos,RUTA_USUARIOS)