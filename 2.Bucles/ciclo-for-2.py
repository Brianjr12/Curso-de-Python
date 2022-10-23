
#* palabras claves utiles
#* pass: para pasar una parte del ciclo
#* continue : para continuar hasta la ejecución
#* break : rompe el ciclo cuando se llegue a la condición

br = [1, 2, 3]

for item in br:
    #comment
    pass

print("fin del libreto")


nombre = "Brian"

for letter in nombre:
    if letter == "i":
        continue
    print(letter)

mama = "beatriz"
for letter in mama:
    if letter == "r":
        break
    print(letter)

#! operadores utiles

milista = [1,2,3]
#* range : funcion para crear un rango
for num in range(10):
    print(num)

#* del 0 al 10 en dos en dos
for num in range(0,11,2):
    print(num)

#* crear un rango en una lista
print(list(range(0,11,2)))


contador_indice = 0
palabra = "hola"

for letter in palabra:
    print(palabra[contador_indice])
    contador_indice += 1

for index, letter in enumerate(palabra):
    print(index)
    print(letter)
    print("\n")


milista1 = [1,2,3,4,5,6,]
milista2 = ["a","b","c"]
milista3 = [100,200,300]

#* zip : para emparejar
for item in zip(milista1,milista2,milista3):
    print(item) 

print(list(zip(milista1,milista2)))