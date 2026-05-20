import math

# 🎯 Actividad 2: Análisis de Temperaturas Semanales

# Lista de temperaturas registradas durante 14 días
temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

# ==================================================
# Indexación
# ==================================================

# Mostrar temperaturas usando índices positivos y negativos
print("Primer día:", temperaturas[0])
print("Último día:", temperaturas[-1])
print("Día 7:", temperaturas[6])
print("Penúltimo día:", temperaturas[-2])

# ==================================================
# Slicing
# ==================================================

# Mostrar días pares de cada semana
print("Días pares de la semana_1:", temperaturas[1:7:2])
print("Días pares de la semana_2:", temperaturas[7:14:2])

# Invertir el orden de la lista
temperaturas.reverse()

print(f"La lista en orden invertido es: {temperaturas}")

# ==================================================
# Promedio de temperaturas
# ==================================================

# Calcular promedio de cada semana
promedio_semana_1 = sum(temperaturas[0:7]) / len(temperaturas[0:7])
promedio_semana_2 = sum(temperaturas[7:14]) / len(temperaturas[7:14])

# Mostrar promedios redondeados
print(f"Promedio de la semana 1: {round(promedio_semana_1, 2)}")
print(f"Promedio de la semana 2: {round(promedio_semana_2, 2)}")

# ==================================================
# Comparación de promedios
# ==================================================

# Comparar cuál semana tuvo mayor promedio
if promedio_semana_1 > promedio_semana_2:
    print("La semana 1 tuvo una temperatura promedio mayor.")

elif promedio_semana_1 < promedio_semana_2:
    print("La semana 2 tuvo una temperatura promedio mayor.")