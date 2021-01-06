import random 


def busqueda_binaria(lista,comienzo,final,busqueda,contador_iteration=0):
    
    # print(f'El {busqueda} esta entre {lista[comienzo]} y {lista[final-1]}')

    contador_iteration += 1
    
    if comienzo > final:
        return (False,contador_iteration)
    
    medio = (comienzo + final) // 2 

    if lista[medio] == busqueda:
        return (True,contador_iteration)
    elif lista[medio] > busqueda:
        return busqueda_binaria(lista,comienzo,medio - 1 ,busqueda,contador_iteration=contador_iteration)
    else:
        return busqueda_binaria(lista,medio + 1,final,busqueda,contador_iteration=contador_iteration)


if __name__ == '__main__':


    tamaño_lista = int(input(f'De qué tamaño quieres la lista ? '))
    target = int(input(f'Qúe número quieres buscar ? '))

    lista = sorted([random.randint(0,tamaño_lista + 1) for i in range(tamaño_lista)])
    
    (encontrado,iteraciones) = busqueda_binaria(lista,0,len(lista),target)
    
    print(lista)

    
    respuesta = print(f'El número {target} {"se encuentra en la lista" if encontrado else "no se encuentra en la lista"} la cantidad de iteraciones son {iteraciones}')