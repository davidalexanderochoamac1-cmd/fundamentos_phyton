import math

#Ejercicio 1

nombre = "David"
valor = 3
promedio = 3.1

print (f"{nombre} su nota es {valor} y su promedio es {promedio} ")
print("")

#Ejercicio 2

variable_entero_1 = int(input("ingrese un numero entero: "))
variable_entero_2 = int(input("ingrese un numero entero: "))

variable_float = float(input("ingrese un numero flotante: "))

variable_string_1 = input("ingrese una cadena de texto: ")
variable_string_2 = input("ingrese una cadena de texto: ")

suma_numeros = float(variable_entero_1 + variable_entero_2 + variable_float)

print (f"La suma de los 3 numeros es :{suma_numeros}")

if variable_entero_1 > variable_entero_2:
    print (f"Este es el entero mayor {variable_entero_1}")

elif variable_entero_2 > variable_entero_1:
    print (f"Este es el entero mayor {variable_entero_2}")

else:
    print (f"El nuemro {variable_entero_2} y el numero {variable_entero_1} son iguales")

print (f"La división del float con el resto de la división de los dos enteros es: {(variable_entero_1/variable_entero_2)/variable_float}") 

print (f"Estas dos son cadenas de texto {variable_string_1}{variable_string_2}")

print("")

#Ejercicio 3

base = 3
exponente = 5

print (f"la potencia de {base} y {exponente} es {base ** exponente}")

print("")

#Ejercicio 4

a = 2
b = 8
c = 9
d = 27
e = 28
f = 55
g = 121

print("Raíz cuadrada de 2:", math.sqrt(a))
print("Raíz cuadrada de 8:", math.sqrt(b))
print("Raíz cuadrada de 9:", math.sqrt(c))
print("Raíz cuadrada de 27:", math.sqrt(d))
print("Raíz cuadrada de 28:", math.sqrt(e))
print("Raíz cuadrada de 55:", math.sqrt(f))
print("Raíz cuadrada de 121:", math.sqrt(g))


# Ejercicio 5

nombre_estudiante = "Carlos"


nota1 = 4.5
nota2 = 3.8
nota3 = 4.2
nota4 = 5.0
nota5 = 4.7

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5


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
print("numeroUno =", numero_uno)
print("numeroDos =", numero_dos)

auxiliar = numero_uno
numero_uno = numero_dos
numero_dos = auxiliar



print("Valores intercambiados:")
print("numeroUno =", numero_uno)
print("numeroDos =", numero_dos)

# Ejercicio 7 

Estado = (5 == 2) or (2 > 1)

print("El valor de Estado es:", Estado)

# Ejercicio 8 

Resultado = (9 / 3) + (8 * 2) - (5 + 1) + (10 % 3) + (2 ** 3)

print("El resultado de la operación es:", Resultado)

#Ejercicio 9

lado_cuadrado = 8

areaCuadrado = lado_cuadrado * lado_cuadrado
perimetroCuadrado = lado_cuadrado * 4

print("Área del cuadrado:", areaCuadrado)
print("Perímetro del cuadrado:", perimetroCuadrado)


base_triangulo = 9
altura_triangulo = 8
lado_uno_triangulo = 8
lado_dos_triangulo = 8

area_triangulo = (base_triangulo * altura_triangulo) / 2
perimetroTriangulo = base_triangulo + lado_uno_triangulo + lado_dos_triangulo

print("Área del triángulo:", area_triangulo)
print("Perímetro del triángulo:", perimetroTriangulo)


baseRectangulo = 8
alturaRectangulo = 6

areaRectangulo = baseRectangulo * alturaRectangulo
perimetroRectangulo = 2 * (baseRectangulo + alturaRectangulo)

print("Área del rectángulo:", areaRectangulo)
print("Perímetro del rectángulo:", perimetroRectangulo)

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