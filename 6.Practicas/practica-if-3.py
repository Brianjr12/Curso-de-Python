
#* En una boutique de damas, si se compra un traje se le hace un descuento del 45%, si compra 2 el 50%, si compra 3 el 60% y si compra más de tres el 65%. Elabore un programa que lea la cantidad de trajes y el precio unitario e imprima el subtotal a pagar, el descuento y el total a pagar.

# input data
cant = int(input("Ingrese la cantidad de trajes que compró: "))
precio = float(input("Ingrese el precio del traje: "))
#process
if cant == 1:
    subtotal = cant*precio
    desc = subtotal* 0.45
    total = subtotal-desc
    #data output
    print(f"Por la compra de {cant} trajes usted recibió un descuento del 45%")
    print(f"su descuento en dinero es {desc} $")
    print(f"el subtotal a pagar es {subtotal} $ .Pero con el descuento ahora es de {total} $")
elif cant == 2:
    subtotal = cant*precio
    desc = subtotal* 0.50
    total = subtotal-desc
    print(f"por la compra de {cant} trajes usted recibió un descuento del 50%")
    print(f"su descuento en dinero es {desc} $")
    print(f"el subtotal a pagar es {subtotal} $ .Pero con el descuento ahora es de {total} $")
elif cant == 3:
    subtotal = cant*precio
    desc = subtotal* 0.60
    total = subtotal-desc
    print(f"por la compra de {cant} trajes usted recibió un descuento del 60%")
    print(f"su descuento en dinero es {desc} $")
    print(f"el subtotal a pagar es {subtotal} $ .Pero con el descuento ahora es de {total} $")
elif cant > 3 :
    subtotal = cant*precio
    desc = subtotal* 0.65
    total = subtotal-desc
    print(f"por la compra de {cant} trajes usted recibió un descuento del 65%")
    print(f"su descuento en dinero es {desc} $")
    print(f"el subtotal a pagar es {subtotal} $ .Pero con el descuento ahora es de {total} $")