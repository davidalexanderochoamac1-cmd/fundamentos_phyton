"""
Fundamentos de Programación
"""

# Fundamentos de Programación
from operator import truediv


print("Hello, World!")

# Tipos de escritura
camelCase = "sena"
PascalCase = "Sena"
snake_case = "sena"

# Variables
nombre = "David"
apellido = "Ochoa"
edad = 18
altura = 1.74
activo = True
correo = "flsmdfrb@gmail.com"
telefono = "3128639385"
cedula = 1234567890

# Conversión de tipos de datos
telefono_int = int(telefono)
edad_float = float(edad)
altura_int = int(altura)
cedula_str = str(cedula)

# Imprime el tipo de dato y el valor de cada variable
print("--------------------------------------------------")
print(type(nombre), nombre)
print(type(apellido), apellido)
print(type(edad), edad)
print(type(altura), altura)
print(type(activo), activo)
print(type(correo), correo)
print(type(telefono), telefono)
print(type(cedula), cedula)

# Imprime el tipo de dato y el valor de cada variable después de la conversión
print("--------------------------------------------------")
print(type(telefono_int), telefono_int)
print(type(edad_float), edad_float)
print(type(altura_int), altura_int)
print(type(cedula_str), cedula_str)

#Indentación en python 
if 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")

#Input
nombre_completo = input("Ingrese su nombre: ")
edad_int = int(input("Ingrese su edad: "))
print("Hola, " + nombre_completo + "! Bienvenido a la programación en Python.")
print("Tu edad es: " + str(edad_int))

#Otra forma de imprimir la edad utilizando f-string
print(f"Tu edad es: {edad_int}")