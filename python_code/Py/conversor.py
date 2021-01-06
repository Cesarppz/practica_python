mensaje = """ Elije una opción
Elije 1 para transformar bolívares a dolares
Elije 2 para transformar pesos mexicanos a dolares
Elije 3 para transformar pesos argentinos a dolares
"""
respuesta = int(input(mensaje))

def nombre_moneda(signo):
    cantidad = float(input("Cuantos " + signo + "tienes? : "))


def resultado(valor_moneda):
    valor = (valor_moneda)
    dolares = nombre_moneda / valor
    dolares = round(dolares, 2)
    dolares = str(dolares)
    return dolares

if respuesta == 1:
    nombre_moneda(bolivares)
    resultado(855871.44)
    print("Tu tienes " + resultado + "$" )

