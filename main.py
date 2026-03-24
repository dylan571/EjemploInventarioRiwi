from agregar_producto import (crear_producto, 
        ver_productos, 
        actualizar_producto, 
        eliminar_producto, 
        calcular_inventario
        )
inventario = []
opcion = 1
while opcion != 0:
    print("\nInventario de productos\n")
    print("Menu de opciones\n")
    print("1. Agregar producto\n")
    print("2. Ver productos\n")
    print("3. Calcular inventario\n")
    print("4. Actualizar producto\n")
    print("5. Eliminar producto\n")
    print("0. Salir\n")

    while True:
        try:
            opcion = int(input("Ingrese una opcion: \n"))
            if opcion < 0:
                raise ValueError("Entrada erronea ingrese una opcion del menu: \n")
            break
        except ValueError:
            print("Entrada erronea ingrese una opcion del menu: \n")
    
    if opcion == 1:
        crear_producto()
    if opcion == 2:
        ver_productos()
    if opcion == 3:
        calcular_inventario()
    if opcion == 4:
        actualizar_producto()
    if opcion == 5:
        eliminar_producto()
    


