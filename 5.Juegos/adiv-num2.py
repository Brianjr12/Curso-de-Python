import random


def adivina_el_numero(x):
    
    print("xxxxxxxxxxxxxxxxxxxx")
    print(" bienvenido al juego")
    print("xxxxxxxxxxxxxxxxxxxx")
    
    print(f" debes pensar un numero del 1 al {x}, y la computadora debera adivinarlo")

    limite_inferior = 1
    limite_superior = x
    
    respuesta = ("")
    
    while respuesta != "c":
        
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_superior


        respuesta = input(f" mi prediccion es, {prediccion}. Si es muy alta,ingresa (A). Si es muy baja ingresa (B). Si es correcta ingresa (C): ").lower()
        
        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
        
    print(f" he logrado adivinar tu numero,es el {prediccion} jugamos otra partida?")
            
            
adivina_el_numero(10)            