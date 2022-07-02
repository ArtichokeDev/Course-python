# Conjunto Parte 2
a = frozenset({1,2,3}) #conjunto inmutable no se puede modificar
b = {3,4,5}

print(a == b)
print(len(a))

c = a | b #Union 2 conjunto
print(c)

c = a & b #Interseccion 2 conjunto
print(c)

c = a - b #Diferencia 2 conjunto
print(c)

c = a ^ b #Diferencia Simetrica 2 conjunto
print(c)

c = {1,2,3,4,5}
print(a.issubset(c)) #Subconjunto
print(c.issuperset(a)) #Super conjunto
print(a.isdisjoint(b))

