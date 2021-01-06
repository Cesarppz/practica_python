import random


def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):                                                          # Código hecho por el prófesor  
        valor_actual = lista[indice]                                                 
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual


def insercion(lista):                                                                             # Código hecho por mi :)
   
    for indice in range(1,len(lista)): 
        valor_buscado = lista[indice]
        comparacion = indice-1

        while comparacion > 0 and valor_buscado < lista[comparacion]:

            valor_buscado = lista[indice - 1]
            comparacion += 1

        valor_buscado = lista[comparacion]

        return lista


if __name__ == '__main__':

    tamaño_lista = int(input(f'De cuanto quieres la lista? '))
    lista = [random.randint(0,100) for i in range(tamaño_lista)]
    print(lista)
    
    resultado = insercion(lista)

    print(resultado)