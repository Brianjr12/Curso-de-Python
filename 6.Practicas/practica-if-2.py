name = input ("ingrese su nombre : ")
num = float(input ("ingrese su calificación en numero y se le asignará una letra : "))

if num >= 0 and num <= 60 :
    print (f" {name} usted esta reprobado con una calificación de F ")

elif num >= 61 and num <= 70:
    print(f" {name} usted esta reprobado con una calificación de D ")

elif num >= 71 and num <= 80 :
    print (f" {name} usted esta aprobado con una calificación de C ")

elif num >= 81 and num <= 90 :
    print (f" {name} felicidades usted esta aprobado con una calificación de B ")

elif num >= 91 and num <= 100 :
    print(f" {name} felicidades usted es un estudiante sobresaliente y esta aprobado con una calificación de A ")
