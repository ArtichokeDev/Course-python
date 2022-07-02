# Bucle While

import math

n = int(input("Escriba un numero: "))

while n < 0:
    print("ERROR, el numero ha de ser positivo")
    n = int(input("Escriba un numero: "))

print(f"\Su raiz cuadrada es de {(math.sqrt(n)):.2f}")

###############
n = 0

while n <= 10:
    print(n)
    n += 1




