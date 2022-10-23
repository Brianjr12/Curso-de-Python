
#* square: al cuadrado
numeros = [1,2,3,4,5]
def square (num):
    result = num**2
    return result

#* map: map() ejecuta una función sobre cada uno de los elementos de un iterador (generalmente una lista o tupla) y retorna un nuevo iterador cuyos elementos son el resultado de dicha operación.
for item in map(square,numeros):
    print(item)

#* hacer lo mismo pero impreso en lista
print(list(map(square,numeros)))

num_lista = [1,2,3,4,5,6,7]
#* check_even para chequear si hay numeros pares
def check_even(num):
    return num % 2 == 0

#* filter para filtrar elementos
for n in filter(check_even,num_lista):
    print(n)