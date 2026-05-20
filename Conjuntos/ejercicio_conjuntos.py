# actividad4_sets.py

# Conjuntos de aprendices
python_curso = {'Ana', 'Luis', 'Marta', 'Carlos', 'Sofia', 'Pedro'}

java_curso = {'Luis', 'Carlos', 'Pedro', 'Laura', 'Diego'}

bd_curso = {'Marta', 'Sofia', 'Laura', 'Ana', 'Miguel'}

# Unión de los tres conjuntos
todos = python_curso | java_curso | bd_curso

print("Aprendices completos:")
print(todos)
print("")

# Aprendices en Python y Java
python_java = python_curso & java_curso

print("Python y Java:")
print(python_java)
print("")

# Solo en Python
solo_python = python_curso - java_curso - bd_curso

print("Solo Python:")
print(solo_python)
print("")

# Exactamente en dos programas
dos_programas = (
    (python_curso & java_curso) |
    (python_curso & bd_curso) |
    (java_curso & bd_curso)
)

tres_programas = python_curso & java_curso & bd_curso

dos_programas = dos_programas - tres_programas

print("Exactamente en dos programas:")
print(dos_programas)
print("")

# Lista con duplicados
inscripciones = [
    'Ana', 'Luis', 'Ana', 'Marta',
    'Carlos', 'Luis', 'Sofia',
    'Pedro', 'Ana'
]

# Convertir a conjunto
unicos = set(inscripciones)

print("Cantidad de aprendices únicos:")
print(len(unicos))

print("Aprendices únicos:")
print(unicos)
print("")

# Conteo de programas
conteo_programas = {}

for aprendiz in todos:

    cantidad = 0

    if aprendiz in python_curso:
        cantidad += 1

    if aprendiz in java_curso:
        cantidad += 1

    if aprendiz in bd_curso:
        cantidad += 1

    conteo_programas[aprendiz] = cantidad

print("Conteo de programas:")
print(conteo_programas)
print("")

# En los tres programas
print("En los tres programas:")
print(tres_programas)