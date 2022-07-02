#Tuplas
#No podemos modificar nada de una tupla
tupla = (4, "Hola", 6.78, [1,2,3])

# tupla.append(5) ERROR
# tupla[0] = 8 ERROR

print(tupla)
print(4 in tupla)
print(tupla.index(4)) # indice del valor 5
print(tupla.count(6.78))
print(len(tupla))

#pasar de tupla a lista
lista = list(tupla)
#pasar de lista a tupla
tupla2 = tuple(lista)
