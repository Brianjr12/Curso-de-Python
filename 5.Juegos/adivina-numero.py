import random


def adivina_el_numero(x):
    
    print("==========================")
    print("Bienvenido(a) al juego")
    print("==========================")
    print(" tu meta es adivinar el número generado por la computadora")
    
    numero_aleatorio = random.randint(1, x) # numero aleatorio entre 1 y X
    
    prediction = 0
    
    while  prediction != numero_aleatorio:
    
        prediction = int(input(f" adivina un número entre 1 y {x}: "))
        if prediction < numero_aleatorio:
            print(f" intenta otra vez. {prediction} es muy pequeño")
        elif prediction > numero_aleatorio:
            print(f"intenta otra vez. {prediction} es muy grande")
        
    print(f" felicitaciones.Adivinaste el número {numero_aleatorio} correctamente")          
        
            
            
adivina_el_numero(30)