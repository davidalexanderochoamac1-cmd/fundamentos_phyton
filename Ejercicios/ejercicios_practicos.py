import math

# Ejercicio 1

nombre = "David"
valor = 3
promedio = 3.1

print(f"{nombre} su nota es {valor} y su promedio es {promedio}")
print("")

# Ejercicio 2

variable_entero_uno = int(input("Ingrese un número entero: "))
variable_entero_dos = int(input("Ingrese un número entero: "))

variable_float = float(input("Ingrese un número flotante: "))

variable_string_uno = input("Ingrese una cadena de texto: ")
variable_string_dos = input("Ingrese una cadena de texto: ")

suma_numeros = float(variable_entero_uno + variable_entero_dos + variable_float)

print(f"La suma de los 3 números es: {suma_numeros}")

if variable_entero_uno > variable_entero_dos:
    print(f"Este es el entero mayor {variable_entero_uno}")

elif variable_entero_dos > variable_entero_uno:
    print(f"Este es el entero mayor {variable_entero_dos}")

else:
    print(f"El número {variable_entero_dos} y el número {variable_entero_uno} son iguales")

print(f"La división del float con el resto de la división de los dos enteros es: {(variable_entero_uno / variable_entero_dos) / variable_float}")

print(f"Estas dos son cadenas de texto {variable_string_uno}{variable_string_dos}")

print("")

# Ejercicio 3

base = 3
exponente = 5

print(f"La potencia de {base} y {exponente} es {base ** exponente}")

print("")

# Ejercicio 4

numero_a = 2
numero_b = 8
numero_c = 9
numero_d = 27
numero_e = 28
numero_f = 55
numero_g = 121

print("Raíz cuadrada de 2:", math.sqrt(numero_a))
print("Raíz cuadrada de 8:", math.sqrt(numero_b))
print("Raíz cuadrada de 9:", math.sqrt(numero_c))
print("Raíz cuadrada de 27:", math.sqrt(numero_d))
print("Raíz cuadrada de 28:", math.sqrt(numero_e))
print("Raíz cuadrada de 55:", math.sqrt(numero_f))
print("Raíz cuadrada de 121:", math.sqrt(numero_g))

# Ejercicio 5

nombre_estudiante = "Carlos"

nota_uno = 4.5
nota_dos = 3.8
nota_tres = 4.2
nota_cuatro = 5.0
nota_cinco = 4.7

promedio = (nota_uno + nota_dos + nota_tres + nota_cuatro + nota_cinco) / 5

print("Nombre del estudiante:", nombre_estudiante)
print("Promedio final:", promedio)

if promedio >= 3.0:
    print("El estudiante aprobó.")
else:
    print("El estudiante reprobó.")

# Ejercicio 6

numero_uno = int(8.3)
numero_dos = int(2.1)

print("Valores originales:")
print("numero_uno =", numero_uno)
print("numero_dos =", numero_dos)

auxiliar = numero_uno
numero_uno = numero_dos
numero_dos = auxiliar

print("Valores intercambiados:")
print("numero_uno =", numero_uno)
print("numero_dos =", numero_dos)

# Ejercicio 7

estado = (5 == 2) or (2 > 1)

print("El valor de estado es:", estado)

# Ejercicio 8

resultado = (9 / 3) + (8 * 2) - (5 + 1) + (10 % 3) + (2 ** 3)

print("El resultado de la operación es:", resultado)

# Ejercicio 9

lado_cuadrado = 8

area_cuadrado = lado_cuadrado * lado_cuadrado
perimetro_cuadrado = lado_cuadrado * 4

print("Área del cuadrado:", area_cuadrado)
print("Perímetro del cuadrado:", perimetro_cuadrado)

base_triangulo = 9
altura_triangulo = 8
lado_uno_triangulo = 8
lado_dos_triangulo = 8

area_triangulo = (base_triangulo * altura_triangulo) / 2
perimetro_triangulo = base_triangulo + lado_uno_triangulo + lado_dos_triangulo

print("Área del triángulo:", area_triangulo)
print("Perímetro del triángulo:", perimetro_triangulo)

base_rectangulo = 8
altura_rectangulo = 6

area_rectangulo = base_rectangulo * altura_rectangulo
perimetro_rectangulo = 2 * (base_rectangulo + altura_rectangulo)

print("Área del rectángulo:", area_rectangulo)
print("Perímetro del rectángulo:", perimetro_rectangulo)

# Ejercicio 10

edad = 22

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

else:
    categoria = "Anciano"

print("Edad:", edad)
print("Categoría:", categoria)