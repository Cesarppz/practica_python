import time
import sys


def fivonachi(n,memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        valor = (fivonachi(n -1,memo) + fivonachi (n - 2,memo))
        memo[n] = valor
        print(memo)
        return valor 


def run():
    sys.setrecursionlimit(1002)
    n = int(input(f'Ingresa el número: '))
    respuesta = fivonachi(n)
    
    print(respuesta)
    print(time.time())
    

if __name__ == '__main__':
    run()
    


#     import sys

# def fibonacci_recursivo(n):
#     if n == 0 or n == 1:
#         return 1

#     return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# def fibonacci_dinamico(n, memo = {}):
#     if n == 0 or n == 1:
#         return 1

#     try:
#         return memo[n]
#     except KeyError:
#         resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
#         memo[n] = resultado

#         return resultado

# if __name__ == '__main__':
#     sys.setrecursionlimit(10002)
#     n = int(input('Escoge un numero: '))
#     resultado = fibonacci_dinamico(n)
#     print(resultado)