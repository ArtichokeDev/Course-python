# Diccionarios

diccionario = {"azul":"blue","rojo":"red", "verde":"green"}
diccionario2 = dict()

diccionario["amarillo"] = "yellow"


print(diccionario.get("azul", "No existe")) # Si existe no mostrara nada
print(diccionario.get("rosa", "No existe")) # NO existe mostrara el mensaje

print("azul" in diccionario)
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())
print(len(diccionario))

diccionario.clear()

diccionario2 = {"Artichok3": [20,1.73], "Jose":[22,1.76]}
print(diccionario)