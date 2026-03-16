from agregar_producto import crear_producto, ver_productos
inventario = []
opcion = 1
while opcion < 4:
    print("Inventario de productos\n")
    print("Menu de opciones\n")
    print("1. Agregar producto\n")
    print("2. Ver productos\n")
    print("3. Actualizar producto\n")
    print("4. Eliminar producto\n")
    print("0. Salir\n")


opcion = input("Ingrese una opcion: \n")

if opcion == "1":
    crear_producto()
if opcion == "2":
    ver_productos()
