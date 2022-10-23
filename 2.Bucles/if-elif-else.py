
from random import shuffle
#* para importar algo al cmd de forma aleatoria

from random import randint, shuffle
#*para importar un numero random entero

hambre = True
sed = True

if hambre and not sed:
    print("tenemos hambre")
elif hambre == True and sed == True:
    print("tenemos hambre y sed")
else:
    print("no tenemos hambre")

años = 18
nombre = "brian"
if años < 18:
    print(f"{nombre} usted es menor de edad")
elif años >= 18:
    print(f"{nombre} usted es mayor de edad")


milista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
milista2 = ["a", "b", "c"]
di = {"k1": 1}
milista3 = [100, 200, 300]

if "k1" in di:
    print("verdadero")

#* imprimir el valor minimo y maximo
print(min(milista1))
print(max(milista1))

(shuffle(milista1))
randint(0,100)