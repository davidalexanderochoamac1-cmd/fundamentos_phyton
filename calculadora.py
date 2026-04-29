# Calculadora básica
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
residuo = num1 % num2
potencia = num1 ** num2

#Elige la operación a realizar
operacion = input("Ingrese la operación a realizar (suma, resta, multiplicación, división, división entera, residuo, potencia): ")
if operacion == "suma":
    resultado = suma
elif operacion == "resta":
    resultado = resta
elif operacion == "multiplicación":
    resultado = multiplicacion
elif operacion == "división":
    resultado = division
elif operacion == "división entera":
    resultado = division_entera
elif operacion == "residuo":
    resultado = residuo
elif operacion == "potencia":
    resultado = potencia

# Imprime los resultados
print("Resultado:", resultado)