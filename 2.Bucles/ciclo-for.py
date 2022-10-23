
milista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
for milista_items in [5]:
    print(milista_items)

for num in milista:
    print(num)

for pares in milista:
    #* chequear numeros pares
    if pares % 2 == 0:
            print(f"numeros pares : {pares}")
    else:
            print(f"numero impar : {pares}")

suma_lista = 0
#* se suman los numeros de milista, ejem: [0+[1]=1+[2]=3+[3]=6+[4]=10+[5]=15]
for numeros in milista:
    suma_lista = suma_lista + numeros
    print(suma_lista)

#*letters por cada letra que se encuentra en la variable
for letter in "hola mundo":
    print(letter)

#*tupla adentro de una lista
milistatu = [(1,2),(3,4),(5,6),(7,8)]

#* item sirve para ver los elmentos de una lista,tupla,diccionario
#* item[un elmento de la lista] mostrara solo ese elemento

print(len(milistatu))

for item in milistatu[3]:
    print(item)

#* desempaquetando una tupla adentro de una lista
for (a,b) in milistatu:
        print(a)
        print(b)


#* bucle for con diccionario
#* imprime solo las llaves
d = {"y1":3,"y2":1,"y3":2}
for item in d:
    print(item)

#* para imprimir las llaves y su valores
d = {"y1":3,"y2":1,"y3":2}
for item in d.items():
    print(item)

#* para ver solo los valores en orden 
for llave,valor in d:
    print(valor)

#* para ver los valores en su orden 
for value in d.values():
    print(value)