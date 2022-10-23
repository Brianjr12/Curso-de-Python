list_numeros = [1,2,3,4,5,6,7]
#* lambda: cuando usamos otras funciones, es una manera de usar funciones juntas ejempl (map y filter)
square = lambda num: num **2

#* imprimiendo un numero al **2
print(square(8))

#* haciendo una lsita con los numeros elevados al **2 de list_numeros
print(list(map(lambda num: num ** 2,list_numeros)))
#* filtrando list_numeros, en numeros par
print(list(filter(lambda num: num %2 ==0,list_numeros)))