import time      # Librería para manejar tiempos (pausas, animaciones)
import random    # Librería para generar números aleatorios

print("")
print("Bienvenido al juego de piedra, papel o tijera")
print("")

# ===================== ENTRADA DEL USUARIO =====================

# Se pide al usuario que seleccione una opción
seleccion = int(input("Seleccione una opcion: 1.piedra, 2.papel, 3.tijera: "))

# Función para validar que la opción esté entre 1 y 3
def validar_seleccion(seleccion):
    if seleccion < 1 or seleccion > 3:
        print("Opcion no existente. Intente nuevamente.")
        return False  # Opción inválida
    return True       # Opción válida

# Se repite hasta que el usuario ingrese un valor correcto
while not validar_seleccion(seleccion):
    seleccion = int(input("Seleccione una opcion: 1.piedra, 2.papel, 3.tijera: "))

print("")

# ===================== ELECCIÓN DEL SISTEMA =====================

print("="*45)

# Se genera un número aleatorio entre 1 y 3
random = random.randint(1,3)

# Se muestra lo que eligió el sistema
if random == 1:
    print("El sistema selecciono: piedra")
elif random == 2:
    print("El sistema selecciono: papel")
elif random == 3:
    print("El sistema selecciono: tijera")

print("-"*45)

# ===================== ELECCIÓN DEL USUARIO =====================

# Se muestra lo que eligió el usuario
if seleccion == 1:
    print("Seleccionaste: piedra")
elif seleccion == 2:
    print("Seleccionaste: papel")
elif seleccion == 3:
    print("Seleccionaste: tijera")

print("="*45)

# ===================== BARRA DE CARGA =====================

# Función que simula una barra de carga
def barra_carga(total=20, duracion=2):
    for carga in range(total + 1):
        progreso = int((carga / total) * 100)  # Porcentaje
        barra = "🟩" * carga + "⬜" * (total - carga)  # Visual
        print(f"\r{barra} {progreso}%", end="")  # \r sobrescribe la línea
        time.sleep(duracion / total)  # Pausa

print('[Procesando resultado...]')
barra_carga()
print("")

# ===================== RESULTADO =====================

# Comparación de elecciones
if seleccion == random:
    print("Empate")

elif seleccion == 1 and random == 3:
    print("Ganaste, piedra gana a tijera")

elif seleccion == 2 and random == 1:
    print("Ganaste, papel gana a piedra")

elif seleccion == 3 and random == 2:
    print("Ganaste, tijera gana a papel")

elif seleccion == 1 and random == 2:
    print("Perdiste, papel gana a piedra")

elif seleccion == 2 and random == 3:
    print("Perdiste, tijera gana a papel")

elif seleccion == 3 and random == 1:
    print("Perdiste, piedra gana a tijera")