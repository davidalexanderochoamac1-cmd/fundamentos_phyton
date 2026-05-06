#Clasificador de IMC
#Valida que el peso y estatura sean positivos
peso = float(input("Ingrese su peso en kilogramos: "))

def validar_peso(peso):
    if peso < 0 or peso == 0:
        print("El peso no puede ser negativo o 0. Intente nuevamente.")
        return False
    return True

while not validar_peso(peso):
    peso = float(input("Ingrese su peso en kilogramos: "))

print("-" * 45)

estatura = float(input("Ingrese su estatura en metros: "))

def validar_estatura(estatura):
    if estatura < 0 or estatura == 0:
        print("La estatura no puede ser negativa o 0. Intente nuevamente.")
        return False
    return True

while not validar_estatura(estatura):
    estatura = float(input("Ingrese su estatura en metros: "))

print("-" * 45)

imc = peso / (estatura ** 2)
print("=" * 45)
print("                RESULTADO")
print("=" * 45)
print(f"Peso ingresado:{round(peso,2)} kg")
print(f"Estatura ingresada: {round(estatura,2)} m")
print("-" * 45)
if imc < 18.5:
    print(f"Tu IMC es: {round(imc,2)}. Clasificación: Bajo peso")
elif imc >= 18.5 and imc < 25:
    print(f"Tu IMC es: {round(imc,2)}. Clasificación: Normal")
elif imc >= 25 and imc < 30:
    print(f"Tu IMC es: {round(imc,2)}. Clasificación: Sobrepeso")
else:
    print(f"Tu IMC es: {round(imc,2)}. Clasificación: Obesidad")
print("=" * 45)