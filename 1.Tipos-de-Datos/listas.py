
# * las listas usan [] y son mutables
mi_lista = ["uno", "dos,", "tres"]

otra_lista = ["cuatro", "cinco"]
nueva_lista = mi_lista + otra_lista
#!.append("") sirve para agg elementos al final de las listas
nueva_lista.append("seis")
print(nueva_lista)
print(nueva_lista[1:])
# *.pop(3) es para remover un elemento de la lista

print("item_popeado")
#! item_popeado para ver el elemento borrado de la lista
letra_lista = ["a", "z", "x", "b", "d"]
num_lista = [4, 1, 5, 7, 3]
# * .sort() sirve para ordenar una lista
letra_lista.sort()
print(letra_lista)

letra_lista.reverse()
print(letra_lista)
# * .reverse() sirve para ordenar listas en reversa
num_lista.sort()
print(num_lista)

num_lista.reverse()
print(num_lista)

#* forma rapida de crear una lista 
mi_lista1 = [x for x in range(0,11)]
print(mi_lista1)

celsius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32)for temp in celsius]
print(fahrenheit)