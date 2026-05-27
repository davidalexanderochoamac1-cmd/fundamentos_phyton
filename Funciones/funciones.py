# =========================
# FUNCIONES EN PYTHON
# =========================

# Una funcion permite agrupar instrucciones para reutilizarlas.
# Se define con def, puede recibir parametros y tambien retornar valores.


# =========================
# FUNCION SIMPLE
# =========================

def saludar(nombre, tema):
    return f"Hola {nombre}, bienvenido al tema de {tema}"


# =========================
# FUNCION CON PARAMETROS
# =========================

def mostrar_aprendiz(nombre, programa):
    print(f"El aprendiz {nombre} pertenece al programa {programa}")


# =========================
# FUNCION CON RETORNO
# =========================

def sumar(numero_1, numero_2):
    resultado = numero_1 + numero_2
    return resultado


# =========================
# FUNCIONES MATEMATICAS
# =========================

def restar(numero_1, numero_2):
    resultado = numero_1 - numero_2
    return resultado


def multiplicar(numero_1, numero_2):
    resultado = numero_1 * numero_2
    return resultado


def dividir(numero_1, numero_2):
    if numero_2 == 0:
        return "No se puede dividir entre cero"
    resultado = numero_1 / numero_2
    return resultado


def division_entera(numero_1, numero_2):
    if numero_2 == 0:
        return "No se puede dividir entre cero"
    resultado = numero_1 // numero_2
    return resultado


def calcular_residuo(numero_1, numero_2):
    if numero_2 == 0:
        return "No se puede dividir entre cero"
    resultado = numero_1 % numero_2
    return resultado


def potenciar(base, exponente):
    resultado = base ** exponente
    return resultado


def calcular_raiz_cuadrada(numero):
    if numero < 0:
        return "No existe raiz cuadrada real para numeros negativos"
    resultado = numero ** 0.5
    return resultado


def calcular_promedio(numero_1, numero_2, numero_3):
    resultado = (numero_1 + numero_2 + numero_3) / 3
    return resultado


def calcular_valor_absoluto(numero):
    if numero < 0:
        return -numero
    return numero


def redondear_numero(numero, decimales):
    return round(numero, decimales)


def calcular_porcentaje(cantidad, porcentaje):
    return cantidad * porcentaje / 100


def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def convertir_fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def es_par(numero):
    return numero % 2 == 0


def es_impar(numero):
    return numero % 2 != 0


def es_multiplo(numero, multiplo):
    if multiplo == 0:
        return False
    return numero % multiplo == 0


def mayor_de_dos(numero_1, numero_2):
    if numero_1 > numero_2:
        return numero_1
    return numero_2


def menor_de_dos(numero_1, numero_2):
    if numero_1 < numero_2:
        return numero_1
    return numero_2


def mayor_de_tres(numero_1, numero_2, numero_3):
    return max(numero_1, numero_2, numero_3)


def menor_de_tres(numero_1, numero_2, numero_3):
    return min(numero_1, numero_2, numero_3)


def convertir_a_mayusculas(texto):
    return texto.upper()


def convertir_a_minusculas(texto):
    return texto.lower()


def contar_caracteres(texto):
    return len(texto)


def invertir_texto(texto):
    return texto[::-1]


def unir_textos(texto_1, texto_2):
    return texto_1 + texto_2


def reemplazar_texto(texto, texto_viejo, texto_nuevo):
    return texto.replace(texto_viejo, texto_nuevo)


def contar_vocales(texto):
    contador = 0
    for letra in texto.lower():
        if letra in "aeiou":
            contador += 1
    return contador


def calcular_area_cuadrado(lado):
    return lado * lado


def calcular_area_rectangulo(base, altura):
    return base * altura


def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


def calcular_perimetro_cuadrado(lado):
    return lado * 4


def calcular_perimetro_rectangulo(base, altura):
    return 2 * (base + altura)


def calcular_perimetro_triangulo(lado_1, lado_2, lado_3):
    return lado_1 + lado_2 + lado_3


def calcular_area_circulo(radio):
    return 3.1416 * (radio ** 2)


def calcular_perimetro_circulo(radio):
    return 2 * 3.1416 * radio


def sumar_lista(numeros):
    return sum(numeros)


def promedio_lista(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)


def mayor_de_lista(numeros):
    if len(numeros) == 0:
        return "La lista esta vacia"
    return max(numeros)


def menor_de_lista(numeros):
    if len(numeros) == 0:
        return "La lista esta vacia"
    return min(numeros)


def contar_elementos_lista(numeros):
    return len(numeros)


# =========================
# FUNCION PARA VALIDAR
# =========================

# Este ejemplo conserva la misma idea que ya aparece en tus ejercicios:
# una funcion valida un dato y luego el programa decide si debe repetir.

def validar_nota(nota, nota_minima, nota_maxima):
    if nota < nota_minima or nota > nota_maxima:
        print(f"La nota debe estar entre {nota_minima} y {nota_maxima}.")
        return False
    return True


# =========================
# FUNCION CON VALOR POR DEFECTO
# =========================

def presentar_ciudad(nombre, ciudad="Tunja"):
    print(f"{nombre} vive en {ciudad}")


# =========================
# FUNCION QUE COMBINA VARIAS OPERACIONES
# =========================

def mostrar_operaciones(numero_1, numero_2):
    print(f"\nNumeros recibidos: {numero_1} y {numero_2}")
    print(f"Suma: {sumar(numero_1, numero_2)}")
    print(f"Resta: {restar(numero_1, numero_2)}")
    print(f"Multiplicacion: {multiplicar(numero_1, numero_2)}")
    print(f"Division: {dividir(numero_1, numero_2)}")
    print(f"Division entera: {division_entera(numero_1, numero_2)}")
    print(f"Residuo: {calcular_residuo(numero_1, numero_2)}")
    print(f"Valor absoluto del primero: {calcular_valor_absoluto(numero_1)}")
    print(f"Mayor: {mayor_de_dos(numero_1, numero_2)}")
    print(f"Menor: {menor_de_dos(numero_1, numero_2)}")


if __name__ == "__main__":
    print(saludar("David", "funciones"))
    mostrar_aprendiz("David", "ADSO")

    resultado_suma = sumar(10, 5)
    print(f"La suma es: {resultado_suma}")
    print(f"La resta es: {restar(10, 5)}")
    print(f"La multiplicacion es: {multiplicar(10, 5)}")
    print(f"La division es: {dividir(10, 5)}")
    print(f"La division entera es: {division_entera(10, 5)}")
    print(f"El residuo es: {calcular_residuo(10, 3)}")
    print(f"La potencia es: {potenciar(2, 4)}")
    print(f"La raiz cuadrada es: {calcular_raiz_cuadrada(81)}")
    print(f"El promedio es: {calcular_promedio(3, 4, 5)}")
    print(f"El valor absoluto es: {calcular_valor_absoluto(-25)}")
    print(f"El numero redondeado es: {redondear_numero(3.14159, 2)}")
    print(f"El porcentaje es: {calcular_porcentaje(200, 15)}")
    print(f"32 grados Celsius son {convertir_celsius_a_fahrenheit(32)} Fahrenheit")
    print(f"86 grados Fahrenheit son {redondear_numero(convertir_fahrenheit_a_celsius(86), 2)} Celsius")
    print(f"El numero 8 es par: {es_par(8)}")
    print(f"El numero 7 es impar: {es_impar(7)}")
    print(f"El numero 20 es multiplo de 5: {es_multiplo(20, 5)}")
    print(f"El mayor entre 9 y 4 es: {mayor_de_dos(9, 4)}")
    print(f"El menor entre 9 y 4 es: {menor_de_dos(9, 4)}")
    print(f"El mayor entre 3, 9 y 7 es: {mayor_de_tres(3, 9, 7)}")
    print(f"El menor entre 3, 9 y 7 es: {menor_de_tres(3, 9, 7)}")
    print(f"Texto en mayusculas: {convertir_a_mayusculas('python')}")
    print(f"Texto en minusculas: {convertir_a_minusculas('PROGRAMACION')}")
    print(f"Cantidad de caracteres: {contar_caracteres('funciones')}")
    print(f"Texto invertido: {invertir_texto('python')}")
    print(f"Textos unidos: {unir_textos('hola ', 'mundo')}")
    print(f"Texto reemplazado: {reemplazar_texto('me gusta python', 'python', 'programar')}")
    print(f"Cantidad de vocales: {contar_vocales('programacion')}")
    print(f"Area del cuadrado: {calcular_area_cuadrado(5)}")
    print(f"Area del rectangulo: {calcular_area_rectangulo(8, 4)}")
    print(f"Area del triangulo: {calcular_area_triangulo(10, 6)}")
    print(f"Perimetro del cuadrado: {calcular_perimetro_cuadrado(5)}")
    print(f"Perimetro del rectangulo: {calcular_perimetro_rectangulo(8, 4)}")
    print(f"Perimetro del triangulo: {calcular_perimetro_triangulo(3, 4, 5)}")
    print(f"Area del circulo: {redondear_numero(calcular_area_circulo(5), 2)}")
    print(f"Perimetro del circulo: {redondear_numero(calcular_perimetro_circulo(5), 2)}")
    print(f"Suma de lista: {sumar_lista([2, 4, 6, 8])}")
    print(f"Promedio de lista: {promedio_lista([2, 4, 6, 8])}")
    print(f"Mayor de lista: {mayor_de_lista([2, 4, 6, 8])}")
    print(f"Menor de lista: {menor_de_lista([2, 4, 6, 8])}")
    print(f"Cantidad de elementos de lista: {contar_elementos_lista([2, 4, 6, 8])}")

    nota_minima = 0
    nota_maxima = 5
    nota_estudiante = float(input("\nIngrese una nota entre 0 y 5: "))

    while not validar_nota(nota_estudiante, nota_minima, nota_maxima):
        nota_estudiante = float(input("Ingrese una nota entre 0 y 5: "))

    print(f"La nota final fue: {nota_estudiante}")

    presentar_ciudad("Laura")
    presentar_ciudad("Carlos", "Bogota")
    mostrar_operaciones(20, 4)
