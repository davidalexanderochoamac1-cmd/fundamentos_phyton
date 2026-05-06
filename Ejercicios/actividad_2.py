#Calculadors de notas 

nota_1 = float(input("Ingrese la primera nota: "))
while nota_1 < 0 or nota_1 > 5:
    print("La nota debe estar entre 0 y 5. Intente nuevamente.")
    nota_1 = float(input("Ingrese la primera nota: "))

print("-" * 45)

nota_2 = float(input("Ingrese la segunda nota: "))
while nota_2 < 0 or nota_2 > 5:
    print("La nota debe estar entre 0 y 5. Intente nuevamente.")
    nota_2 = float(input("Ingrese la segunda nota: "))

print("-" * 45)

nota_3 = float(input("Ingrese la tercera nota: "))
while nota_3 < 0 or nota_3 > 5:
    print("La nota debe estar entre 0 y 5. Intente nuevamente.")
    nota_3 = float(input("Ingrese la tercera nota: "))

print("-" * 45)

#promedio
promedio = (nota_1 + nota_2 + nota_3) / 3

print("=" * 45)
print("                RESULTADO")
print("=" * 45)
if promedio >= 3:
    print(f" El promedio es: {round(promedio,1)}.")
    print("                ¡Aprobado!")
else:
    puntos_faltantes = 3 - promedio
    print(f" El promedio es: {round(promedio,1 )}.")
    print(f" Te faltan {round(puntos_faltantes,1)} puntos para aprobar.")
    print("                REPROBADO")
    
print("=" * 45)