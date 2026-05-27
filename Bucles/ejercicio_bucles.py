# =========================
# EJERCICIOS DE BUCLES
# =========================

# Ejercicio 1: tabla de multiplicar
numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))

print("\nTabla de multiplicar")

for contador in range(1, 11):
    print(f"{numero} x {contador} = {numero * contador}")


# Ejercicio 2: suma acumulada
print("\nSuma acumulada del 1 al 5")

acumulado = 0

for numero_suma in range(1, 6):
    acumulado += numero_suma
    print(f"Acumulado actual: {acumulado}")

print(f"Resultado final: {acumulado}")


# Ejercicio 3: validar una nota con while
print("\nValidacion de nota")

nota = float(input("Ingrese una nota entre 0 y 5: "))

while nota < 0 or nota > 5:
    print("La nota debe estar entre 0 y 5. Intente nuevamente.")
    nota = float(input("Ingrese una nota entre 0 y 5: "))

print(f"La nota registrada fue: {nota}")


# Ejercicio 4: contar pares
print("\nNumeros pares del 1 al 20")

for numero_par in range(1, 21):
    if numero_par % 2 == 0:
        print(numero_par)
