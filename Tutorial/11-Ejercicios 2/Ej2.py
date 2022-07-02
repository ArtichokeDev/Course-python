
lista1 = [1,2,3,4,5,6,7,8,9,1,5]
lista2 = [4,6,7,8,9,2,3,1,2,8,9,1,5]

a = set(lista1)
b = set(lista2)
print(f"lista1 UNION lista2: {list(a.union(b))}")
print(f"lista1 MENOS lista2: {list(a.difference(b))}")
print(f"lista2 MENOS lista1: {list(b.difference(a))}")
print(f"lista 1 INTERSECCION lista2: {list(a.intersection(b))}")
