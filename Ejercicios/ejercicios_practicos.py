# Importamos la librería math para usar funciones matemáticas
import math

# =========================================================
# Ejercicio 1
# =========================================================
print("Ejercicio 1")

# Variables con datos del estudiante
nombre = "David"
valor = 3
promedio = 3.1

# Mostramos la información usando f-string
print(f"{nombre} su nota es {valor} y su promedio es {promedio}")
print("")

# =========================================================
# Ejercicio 2
# =========================================================
print("Ejercicio 2")

# Pedimos dos números enteros al usuario
variable_entero_uno = int(input("Ingrese un número entero: "))
variable_entero_dos = int(input("Ingrese un número entero: "))

# Pedimos un número decimal
variable_float = float(input("Ingrese un número flotante: "))

# Pedimos dos cadenas de texto
variable_string_uno = input("Ingrese una cadena de texto: ")
variable_string_dos = input("Ingrese una cadena de texto: ")

# Sumamos los dos enteros y el número flotante
suma_numeros = float(variable_entero_uno + variable_entero_dos + variable_float)

# Mostramos el resultado de la suma
print(f"La suma de los 3 números es: {suma_numeros}")

# Validamos cuál entero es mayor
if variable_entero_uno > variable_entero_dos:
    print(f"Este es el entero mayor {variable_entero_uno}")

elif variable_entero_dos > variable_entero_uno:
    print(f"Este es el entero mayor {variable_entero_dos}")

# Si ambos son iguales mostramos este mensaje
else:
    print(f"El número {variable_entero_dos} y el número {variable_entero_uno} son iguales")

# Realizamos una operación matemática con división
print(f"La división del float con el resto de la división de los dos enteros es: {(variable_entero_uno / variable_entero_dos) / variable_float}")

# Concatenamos las cadenas de texto
print(f"Estas dos son cadenas de texto {variable_string_uno}{variable_string_dos}")

print("")

# =========================================================
# Ejercicio 3
# =========================================================
print("Ejercicio 3")

# Variables de base y exponente
base = 4
exponente = 5

# Calculamos la potencia
print(f"La potencia de {base} y {exponente} es {base ** exponente}")

print("")

# =========================================================
# Ejercicio 4
# =========================================================
print("Ejercicio 4")

# Variables con números para calcular raíces cuadradas
numero_a = 2
numero_b = 8
numero_c = 9
numero_d = 27
numero_e = 28
numero_f = 55
numero_g = 121

# Calculamos y mostramos las raíces cuadradas
print("Raíz cuadrada de 2:", math.sqrt(numero_a))
print("Raíz cuadrada de 8:", math.sqrt(numero_b))
print("Raíz cuadrada de 9:", math.sqrt(numero_c))
print("Raíz cuadrada de 27:", math.sqrt(numero_d))
print("Raíz cuadrada de 28:", math.sqrt(numero_e))
print("Raíz cuadrada de 55:", math.sqrt(numero_f))
print("Raíz cuadrada de 121:", math.sqrt(numero_g))

# =========================================================
# Ejercicio 5
# =========================================================
print("Ejercicio 5")

# Nombre del estudiante
nombre_estudiante = "Carlos"

# Notas del estudiante
nota_uno = 4.5
nota_dos = 3.8
nota_tres = 4.2
nota_cuatro = 5.0
nota_cinco = 4.7

# Calculamos el promedio
promedio = (nota_uno + nota_dos + nota_tres + nota_cuatro + nota_cinco) / 5

# Mostramos resultados
print("Nombre del estudiante:", nombre_estudiante)
print("Promedio final:", promedio)

# Verificamos si aprueba o reprueba
if promedio >= 3.0:
    print("El estudiante aprobó.")
else:
    print("El estudiante reprobó.")

# =========================================================
# Ejercicio 6
# =========================================================
print("Ejercicio 6")

# Convertimos números flotantes a enteros
numero_uno = int(8.3)
numero_dos = int(2.1)

# Mostramos los valores originales
print("Valores originales:")
print("numero_uno =", numero_uno)
print("numero_dos =", numero_dos)

# Intercambiamos los valores usando una variable auxiliar
auxiliar = numero_uno
numero_uno = numero_dos
numero_dos = auxiliar

# Mostramos los valores intercambiados
print("Valores intercambiados:")
print("numero_uno =", numero_uno)
print("numero_dos =", numero_dos)

# =========================================================
# Ejercicio 7
# =========================================================
print("Ejercicio 7")

# Evaluamos una expresión lógica
estado = (5 == 2) or (2 > 1)

# Mostramos el resultado booleano
print("El valor de estado es:", estado)

# =========================================================
# Ejercicio 8
# =========================================================
print("Ejercicio 8")

# Realizamos una operación matemática combinada
resultado = (9 / 3) + (8 * 2) - (5 + 1) + (10 % 3) + (2 ** 3)

# Mostramos el resultado
print("El resultado de la operación es:", resultado)

# =========================================================
# Ejercicio 9
# =========================================================
print("Ejercicio 9")

# -----------------------------
# Cuadrado
# -----------------------------

# Lado del cuadrado
lado_cuadrado = 8

# Fórmulas del cuadrado
area_cuadrado = lado_cuadrado * lado_cuadrado
perimetro_cuadrado = lado_cuadrado * 4

# Mostramos resultados
print("Área del cuadrado:", area_cuadrado)
print("Perímetro del cuadrado:", perimetro_cuadrado)

# -----------------------------
# Triángulo
# -----------------------------

# Datos del triángulo
base_triangulo = 9
altura_triangulo = 8
lado_uno_triangulo = 8
lado_dos_triangulo = 8

# Fórmulas del triángulo
area_triangulo = (base_triangulo * altura_triangulo) / 2
perimetro_triangulo = base_triangulo + lado_uno_triangulo + lado_dos_triangulo

# Mostramos resultados
print("Área del triángulo:", area_triangulo)
print("Perímetro del triángulo:", perimetro_triangulo)

# -----------------------------
# Rectángulo
# -----------------------------

# Datos del rectángulo
base_rectangulo = 8
altura_rectangulo = 6

# Fórmulas del rectángulo
area_rectangulo = base_rectangulo * altura_rectangulo
perimetro_rectangulo = 2 * (base_rectangulo + altura_rectangulo)

# Mostramos resultados
print("Área del rectángulo:", area_rectangulo)
print("Perímetro del rectángulo:", perimetro_rectangulo)

# =========================================================
# Ejercicio 10
# =========================================================
print("Ejercicio 10")

# Edad de la persona
edad = 22

# Clasificamos la edad según el rango
if edad >= 0 and edad <= 5:
    categoria = "Infante"

elif edad >= 6 and edad <= 10:
    categoria = "Niño"

elif edad >= 11 and edad <= 15:
    categoria = "Pre adolescente"

elif edad >= 16 and edad <= 18:
    categoria = "Adolescente"

elif edad >= 19 and edad <= 25:
    categoria = "Pre adulto"

elif edad >= 26 and edad <= 40:
    categoria = "Adulto"

elif edad >= 41 and edad <= 55:
    categoria = "Pre anciano"

# Si no cumple ninguna condición anterior será anciano
else:
    categoria = "Anciano"

# Mostramos resultados
print("Edad:", edad)
print("Categoría:", categoria)