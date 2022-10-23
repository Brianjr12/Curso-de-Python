
#* init : sirve para poder definir los atributos que vamos a poder usar adentro de nuestra clase
class perros(): 
    
    def __init__(self,raza,nombre,puntos):
        
        #atributos
        self.raza =raza
        self.nombre = nombre
        #esperamos valor booleano true o false
        self.puntos = puntos
        
huskie = perros(raza= "huskie", nombre= "sam",puntos= False) 


#! Herencias y polimorfismo
#* esto su usa para crear una clase con una clase ya definida basada en la clase ya definida en forma de herencia

class Animal():
    def __init__(self,):
        print("animal creado")
        
        def quien_soy(self):
            print("soy un animal")
            
            def comer(self):
                print("estoy comiendo")
                
class Perro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("perro creado")
        
    def quien_soy(self):
            print("soy un perro")

