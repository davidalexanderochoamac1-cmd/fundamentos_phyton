# =========================
# BUCLES EN PYTHON
# =========================

# Un bucle permite repetir instrucciones varias veces.
# Los dos mas usados son:
# 1. for    -> recorre elementos o rangos
# 2. while  -> se repite mientras una condicion sea verdadera


# =========================
# BUCLE FOR CON RANGE
# =========================

print("Conteo del 1 al 5 con for")

for numero in range(1, 6):
    print(numero)


# =========================
# FOR RECORRIENDO UNA LISTA
# =========================

aprendices = ["Carlos", "Laura", "Mateo", "Sofia"]

print("\nLista de aprendices")

for aprendiz in aprendices:
    print(aprendiz)


# =========================
# FOR CON INDICE
# =========================

print("\nAprendices con posicion")

for posicion, aprendiz in enumerate(aprendices):
    print(f"Posicion {posicion}: {aprendiz}")


# =========================
# WHILE
# =========================

print("\nConteo con while")

contador = 1

while contador <= 5:
    print(contador)
    contador += 1


# =========================
# VALIDACION CON WHILE
# =========================

# Este ejemplo mantiene la misma logica que ya usas en otros archivos:
# pedir un dato, validarlo y volver a pedirlo si no cumple la condicion.

edad = int(input("\nIngrese una edad entre 1 y 100: "))

while edad <= 0 or edad > 100:
    print("Edad no valida. Intente nuevamente.")
    edad = int(input("Ingrese una edad entre 1 y 100: "))

print(f"La edad registrada fue: {edad}")


# =========================
# BREAK Y CONTINUE
# =========================

print("\nEjemplo de continue")

for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)

print("\nEjemplo de break")

for numero in range(1, 6):
    if numero == 4:
        break
    print(numero)
