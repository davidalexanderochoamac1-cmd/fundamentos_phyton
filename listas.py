#Listas

#Estructura de una lista

# Indice     0           1           2
# Indices-  -3          -2          -1
lista = ["objeto_1", "objeto_2", "objeto_3"]
print(type(lista))# <class 'list'>

lista_mixta = ["texto", 12, 4.1, False]
print(lista_mixta)

# Lista de aprendices SENA ADSO

aprendices = ["Carlos", "Pedro", "Luis", "Jorge", "María"]
print(aprendices)
print(aprendices[1]) #Jorge

# Modificar elemento de la lista
aprendices[0] = "Juan"
print(aprendices)

# Consulta con rango 
print(aprendices[0:2])
print(aprendices[0::2])

# Consulta selectiva multiple
print(aprendices[0])

#Concatenar
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

lista_concatenada = lista_1 + lista_2

print(lista_concatenada)