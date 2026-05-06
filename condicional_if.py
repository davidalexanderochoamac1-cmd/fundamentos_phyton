#Condicional if elif else

if True:
    print("La primera condicion es verdadera")
elif False:
    print("La segunda condicion es verdadera")
elif False:
    print("La tercera condicion es verdadera")
else:
    print("La condicion es falsa")

#Ejercicio: Clasificacion de Edad
edad = int(input("Ingrese su edad: "))


if edad < 18 and edad > 0:
    print ("Eres menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres adulto")
elif edad >= 65 and edad <= 100:
    print("Eres adulto mayor")
elif edad == 0:
    print("Edad no valida")
else:
    print("Edad no valida")


#if anidados
edad = int(input("Ingrese su edad: "))

if edad < 18 and edad > 0:
    if edad < 12:
        print("Eres un niño")
    else:
        print("Eres un adolescente") 
else:
    if edad >= 18 and edad < 65:
        print("Eres un adulto")
    elif edad >= 65 and edad <= 100:
        print("Eres un adulto mayor")
    else:
        print("Edad no valida")

#Operador ternario
numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")

print(f"El numero {numero} es par" if numero % 2 == 0 else f"El numero {numero} es impar")