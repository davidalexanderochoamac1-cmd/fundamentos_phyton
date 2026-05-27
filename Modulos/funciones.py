def saludar(nombre, tema):
    return f"Hola {nombre}, bienvenido al tema de {tema}"


def sumar(numero_1, numero_2):
    return numero_1 + numero_2


def restar(numero_1, numero_2):
    return numero_1 - numero_2


def multiplicar(numero_1, numero_2):
    return numero_1 * numero_2


def dividir(numero_1, numero_2):
    if numero_2 == 0:
        return "No se puede dividir entre cero"
    return numero_1 / numero_2
