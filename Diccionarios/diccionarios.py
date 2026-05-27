# DICCIONARIOS (Caracteristicas a un elemento)
# Creacion de un diccionario

# Estructura de un diccionario 
diccionario = {
    "clave_1": "valor_1",
    "clave_2": "valor_2",
    "clave_3": "valor_3"
}

# Diccionario vacio
diccionario_vacio = {}

# Diccionario con elemnentos 
diccionario_aprendiz = {
    "nombre": "Felipe",
    "apellido": "Sandoval",
    "programa": "ADSO",
    "edad": 32,
    
}

print(type(diccionario_aprendiz),diccionario_aprendiz,"\n")

# Acceder a un valor a través de su clave
print(diccionario_aprendiz["programa"])
print(diccionario_aprendiz.get("programa"),"\n")

# Obtener solo las claves del diccionario
print(diccionario_aprendiz.keys(),"\n")

# Obtener solo los valores del diccionario
print(diccionario_aprendiz.values(),"\n")

# Obtener claves y valores del diccionario 
print(diccionario_aprendiz.items(),"\n")

# Agregar un elemento al diccionario 
diccionario_aprendiz["correo"] = "afsandoval@sena.edu.co"
print (diccionario_aprendiz,"\n")

# Modificar un elemento 
diccionario_aprendiz["programa"] = "SST"
print(diccionario_aprendiz,"\n")

# Metodo update
diccionario_aprendiz.update({"nombre": "Andres"})
diccionario_aprendiz.update({"ciudad":"Duitama"})

print(diccionario_aprendiz,"\n")

# Comprobar pertenencia in 

if "programa" in diccionario_aprendiz:
    print("programa es una de las propiedades de este Diccionario ","\n")

# Recorrer solo las claves del diccionario 
for clave in diccionario_aprendiz.keys():
    print(clave)

print("")

# Recorres solo las variables del diccionario
for valor in diccionario_aprendiz.values():
    print(valor)

print("")

# Recorrer claves y variables del diccionario
for clave, valor in diccionario_aprendiz.items():
    print(f"{clave}: {valor}")

print("")

# Eliminar un elemento del diccionario
diccionario_aprendiz.popitem()# Elimina el último elemento agregado al diccionario
print(diccionario_aprendiz,"\n")

diccionario_aprendiz.pop("apellido")# Elimina el elemento con la clave especificada
print(diccionario_aprendiz,"\n")

# Eliminar todos los elementos del diccionario
diccionario_aprendiz.clear()
print(diccionario_aprendiz,"\n")

# Diccionarios anidados
aprendices = {
    "aprendiz_1": {
        "nombre": "Felipe",
        "apellido": "Sandoval",
        "programa": "ADSO",
        "edad": 32
    },
    "aprendiz_2": {
        "nombre": "Andres",
        "apellido": "Gomez",
        "programa": "SST",
        "edad": 28,
    },
    "aprendiz_3": {
        "nombre": "Camilo",
        "apellido": "Perez",
        "programa": "TOPOGRAFÍA",
        "edad": 30,
    }
}

print(aprendices["aprendiz_1"]["nombre"],"\n")

# Recorrer un diccionario anidado
for aprendiz, datos in aprendices.items():
    print("")
    print(f"{aprendiz}")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")