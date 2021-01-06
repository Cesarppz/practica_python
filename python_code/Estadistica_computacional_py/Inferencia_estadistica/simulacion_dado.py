import random
import collections
import math
from bokeh.plotting import show,figure,output_file 
from estadistica import media, desviacion_estandar


def grafica(x,y,media_tiros):
    
    plot = figure(title='media dado',x_axis_label='Númeors',y_axis_label='Valores')
    plot.vbar(x,top=y,width=0.5,color="#46f2d3")
    
    x_media = media(media_tiros)
    y_media = [min(media_tiros),max(media_tiros)]
    plot.line(x_media,y_media,color='red',legend='media',line_width=3)
    
    # plot.line(x,distribucion_normal,color="green",title='distribución normal')
    
    
    output_file("Media.html")

    show(plot)

# def distribucion_normal(X,mu,sigma):
#     valores_y = []
#     for x in X:
#         y = (1/(sigma*math.sqrt(2*math.pi)))*math.exp(-1/2*((x-mu)/(sigma))**2)
#         valores_y.append(y)

#     return valores_y

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
    media_tiros = []
    sigmas = []
    # distribucion_normal_tiro=[]

    for _ in range(cantidad_simulaciones):
        tiros = tiros_dado(cantidad_tiros)
        resultados_simulaciones.append(tiros)
    
        media_tiro=media(tiros)
        sigma = desviacion_estandar(tiros)
        media_tiros.append(media_tiro)
        sigmas.append(sigma)
        # distribucion_tiros = distribucion_normal(tiros,media_tiro,sigma)
        # distribucion_normal_tiro.append(distribucion_tiros) 
    
    counter = dict(collections.Counter(media_tiros))
    # print(counter)
    x=list(counter.keys())
    y=list(counter.values())

  

    grafica(x,y,media_tiros)

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
    print("___"*20)
    print(f'Media = {media(media_tiros)} con una desviación estándar de {media(sigmas)}')
    
    # grafica_probabilidad = grafica(round(probabilidad_del_cinco,1),round(probabilidad_del_doce,1)) 


if __name__ == '__main__':
    cantidad_tiros = int(input(f'Cúantas veces quieres tirar el dado? '))
    cantidad_simulaciones = int(input(f'Cúantas veces quieres simular el programa? '))

    main(cantidad_simulaciones,cantidad_tiros)