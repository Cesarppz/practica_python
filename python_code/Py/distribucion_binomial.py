from math import factorial

from math import factorial


def mi_binomial2(k,n,p):
    total=0
    for i in range(k+1):
        total+=round((factorial(n)/(factorial(i)*factorial(n-i)))*(p**i)*((1-p)**(n-i)),4)
        # print(total)
    return total


def mi_binomial(k,n,p):
    return round((factorial(n)/(factorial(k)*factorial(n-k)))*(p**k)*((1-p)**(n-k)),4)


def run():
    total=0
    # numeros=[]
        
    if tipo == 1:
        total+=(mi_binomial(k,n,p))
    else:
        total+=(mi_binomial2(k,n,p))
        # numeros.append(mi_binomial2(k,n,p))
        
    # print(numeros)
    print(f'___'*20)
    print(f'la probabilidad calculada es de {total}')

if __name__ == '__main__':
    tipo=int(input(f"""Si estas buscando un solo número presiona 1
de lo contrario presiona 2
  """))
    k= int(input(f'A qué número le quieres buscar la dist binomal? '))
    n= int(input(f'Cúal es la n ? '))
    p= float(input(f'Cúal es la probabilidad ? '))

    run()




# def distribucion_binomial(k,n,p):
#     prob= []
#     for i in range(k+1):
#         distribucion_bino = (factorial(n) / (factorial(i) * factorial((n-i)))) * (p ** i) * ((1-p)** (n-i))
#         prob.append(distribucion_bino)
#     print(prob)
#     return sum(prob)


# if __name__ == '__main__':
#     resultado = distribucion_binomial(2,3,0.5)
#     print(resultado)

