# open (nombre, modo )-> Funcion de python para manipular archivos 

# R (Read) Lectura
# W (Write) Escritura
# x (Create) Crear un nuevo archivo
# a (Append) Agregar contenido a un archivo existente
# t (Text) Modo texto
# b (Binary) Modo binario

try:
    file = open("archivo.txt", "r")
    print(file.readline())
    file.close()
except FileNotFoundError:
    print("No se encontró el archivo 'archivo.txt'")

# Uso del with para no cerrar el archivo manualmente

try: 
    with open("archivo.txt", "r") as file:
        print(file.readline())
except FileNotFoundError:
    print("No se encontró el archivo 'archivo.txt'")

# Sobreescribir un archivo
try:
    with open("archivo.txt", "w") as file:
        file.write("Texto sobrescrito")
except Exception as e:
    print(f"Ocurrió un error: {e}")