# Listas

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "viernes", 40, 5.67, [1,2,3], True]

print(lista[0])
print(lista[-1])
print(lista[0:3]) #de la 0 a la 2  (0:3) de la que empieza y una posicion antes a la que pones

#Parte 2
print(len(lista))

lista.append(6)
print(lista)

list1 =[1,2,4,5]
list1.insert(2,3) # (indice, valor)

list1.extend([6,7,8]) # concatenar lista

list2 = [6,7,8]

list3 = list1 + list2

print("Artichok3" in list3)
print(list3.index(5)) # indice del valor 5
print(list3.count(7))

list3.pop() #eliminar ultimo parametro en la lista
list3.pop(2) #eliminar valor indice 2
lista.remove("Lunes")
lista.clear()
list3.reverse()
list3.sort()
list3.sort(reverse=True)
