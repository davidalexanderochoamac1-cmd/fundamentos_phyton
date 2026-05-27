# Actividad 1: Inventario de la Tienda Escolar

# Lista de productos
productos = [
    "Cuaderno",
    "Lapicero",
    "Borrador",
    "Regla",
    "Mochila",
    "Calculadora"
]

# Lista de precios
precios = [2.50, 0.75, 1.00, 1.50, 25.00, 15.00]

# Lista de cantidades disponibles
cantidades = [100, 150, 80, 60, 134, 55]

# Imprimir listas completas
print("Imprimir las listas completas\n")

print(
    "\nProductos:", productos,
    "\nPrecios:", precios,
    "\nCantidades:", cantidades,
    "\nCantidad de productos en el inventario:", len(productos),
    "\n"
)

# Mostrar información de cada producto
print("Impresion por producto\n")

print(f"El producto {productos[0]} tiene un precio de ${precios[0]} y hay {cantidades[0]} unidades disponibles.\n")
print(f"El producto {productos[1]} tiene un precio de ${precios[1]} y hay {cantidades[1]} unidades disponibles.\n")
print(f"El producto {productos[2]} tiene un precio de ${precios[2]} y hay {cantidades[2]} unidades disponibles.\n")
print(f"El producto {productos[3]} tiene un precio de ${precios[3]} y hay {cantidades[3]} unidades disponibles.\n")
print(f"El producto {productos[4]} tiene un precio de ${precios[4]} y hay {cantidades[4]} unidades disponibles.\n")
print(f"El producto {productos[5]} tiene un precio de ${precios[5]} y hay {cantidades[5]} unidades disponibles.\n")

# Mostrar tipos de datos
print("Mostrar el tipo de dato de la lista y del primer elemento\n")

print("El tipo de dato de la lista productos es:", type(productos))
print("El tipo de dato del primer elemento de productos es:", type(productos[0]), "\n")

print("El tipo de dato de la lista precios es:", type(precios))
print("El tipo de dato del primer elemento de precios es:", type(precios[0]), "\n")

print("El tipo de dato de la lista cantidades es:", type(cantidades))
print("El tipo de dato del primer elemento de cantidades es:", type(cantidades[0]))

# type(lista) muestra el tipo de la estructura completa.
# type(lista[0]) muestra el tipo del elemento almacenado.