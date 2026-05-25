# ================================

# EJERCICIO 1

# Análisis de Calificaciones

# ================================

# Función para analizar las calificaciones

def analizar_calificaciones(calificaciones):


# Calcular promedio
    promedio = sum(calificaciones) / len(calificaciones)

# Obtener nota más alta
    nota_alta = max(calificaciones)

# Obtener nota más baja
    nota_baja = min(calificaciones)

# Retornar resultados en una tupla
    return promedio, nota_alta, nota_baja


# Lista de ejemplo

notas = [4.5, 3.8, 5.0, 2.9, 4.2]

# Llamar la función

resultado = analizar_calificaciones(notas)

# Mostrar resultados

print("Promedio:", round(resultado[0], 2))
print("Nota más alta:", resultado[1])
print("Nota más baja:", resultado[2])