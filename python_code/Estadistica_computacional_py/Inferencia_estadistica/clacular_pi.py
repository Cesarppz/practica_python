import random
from estadistica import media, desviacion_estandar
from bokeh.plotting import show,figure,output_file

def lanzar_agujas(numero_de_agujas):
    adentro_del_circulo = 0
    
    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([1,-1])
        y = random.random() * random.choice([1,-1])
        distancia_aguja=(x**2 + y**2)**0.5

        if distancia_aguja <= 1:
            adentro_del_circulo +=1
    # se devuleve el cálculo de pi según el número de agujas que caen adentro del circulo
    return (adentro_del_circulo*4)/numero_de_agujas

def estimacion(numero_de_agujas,numero_intentos):
    estimados = []

    for _ in range(numero_intentos):
        estimacion_pi = lanzar_agujas(numero_de_agujas)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'Est={round(media_estimados,5)} sigma={round(sigma,5)} Agujas lanzadas = {numero_de_agujas}')

    return (media,sigma)

    
def estimar_pi(precision,numero_intentos):
    numero_de_agujas = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        media,sigma = estimacion(numero_de_agujas,numero_intentos)
        numero_de_agujas *= 2

    return media


if __name__ == '__main__':
    estimar_pi(0.01,1000)
 