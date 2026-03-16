productos = []

print("Inventario de productos\n")
print("Menu de opciones\n")
print("1. Agregar producto\n")
print("2. Ver productos\n")
print("3. Actualizar producto\n")
print("4. Eliminar producto\n")
print("0. Salir\n")

opcion = input("Ingrese una opcion: \n")

#pedir nombre precio y cantidad del producto
if opcion == "1":
    nombre = input("Ingrese el nombre del producto: \n")
    precio = float(input("Ingrese el precio del producto: \n"))
    cantidad = int(input("Ingrese la cantidad del producto: \n"))
    total = precio * cantidad
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad, "total": total})
    print(f"Producto agregado exitosamente, Nombre: {nombre}, Precio: {precio}, Cantidad: {cantidad}, Total: {total}")
