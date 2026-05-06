# ===================== CLASIFICADOR DE IMC =====================

# ===================== VALIDACIÓN DE PESO =====================

# Se pide el peso al usuario
peso = float(input("Ingrese su peso en kilogramos: "))

# Función para validar que el peso sea mayor a 0
def validar_peso(peso):
    if peso < 0 or peso == 0:  # Si es negativo o cero, no es válido
        print("El peso no puede ser negativo o 0. Intente nuevamente.")
        return False  # Indica que el dato es incorrecto
    return True  # Indica que el dato es válido

# Se repite hasta que el peso sea válido
while not validar_peso(peso):
    peso = float(input("Ingrese su peso en kilogramos: "))

print("-" * 45)

# ===================== VALIDACIÓN DE ESTATURA =====================

# Se pide la estatura al usuario
estatura = float(input("Ingrese su estatura en metros: "))

# Función para validar que la estatura sea mayor a 0
def validar_estatura(estatura):
    if estatura < 0 or estatura == 0:  # Validación
        print("La estatura no puede ser negativa o 0. Intente nuevamente.")
        return False
    return True

# Se repite hasta que la estatura sea válida
while not validar_estatura(estatura):
    estatura = float(input("Ingrese su estatura en metros: "))

print("-" * 45)

# ===================== CÁLCULO DEL IMC =====================

# Fórmula del IMC: peso / (estatura**2)
imc = peso / (estatura ** 2)

# ===================== RESULTADO =====================

print("=" * 45)
print("                RESULTADO")
print("=" * 45)

# Muestra los datos ingresados
print(f"Peso ingresado: {round(peso, 2)} kg")
print(f"Estatura ingresada: {round(estatura, 2)} m")

print("-" * 45)

# ===================== CLASIFICACIÓN =====================

# Según el valor del IMC se clasifica
if imc < 18.5:
    print(f"Tu IMC es: {round(imc, 2)}. Clasificación: Bajo peso")

elif imc >= 18.5 and imc < 25:
    print(f"Tu IMC es: {round(imc, 2)}. Clasificación: Normal")

elif imc >= 25 and imc < 30:
    print(f"Tu IMC es: {round(imc, 2)}. Clasificación: Sobrepeso")

else:
    print(f"Tu IMC es: {round(imc, 2)}. Clasificación: Obesidad")

print("=" * 45)