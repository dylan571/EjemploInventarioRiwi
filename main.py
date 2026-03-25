from src.funciones import (cargar_csv, 
        crear_producto, 
        ver_productos, 
        actualizar_producto, 
        eliminar_producto, 
        calcular_inventario,
        guardar_csv
        )
opcion = 1
while opcion != 0:
    print("\nInventario de productos\n")
    print("Menu de opciones\n")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Calcular inventario")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Cargar CSV")
    print("7. Guardar CSV")
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
    if opcion == 6:
        cargar_csv()
    if opcion == 7:
        guardar_csv()
    


