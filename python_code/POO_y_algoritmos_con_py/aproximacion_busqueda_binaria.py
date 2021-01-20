# busqueda = int(input("pon el numero "))
# epsilon = 0.01
# paso = epsilon**2
# respuesta= 0.0

# while abs(busqueda - respuesta**2) >= epsilon:
#     respuesta += paso
#     print(paso)

# if abs(busqueda - respuesta**2) >= epsilon:
#     print(f'{busqueda} no tiene raiz cuadrada')
# else:
#     print(f'La raiz cuadrada de {busqueda} es {respuesta}')       
#      Aproximación de soluciones !!!!!

busqueda = int(input('Di un número ' ))
epsiolon= 0.001
bajo = 0.0
alto = max(1.0, busqueda)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - busqueda) >= epsiolon:
    print(alto,bajo,respuesta)
    if respuesta**2 > busqueda:
        alto = respuesta
    else:
        bajo = respuesta

    respuesta = (alto + bajo) / 2
print(f'La raiz de {busqueda} es {respuesta}')             