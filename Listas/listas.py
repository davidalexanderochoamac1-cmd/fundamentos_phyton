# =========================
# LISTAS EN PYTHON
# =========================

# Estructura básica de una lista

# Índice      0           1           2
# Índices-   -3          -2          -1

# Creación de una lista
lista = ["objeto_1", "objeto_2", "objeto_3"]

# Mostrar el tipo de dato de la variable
print("La variable 'lista' es de tipo:", type(lista))


# =========================
# LISTA MIXTA
# =========================

# Lista con diferentes tipos de datos
lista_mixta = ["texto", 12, 4.1, False, [1, 2, 3]]

# Mostrar el contenido de la lista mixta
print("El contenido de la lista mixta es:", lista_mixta)


# =========================
# LISTA DE APRENDICES
# =========================

# Crear lista de aprendices
aprendices = ["Carlos", "Pedro", "Luis", "Jorge", "María"]

# Mostrar lista completa
print("La lista de aprendices es:", aprendices)

# Mostrar un elemento específico usando índice
print("El aprendiz ubicado en la posición 1 es:", aprendices[1])


# =========================
# MODIFICAR ELEMENTOS
# =========================

# Cambiar el valor de la posición 0
aprendices[0] = "Juan"

# Mostrar lista modificada
print("La lista después de modificar el primer aprendiz es:", aprendices)


# =========================
# CONSULTA CON RANGO
# =========================

# Mostrar elementos desde la posición 0 hasta la 1
print("Los elementos desde la posición 0 hasta la 1 son:", aprendices[0:2])

# Mostrar elementos de dos en dos
print("Los elementos tomados de dos en dos son:", aprendices[0::2])


# =========================
# CONSULTA SELECTIVA
# =========================

# Mostrar el elemento de la posición 0
print("El elemento ubicado en la posición 0 es:", aprendices[0])


# =========================
# CONCATENAR LISTAS
# =========================

# Crear listas numéricas
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6, 2]

# Unir listas usando el operador +
lista_concatenada = lista_1 + lista_2

# Mostrar resultado de la concatenación
print("La lista concatenada es:", lista_concatenada)


# =========================
# UNIR LISTAS CON EXTEND
# =========================

# Agregar todos los elementos de lista_2 a lista_1
extend_listas_unidas = lista_1.extend(lista_2)

# Mostrar lista después de usar extend
print("La lista 1 después de usar extend es:", lista_1)


# =========================
# MEDIR LONGITUD CON LEN
# =========================

# Mostrar cantidad de elementos de la lista
print("La cantidad de elementos de la lista 1 es:", len(lista_1))


# =========================
# CONTAR ELEMENTOS CON COUNT
# =========================

# Contar cuántas veces aparece el número 2
count_num_2 = lista_1.count(2)

# Mostrar resultado del conteo
print("La cantidad de veces que aparece el número 2 es:", count_num_2)


# =========================
# OBTENER ÍNDICE CON INDEX
# =========================

# Obtener la posición del primer número 2
index_num_1 = lista_1.index(2)

# Mostrar índice encontrado
print("La primera posición donde aparece el número 2 es:", index_num_1)


# =========================
# COPIAR LISTAS CON COPY
# =========================

# Crear una copia de la lista
nueva_lista = lista_2.copy()

# Mostrar copia realizada
print("La copia de la lista 2 es:", nueva_lista)


# =========================
# AGREGAR ELEMENTOS
# =========================

# Agregar un elemento al final de la lista
lista_1.append(8)

# Mostrar lista después de append
print("La lista 1 después de agregar el número 8 es:", lista_1)

# Insertar un elemento en una posición específica
lista_1.insert(0, 0)

# Mostrar lista después de insert
print("La lista 1 después de insertar el número 0 en la posición 0 es:", lista_1)


# =========================
# ELIMINAR ELEMENTOS
# =========================

# Eliminar el primer número 2 encontrado
lista_1.remove(2)

# Mostrar lista después de remove
print("La lista 1 después de eliminar el primer número 2 es:", lista_1)

# Eliminar el elemento ubicado en la posición 2
lista_1.pop(2)

# Mostrar lista después de pop
print("La lista 1 después de eliminar el elemento en la posición 2 es:", lista_1)


# =========================
# PERTENENCIA CON IN
# =========================

# Verificar si un número está en la lista
if 123456 in lista_1:

    # Mensaje si el número existe
    print("El número 123456 sí está en la lista")

else:

    # Mensaje si el número no existe
    print("El número 123456 no está en la lista")


# =========================
# ORDENAR LISTA
# =========================

# Ordenar lista de menor a mayor
lista_1.sort()

# Mostrar lista ordenada
print("La lista 1 ordenada de menor a mayor es:", lista_1)


# =========================
# INVERTIR LISTA
# =========================

# Invertir el orden de la lista
lista_1.reverse()

# Mostrar lista invertida
print("La lista 1 invertida es:", lista_1)


# =========================
# LIMPIAR LISTA
# =========================

# Eliminar todos los elementos de la lista
lista_1.clear()

# Mostrar lista vacía
print("La lista 1 después de eliminar todos sus elementos es:", lista_1)