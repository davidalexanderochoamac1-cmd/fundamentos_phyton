#Calculadora de notas 

#Se ingresan 3 notas se promedian y si es mayor a 3 se aprueba, si es menor a 3 se reprueba7

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 3:
    print(f"El promedio es: {promedio}. ¡Aprobado!")
else:
    print(f"El promedio es: {promedio}. Reprobado.")