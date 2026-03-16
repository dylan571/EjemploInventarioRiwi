productos = []

def crear_producto():
    nombre = input("Ingrese el nombre del producto: \n")
    while True:
        precio = float(input("Ingrese el precio del producto: \n"))
        if precio <= 0:
            print("Entrada no valida, ingrese un numero valido...")
            continue
        break
    while True:
        cantidad = int(input("Ingrese la cantidad del producto: \n"))
        if cantidad <= 0:
            print("Entrada no valida, ingrese un numero valido...")
            continue
        break
    productos.append(
        {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    )
    print(
        f"Producto agregado exitosamente, Nombre: {nombre}, Precio: {precio}, Cantidad: {cantidad}"
    )

def ver_productos():
    print(productos)