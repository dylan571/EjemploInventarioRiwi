import csv
import os

productos = []

def crear_producto():
    nombre = input("Ingrese el nombre del producto: \n").upper()
    print()
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: \n"))
            print()
            if precio <= 0:
                print("Entrada no valida, ingrese un numero valido...")
                continue
            break
        except ValueError:
            print("Entrada no valida, ingrese un valor valido (numeros)")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: \n"))
            print()
            if cantidad <= 0:
                print("Entrada no valida, ingrese un numero valido...")
                continue
            break
        except ValueError:
            print("Entrada no valida, ingrese un valor valido (numeros)")

    productos.append(
        {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    )
    guardar_csv()
    #limpiar pantalla os.system("cls")
    print(f"Producto '{nombre}' agregado y guardado en el archivo.")

def ver_productos():
    if len(productos) == 0:
        print("No hay datos para mostrar")
        print()
    else:
        print("Lista de productos:")
        for i, producto in enumerate(productos):
            print(f"{i + 1}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")
    print()

def actualizar_producto():
    if len(productos) == 0:
        print("No hay productos para actualizar\n")
        return

    print("Lista de productos:")
    for i, producto in enumerate(productos):
        print(f"{i + 1}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")
    print()

    while True:
        try:
            opcion = int(input("Seleccione el número del producto a actualizar: "))
            if opcion < 1 or opcion > len(productos):
                raise ValueError
            break
        except ValueError:
            print("Entrada inválida, intente nuevamente\n")

    producto = productos[opcion - 1]

    print(f"\nActualizando producto: {producto['nombre']}")

    # Nuevo nombre
    nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ").upper()
    if nuevo_nombre != "":
        producto['nombre'] = nuevo_nombre

    # Nuevo precio
    while True:
        try:
            nuevo_precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            if nuevo_precio == "":
                break
            nuevo_precio = float(nuevo_precio)
            if nuevo_precio <= 0:
                raise ValueError
            producto['precio'] = nuevo_precio
            break
        except ValueError:
            print("Precio inválido")

    # Nueva cantidad
    while True:
        try:
            nueva_cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            if nueva_cantidad == "":
                break
            nueva_cantidad = int(nueva_cantidad)
            if nueva_cantidad <= 0:
                raise ValueError
            producto['cantidad'] = nueva_cantidad
            break
        except ValueError:
            print("Cantidad inválida")
    guardar_csv()
    print("\nProducto actualizado correctamente\n")

def eliminar_producto():
    if len(productos) == 0:
        print("No hay productos para eliminar. \n")
        print()
        return
    
    print("Lista de productos:")
    for i, producto in enumerate(productos):
        print(f"{i + 1}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")
    print()

    while True:
        try:
            opcion = int(input("Seleccione el número del producto a eliminar: "))
            if opcion < 1 or opcion > len(productos):
                raise ValueError
            break
        except ValueError:
            print("Entrada inválida, intente nuevamente\n")

    producto = productos[opcion - 1]

    print(f"\nEliminando producto: {producto['nombre']}")

    confirmar = input("¿Seguro que deseas eliminar este producto? (s/n): ")

    if confirmar.lower() == "s":
        productos.pop(opcion - 1)
        guardar_csv()
        print("Producto eliminado correctamente \n")
        print("Lista de productos:")
        for i, producto in enumerate(productos):
            print(f"{i + 1}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")
        print()
    else:
        print("Operacion cancelada. \n")
        print("Lista de productos:")
        for i, producto in enumerate(productos):
            print(f"{i + 1}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")
        print()

def calcular_inventario():
    if len(productos) == 0:
        print("No hay productos para calcular. \n")
        print()
    else:
        producto_mas_caro = None
        producto_mayor_stock = None
        valor_total_sumado = 0
        cantidad_de_productos = 0
        print("Lista de productos:")
        for i, producto in enumerate(productos):
            if producto_mas_caro is None or producto["precio"] > producto_mas_caro["precio"]:
                producto_mas_caro = producto
            if producto_mayor_stock is None or producto["cantidad"] > producto_mayor_stock["cantidad"]: 
                producto_mayor_stock = producto
            valor_total_sumado += producto["precio"] * producto["cantidad"]
            cantidad_de_productos += producto["cantidad"]
            print(f"{i + 1}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']} - Subtotal: {producto["precio"] * producto["cantidad"]}")
    print(f"\nTotal del inventario:, {valor_total_sumado}")
    print("Cantidad total de productos:", cantidad_de_productos)
    print("\nProductos con mas stock:")
    print(f"{producto_mayor_stock["nombre"]} - Cantidad: {producto_mayor_stock["cantidad"]}")
    print("\nProducto mas caro:")
    print(f"{producto_mas_caro["nombre"]} - Precio: {producto_mas_caro["precio"]}")
    
def guardar_csv():
    nombre_archivo = "data/inventario.csv"
    campos = ["nombre", "precio", "cantidad"]

    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        escritor.writerows(productos)

    print(f"Datos guardados con exito en {nombre_archivo}")
    
def cargar_csv():
    lista_temporal = []
    nombre_archivo = "data/inventario.csv"

    if os.path.exists(nombre_archivo):
    
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                fila["precio"] = float(fila["precio"])
                fila["cantidad"] = int(fila["cantidad"])
                lista_temporal.append(fila)
        global productos
        productos = lista_temporal      
        print("Productos cargados.")
    else:
        print("No se encontro el archivo. Iniciando inventario vacio.")
    return []

def buscar_producto(productos, nombre):
    objetivo = nombre.strip().upper()
    for busqueda in productos:
        if busqueda["nombre"].strip().upper() == objetivo:
            return busqueda
    return None