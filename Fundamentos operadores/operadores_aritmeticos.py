#Librerias matematicas
import math
import random

#Math
print(f"El valor de π es: {math.pi}")
print(f"El valor de e es: {math.e}")
print(f"La raíz cuadrada de 32 es: {math.sqrt(32)}")

#Random
random.random() #Genera un número aleatorio entre 0 y 1
numero_aleatorio = random.randint(1, 100) #Genera un número aleatorio entre 1 y 100
print(f"Un número aleatorio entre 1 y 100 es: {numero_aleatorio}")

#Operadores aritméticos

a = 10
b = 5

#Suma
suma = a + b
print(f"La suma de {a} y {b} es: {suma}")

#Resta
resta = a - b
print(f"La resta de {a} y {b} es: {resta}")

#Multiplicación
multiplicacion = a * b
print(f"La multiplicación de {a} y {b} es: {multiplicacion}")

#División flotante o decimal
division = a / b
print(f"La división de {a} y {b} es: {division}")

#División entera
division_entera = a // b
print(f"La división entera de {a} y {b} es: {division_entera}")

#Residuo
residuo = a % b
print(f"El residuo de {a} y {b} es: {residuo}")

#Potencia
potencia = a ** b
print(f"La potencia de {a} y {b} es: {potencia}")
print("")

#Precedencia de operadores
resultado = a + b * 2
print(f"El resultado de la operación {a} + {b} * 2 es: {resultado}")

resultado_2 = (a + b) * 2
print(f"El resultado de la operación ({a} + {b}) * 2 es: {resultado_2}")

resultado_3 = a * b // 3
print(f"El resultado de la operación {a} * {b} // 3 es: {resultado_3}")

resultado_4 = (a * b) // 3
print(f"El resultado de la operación ({a} * {b}) // 3 es: {resultado_4}")   

resultado_5 = a * (b // 3)
print(f"El resultado de la operación {a} * ({b} // 3) es: {resultado_5}")

resultado_6 = ((a**b)) / ((2*a)-(a+b))
print(f"El resultado de la operación (({a}**{b}))/(({a}+{b})-(2*{a})) es: {resultado_6}")