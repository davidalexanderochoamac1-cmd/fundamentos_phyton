#Operadores logicos

#Operador AND
a = True
b = True
c = False

print(f"El resultado de {a} AND {b} es: {a and b}")
print(f"El resultado de {a} AND {c} es: {a and c}")
print(f"El resultado de {c} AND {b} es: {c and b}") 
print(f"El resultado de {c} AND {c} es: {c and c}")

print("Operador OR")

#Operador OR
print(f"El resultado de {a} OR {b} es: {a or b}")
print(f"El resultado de {a} OR {c} es: {a or c}")
print(f"El resultado de {c} OR {b} es: {c or b}")
print(f"El resultado de {c} OR {c} es: {c or c}")

print("Operador NOT")

#Operador NOT
print(f"El resultado de NOT {a} es: {not a}")
print(f"El resultado de NOT {b} es: {not b}")
print(f"El resultado de NOT {c} es: {not c}")

print("Ejercicio AND")

#Ejercicio AND

print(f"El resultado del ejercicio (5>3 and 2<4) es: {5>3 and 2<4}")
print(f"El resultado del ejercicio (5>3 and 2>4) es: {5>3 and 2>4}")
print(f"El resultado del ejercicio (5<3 and 2<4) es: {5<3 and 2<4}")
print(f"El resultado del ejercicio (5<3 and 2>4) es: {5<3 and 2>4}")

print("Ejercicio OR")

#Ejercicio OR
print(f"El resultado del ejercicio (5>3 or 2<4) es: {5>3 or 2<4}")
print(f"El resultado del ejercicio (5>3 or 2>4) es: {5>3 or 2>4}")
print(f"El resultado del ejercicio (5<3 or 2<4) es: {5<3 or 2<4}")
print(f"El resultado del ejercicio (5<3 or 2>4) es: {5<3 or 2>4}")

print("Ejercicio NOT")

#Ejercicio NOT
print(f"El resultado del ejercicio NOT (5>3) es: {not (5==3)}")
print(f"El resultado del ejercicio NOT (2<4) es: {not (2!=4)}")
print(f"El resultado del ejercicio NOT (5<3) es: {not (5<=3)}")
print(f"El resultado del ejercicio NOT (2>4) es: {not (2<=4)}")

