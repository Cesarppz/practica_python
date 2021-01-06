import random

def lista_ordenada(lista):
    
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j],lista[j+1] = lista[j+1],lista[j] 
    return lista

if __name__ == '__main__':

    tamaño_l = int(input(f'De que tamaño va a ser la lista? '))
    # busqueda = int(input(f'Qué número vas a buscar? '))
    
    lista = [random.randint(0,100) for i in range(tamaño_l)]    
    print(lista)
    
    lista_ord = lista_ordenada(lista)
    print(lista_ord)
    