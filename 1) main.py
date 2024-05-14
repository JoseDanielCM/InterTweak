from menu import *

RUTA_USUARIOS="usuarios.json"
RUTA_SERVICIOS="servicios.json"
RUTA_PRODUCTOS="productos.json"

print("Bienvenido, cualquier duda ingresa a la opcion 6 (mas opciones) y escribela en el modulo correspondiente")

while True: 
    menu_modulos()
    opc=pedir_opcion()
    if opc==1:
        mod_usuario()
    elif opc==2:
        mod_servicios()
    elif opc==3:
        mod_productos()
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
        print("Ingresa una opcion valida")



