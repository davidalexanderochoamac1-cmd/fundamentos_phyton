# ===================== CALCULADORA DE NOTAS =====================

# Valores de referencia
nota_maxima = 5.0   # Nota máxima posible
nota_minima = 3.0   # Nota mínima para aprobar

# ===================== NOTA 1 =====================
# Se pide la primera nota al usuario
nota_1 = float(input("Ingrese la primera nota: "))

# Validación: la nota debe estar entre 0 y 5
while nota_1 < 0 or nota_1 > 5:
    print("La nota debe estar entre 0 y 5. Intente nuevamente.")
    nota_1 = float(input("Ingrese la primera nota: "))

print("-" * 45)  # Línea decorativa

# ===================== NOTA 2 =====================
nota_2 = float(input("Ingrese la segunda nota: "))

# Validación
while nota_2 < 0 or nota_2 > 5:
    print("La nota debe estar entre 0 y 5. Intente nuevamente.")
    nota_2 = float(input("Ingrese la segunda nota: "))

print("-" * 45)

# ===================== NOTA 3 =====================
nota_3 = float(input("Ingrese la tercera nota: "))

# Validación
while nota_3 < 0 or nota_3 > 5:
    print("La nota debe estar entre 0 y 5. Intente nuevamente.")
    nota_3 = float(input("Ingrese la tercera nota: "))

print("-" * 45)

# ===================== PROMEDIO =====================
# Se calcula el promedio de las 3 notas
promedio = (nota_1 + nota_2 + nota_3) / 3

# ===================== RESULTADO =====================
print("=" * 45)
print("                RESULTADO")
print("=" * 45)

# Condicional para saber si aprueba o no
if promedio >= 3:
    # Si aprueba
    print(f" El promedio es: {round(promedio, 2)}.")  # round() redondea a 2 decimales
    print("                ¡Aprobado!")
else:
    # Si pierde
    puntos_maxfaltantes = nota_maxima - promedio  # Cuánto falta para llegar a 5
    puntos_minfaltantes = nota_minima - promedio  # Cuánto falta para llegar a 3

    print(f" El promedio es: {round(promedio, 2)}.")
    print(f" Te faltan {round(puntos_maxfaltantes, 2)} puntos para llegar a la nota máxima.")
    print(f" Te faltan {round(puntos_minfaltantes, 2)} puntos para aprobar.")
    print("                REPROBADO")

print("=" * 45)