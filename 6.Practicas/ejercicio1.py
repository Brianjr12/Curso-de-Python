
#* pedir 10 numeros por teclado. sumarlos y mostrar en la pantalla
suma = 0
for n in range(0,10):
    numero = int(input("introduce un número: "))
    suma = suma + numero
print (f"la suma es {suma}")