num1 = float(input("Dijita el primer numero: "))
num2 = float(input("Dijita el segundo numero: "))
operacion = input("Dijita la operacion a realizar de esta forma"
                  + "Suma:s,S"
                  + "Resta:r,R"
                  + "Multiplicacion:m,M"
                  + "Division:d,D"
                  + "Mob:b,B: ").lower()
suma = num1+num2
resta = num1-num2
multiplicacion = num1*num2
division = num1/num2
mob = num1%num2
if operacion=='s':
    print(f"La suma de los numeros es {suma}")
elif operacion=='r':
    print(f"La resta de los 2 numeros es {resta}")
elif operacion=='m':
    print(f"La multiplicacion de los numeros es {multiplicacion}")
elif operacion=='d':
    print(f"La division de los numeros es {division}")
elif operacion=='b':
    print(f"El mob de los 2 numeros es {mob}")
else:
    print("Esa operacion no existe:")