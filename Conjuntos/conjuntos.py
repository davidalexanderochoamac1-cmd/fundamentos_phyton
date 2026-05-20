# Conjuntos

# Estructura de un conjunto

conjunto = set()
print(type(conjunto))

# Creacion
lenguajes = {"Python", "Java", "C++", "Python", "Java"}
print(lenguajes,"\n")

# Metodos de modificacion
frutas ={"mango","guayaba","mora"}
frutas.add("maracuya")
frutas.add("mango")
frutas.remove("mora")
frutas.discard("papaya")
elem = frutas.pop()
print (frutas)
print (elem,"\n")

# Verificacion pertenencia
print("Python" in lenguajes)
print("COBOL" in lenguajes,"\n")

# EJERCICIO

# CONJUNTOS
python_devs = {"Ana","Luis","Marta","Carlos","Sofia"}
java_devs = {"Luis","Carlos","Pedro","Laura"}

# UNION DE 2 CONJUNTOS | o .union
todos = python_devs | java_devs
print(f"Union: {todos}")

# INTERSECCIÓN DE 2 CONJUNTOS & o .intersection
todos = python_devs & java_devs
print(f"Interseccion: {todos}")

# DIFERENCIA DE 2 CONJUNTOS - o differece
todos = python_devs - java_devs
print(f"Diferencia: {todos}")

# DIFERENCIA SIMETRICA DE 2 CONJUNTOS ^ o .symmetric_difference
todos = python_devs ^ java_devs
print(f"Diferencia simetrica: {todos}")

