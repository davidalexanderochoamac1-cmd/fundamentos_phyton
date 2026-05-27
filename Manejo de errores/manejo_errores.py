# manejo de errores try-except

# Estructura 
try: 
    print("Intentemos algo")
except:
    print("Captura el error")
finally:
    print("Esto se ejecuta siendo exitoso o no el bloque")


# Ejemplo: Convertir o castear dato de entrada del usuario 
while True:
    try:
        edad_usuario = int(input("\n Ingrese su edad: "))
        break  # Salir del bucle si la conversión es exitosa
    except ValueError:
        print("Debe ingresar un número válido para la edad.")

#Ejemplo Variable no definida
try:
    print(x)
except NameError:
    print("\n La variable x no está definida")

#Ejemplo división por cero
try:
    numero = 10/0
except ZeroDivisionError:
    print("\n No se puede dividir por cero")