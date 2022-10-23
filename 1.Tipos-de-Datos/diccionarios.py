
#*diccionarios se usa{}

mi_diccionario = {"llave1" : "valor1", "llave2" : "valor2"}
print(mi_diccionario["llave1"])
frutas = {"manzanas" : "2.90", "agua" : "2.90", "leche" : "5.90" }
print(frutas["manzanas"])
#ejemplo de diccionarios con listas 
dicc_lista = {"manzanas": "2.90", 'kekes' : ['manzana', 'platano'], "leche": "5.90"}
print(dicc_lista)
print(dicc_lista['kekes'][1])
dicc_lista["gaseosa"] = 300
print(dicc_lista)
#* para ver las llaves en un diccionario se usa .keys()
print(dicc_lista.keys())
#* .values() para ver lo contrario de keys
print(dicc_lista.values())
#* .items() para verlos separados
print(dicc_lista.items())