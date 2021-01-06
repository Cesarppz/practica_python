# import time 
# import sys

# def factorial(n):
#     respuesta = 1
#     while n > 1:
#             respuesta *= n
#             n -=1
            
#     return respuesta
    
# def factorial_r(n):
#     if n == 1:
#         return 1  
#     return n*factorial_r(n-1)

# if __name__=='__main__':
#     n=2000
#     sys.setrecursionlimit(100000)

#     comienzo= time.time()
#     factorial(n)
#     final= time.time()
#     print(final - comienzo)

#     comienzo1=time.time()
#     factorial_r(n)
#     final1=time.time()
#     print(final1 - comienzo1)
# def f(x):
#     respuesta = 0

#     for i in range(x):
#         for f in range(x):
#             print(i,f)
#             respuesta += 1
#             respuesta += 1
#     return(f'esta es la {respuesta}')

# if __name__ == '__main__':
#     x=5
#     print(f(x))


import random


def busqueda_lineal(lista,busqueda):
    
    contador_iteration = 0
    match = False
    
    for i in lista:
        contador_iteration += 1
        if i == busqueda:
            match = True
            break

    return (match,contador_iteration)


if __name__ == '__main__':

    tamaño_l = int(input(f'De que tamaño va a ser la lista? '))
    busqueda = int(input(f'Qué número vas a buscar? '))
    lista = [random.randint(0,100) for i in range(tamaño_l)]    
    (encontrado,iterations) = busqueda_lineal(lista,busqueda)

    
    print(lista)
    print(f"""El número {busqueda} {"esta" if encontrado else "no esta"} en la lista
    La cantidad de iteration : {iterations}""") 
