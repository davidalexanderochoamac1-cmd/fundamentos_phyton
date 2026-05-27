# actividad2_diccionarios.py

# Diccionario de aprendices
grupo = {
    101: {
        "nombre": "Carlos",
        "edad": 18,
        "notas": [3.5, 4.0, 3.8, 4.2],
        "ciudad": "Bogotá"
    },

    102: {
        "nombre": "Laura",
        "edad": 19,
        "notas": [2.5, 3.0, 2.8, 3.2],
        "ciudad": "Medellín"
    },

    103: {
        "nombre": "Andrés",
        "edad": 20,
        "notas": [4.5, 4.8, 4.2, 4.7],
        "ciudad": "Cali"
    },

    104: {
        "nombre": "Sofía",
        "edad": 18,
        "notas": [3.0, 3.5, 3.2, 3.8],
        "ciudad": "Tunja"
    }
}

# Mostrar reporte
print("REPORTE DE APRENDICES\n")

for ficha, datos in grupo.items():

    promedio = sum(datos["notas"]) / len(datos["notas"])

    if promedio >= 3.0:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    print("Ficha:", ficha)
    print("Nombre:", datos["nombre"])
    print("Edad:", datos["edad"])
    print("Promedio:", round(promedio, 2))
    print("Estado:", estado)
    print("Ciudad:", datos["ciudad"])
    print("")

# Agregar nuevo aprendiz
grupo[105] = {
    "nombre": "Mateo",
    "edad": 21,
    "notas": [4.0, 3.8, 4.2, 4.1],
    "ciudad": "Pasto"
}
print("Nuevo aprendiz agregado:\n", grupo[105],"\n")

# Actualizar ciudad
grupo[102]["ciudad"] = "Barranquilla"
print("Ciudad actualizada para Laura:\n", grupo[102],"\n")