import random
import math

# def distribucion_normal(X,mu,sigma):
#     valores_y = []
#     for x in X:
#         y = (1/(sigma*math.sqrt(2*math.pi)))*math.exp(-1/2*((x-mu)/(sigma))**2)
#         valores_y.append(y)

#     return valores_y

def media(X):
    return (sum(X)/len(X))


def varianza(X):

    contador = 0
    for x in X:
        contador += (x - media(X))**2
    
    return contador / len(X)

def desviacion_estandar(X) :
    return math.sqrt(varianza(X))


if __name__ == '__main__':
    X = [random.randint(1,21) for i in range(20)]
    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)

    print(f'La media de {X} es de {mu}')
    print("__"*20)
    print(f'La varianza de {X} es de {Var}')
    print("__"*20)
    print(f'La desviación estándar de {X} es de {sigma}')


    