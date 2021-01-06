import random
from bokeh.plotting import show,figure 

# def grafica(prob_5,prob_12):
    
#     plot = figure(plot_width=300, plot_height=300)
#     plot.vbar(x=[1,2], width=0.5, bottom=0, top=[prob_5,prob_12,100], color="#CAB2D6")

#     show(plot)


def tiros_dado(tiros):
    resultado = []

    for _ in range(tiros):
        tiro_dado = random.choice([1,2,3,4,5,6])
        tiro_dado2 = random.choice([1,2,3,4,5,6])
        resultado.append(tiro_dado + tiro_dado2)
    # print(resultado)
    return resultado

def main(cantidad_simulaciones,cantidad_tiros):
    resultados_simulaciones = []

    for _ in range(cantidad_simulaciones):
        tiros = tiros_dado(cantidad_tiros)
        resultados_simulaciones.append(tiros)

    tiros_de_doce = 0
    for numero in resultados_simulaciones:
        if 12 in numero:
            tiros_de_doce += 1

    tiros_de_cinco = 0
    for numero in resultados_simulaciones:
        if 5 in numero:
            tiros_de_cinco += 1
    
    # print(resultados_simulaciones)
    probabilidad_del_cinco = tiros_de_cinco / cantidad_tiros
    probabilidad_del_doce = (tiros_de_doce / cantidad_tiros)

    print(f'La probabilidad de que aparezca un 5 en {cantidad_tiros} tiros es de {probabilidad_del_cinco}')
    print("___"*20)
    print(f'La probabilidad de que aparezca un 12 en {cantidad_tiros} tiros es de {probabilidad_del_doce}')
    
    # grafica_probabilidad = grafica(round(probabilidad_del_cinco,1),round(probabilidad_del_doce,1)) 


if __name__ == '__main__':
    cantidad_tiros = int(input(f'Cúantas veces quieres tirar el dado? '))
    cantidad_simulaciones = int(input(f'Cúantas veces quieres simular el programa? '))

    main(cantidad_simulaciones,cantidad_tiros)