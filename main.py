from menu import *

RUTA_USUARIOS="usuarios.json"
RUTA_SERVICIOS="servicios.json"
RUTA_PRODUCTOS="productos.json"

print("Para el correcto funcionamiento cuando se vayan a ingresar nuevos servicios el identificador debe comenzar con:")
print("INTERNET: (C para cable) (F para fibra optica) (S para satelital)")
print("PLANES: (PR para prepago) (PT para pospago)")
print("luego de las siglas se agrega un numero si es menor a diez agregarle un cero al inicio EJ (C06) , (PR15)")

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



