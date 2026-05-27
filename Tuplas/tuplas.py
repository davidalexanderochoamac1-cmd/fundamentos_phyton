#Tuplas

# Estructura de una tupla

# Índice      0            1             2
tupla =("elemento_1", "elemento_2", "elemento_3")
print(type(tupla))

tupla_2= "a", "b", "c"
print(type(tupla_2))

tupla_3 = ("Hola",)
print(type(tupla_3))

tupla_4 = tuple("Hola")
print(type(tupla_4))

tupla_mixta = ("texto", 12, 4.1, False, [1, 2, 3])
print(tupla_mixta)

#Tupla aprendices sena ADSO
# Indice         0        1        2       3        4
aprendices = ("Simon", "Camilo", "Santiago", "Valentina", "Laura")
print(aprendices)

# Mostrar un elemento específico usando índice
print(aprendices[1])
 
# Modificar elemento de la tupla
#aprendices[0] = "Juan"
#print(aprendices) # Esto generará un error porque las tuplas son inmutables, no se pueden modificar sus elementos.

# Consulta con rango
print(aprendices[0:2])
print(aprendices[1::4])
print(aprendices[1:])

# Sumar 2 tuplas
tupla_1 = (1, 2, 3)
tupla_2 = (4, 5, 6)
tupla_suma = tupla_1 + tupla_2
print(tupla_suma)

# Multiplicar una tupla
tupla_multiplicada = tupla_1 * 3
print(tupla_multiplicada)

# Medir la longitud con len()
print(len(aprendices    ))

# Contar cuántas veces aparece un elemento con count()
print(aprendices.count("Camilo"))

# Encontrar la posición de un elemento con index()
print(aprendices.index("Valentina"))

# Modificar una una lista

print(type(aprendices))
aprendices_lista = list(aprendices)
aprendices_lista.append("Felipe")
print(type(aprendices_lista))
print(aprendices_lista)

aprendices = tuple(aprendices_lista)
print(type(aprendices))

# Comprobar pertenencia con in
print("Simon" in aprendices)
print("Andres" in aprendices)

# Empaquetar y desempquetar tuplas

# Empaquetar tupla
programa_1 = "ADSO"
programa_2 = "SST"
programa_3 = "TOPOGRAFÍA"

tupla_empaquetada = programa_1, programa_2, programa_3
print(tupla_empaquetada)

# Desempquetar tupla
tupla_desempaquetada = ("ADSO", "SST", "TOPOGRAFÍA")
program_1, program_2, program_3 = tupla_desempaquetada
print(program_1)
print(program_2)
print(program_3)

# EJRRCICIO 2 DESEMPAQUETAR TUPLA
tupla_ciudades = ("Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena")
ciudad_1, *ciudad_2 = tupla_ciudades
print(ciudad_1)
print(ciudad_2)

for ciudad in tupla_ciudades:
    print(ciudad)