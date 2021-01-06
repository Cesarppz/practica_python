iteraciones = 0

def morral(tamaño_morral,peso,valor,n):
    
    global iteraciones
    iteraciones += 1
    
    if n == 0 or tamaño_morral == 0:
        return 0
    
    if peso[n-1] > tamaño_morral:
        return morral(tamaño_morral,peso,valor, n - 1)
    
    maximo= max(valor[n -1] + morral(tamaño_morral - peso[n -1],peso , valor, n-1),morral(tamaño_morral, peso , valor, n-1))
    print(str(iteraciones),"-" * 10 + str(maximo))
    return maximo


if __name__ == '__main__':
    tamaño_morral = int(input(f'De que tamaño es el morral? '))
    valor = [200,100,50,25]
    peso = [40,20,10,5]
    n = len(valor)

    respuesta = morral(tamaño_morral,peso,valor,n)
    print(f'El mayor valor que puedes llevar en un morral de {tamaño_morral} es de {respuesta}')
    print("_" * 30)
    print(iteraciones)