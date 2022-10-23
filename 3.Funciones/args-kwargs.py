def suma(num1, num2):
    total = num1 + num2
    print (total)

suma(1,2)

def chequear_numero_par_en_lista(num_list):
    
    for number in num_list:
        if number % 2 == 0:
            print("true")
            return True
        
    else:
        pass
        print("false")
        return False

chequear_numero_par_en_lista([2,3,5])

#* *args, sirve para agregar mas argumentos y retorna un tupla
def func(*args):
    return print (sum(args) * 0.05)

func(40,60,760,890)

#* : **kwargs sirve como un diccionario 
def funcion(**kwargs):
    if "fruit" in kwargs:
        print("mi fruta escogida es {}".format(kwargs["fruit"]))
    else:
        print("no hay fruta")

funcion(fruit= "manzanas", veggie="lechuga")

def ambos(*args, **kwargs):
    print(args)
    print(kwargs)
    print("me gustaría {} {}".format(args[0], kwargs["comida"]))

ambos(10,30,50, comida= "leche", animal= "perro")