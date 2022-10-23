

#* son funciones adentro de funciones
#global
varglb = "variable global"

#* si la variable se encuentra adentro de un funcion solo esa puede usar la variable y sino la pueden usar las demas funciones


def saludo():
    #* enclosing : porque se encuentra medio de dos funciones
    name1 = "brian ojeda"

    def hola():
        #local
        varlc = "variable local"
        print("hola " + name1)
    hola()


saludo()


#* como reasignar variables
# variable global
b = 50

def func(b):
#* re asignación local variable
    b = 200
    print(f"fue localmente cambiada de b a {b}")

func(b)
#* re asignación globalmente
x = 50
def func ():
    global x 
    print(f"x es {x}")
    #* re asignación local
    x = "nuevo valor"
    print(f" fue localmente cambiada de x a {x}")

func()
print(x)

