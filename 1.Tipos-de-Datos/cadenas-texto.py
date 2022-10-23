mi_cadena = "hola mundo"
# len para ver la longitud
print(len(mi_cadena))
# slicing para agarrar elementos [:]
print(mi_cadena[::])
# propiedades y metodos de cadenas
name = ("pam")
ultimas_letras = name[1:]
print("p" + ultimas_letras)
letra = "z"
letra = letra * 10
print(letra)
# .split para separa palabras
x = "hola|mundo"
x = x.split("|")
print(x)
# formato de impresion en cadena de texto
# {}.format sirve para agg elementos en una cadena de texto
print("esta {0} {1} {2}".format("es", "una", "cadena"))
print("esta {c} {u} {c}".format(e="es", u="una", c="cadena"))
resultados = 100/888
print("los resultados son:{r:1.5f}".format(r=resultados))

nombre = "Brian"
edad = 18
print(f"la de edad de {nombre} es:  {edad} años")
