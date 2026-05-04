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
operacion = input("Ingrese la operación a realizar (1.suma, 2.resta, 3.multiplicación, 4.división, 5.división entera, 6.residuo, 7.potencia): ")
if operacion == "1":
    resultado = suma
elif operacion == "2":
    resultado = resta
elif operacion == "3":
    resultado = multiplicacion
elif operacion == "4":
    resultado = division
elif operacion == "5":
    resultado = division_entera
elif operacion == "6":
    resultado = residuo
elif operacion == "7":
    resultado = potencia

# Imprime los resultados
print ("Resultado:", resultado)