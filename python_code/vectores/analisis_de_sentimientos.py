import numpy as np
import collections

lista = ['gran','excelente','bueno','inteligente','muerte','perdida','luto','ignorante','nacional','videos','quiero','platzi','modo','de']


def reemplazo(tweet):
    return tweet.replace("!","").replace(",","").replace("(","").replace(")","").lower().split(" ")


def vector_s(tweet):
    positivas = [tweet.count(i) for i in lista[0:4]]
    negativas = [tweet.count(i) for i in lista[4:8]]
    neutras = [tweet.count(i) for i in lista [8:]]
    vector_s = [sum(positivas), sum(neutras), sum(negativas)]

    return vector_s

def vect_score(s):
    return np.dot(np.array([1, 0, -1]),s)


def vector_w(tweet):
    vector_w = [tweet.count(i) for i in lista]
    return vector_w

def promedio_vect(w):
    return round((sum(w)/len(lista)),4)



def analisis_sentimientos(tweet1,tweet2,tweet3,tweet4):
    tweet1 = reemplazo(tweet1)
    tweet2 = reemplazo(tweet2)
    tweet3 = reemplazo(tweet3)
    tweet4 = reemplazo(tweet4)

    vector_w1 = vector_w(tweet1)
    vector_w2 = vector_w(tweet2)
    vector_w3 = vector_w(tweet3)
    vector_w4 = vector_w(tweet4)

    vector_s1 = vector_s(tweet1)
    vector_s2 = vector_s(tweet2)
    vector_s3 = vector_s(tweet3)
    vector_s4 = vector_s(tweet4)

    promedio1 = promedio_vect(vector_w1)
    promedio2 = promedio_vect(vector_w2)
    promedio3 = promedio_vect(vector_w3)
    promedio4 = promedio_vect(vector_w4)

    score1 = vect_score(vector_s1)
    score2 = vect_score(vector_s2)
    score3 = vect_score(vector_s3)
    score4 = vect_score(vector_s4)

    calidad_media = round((promedio1 + promedio2 + promedio3 + promedio4)/4,4)

    
    tweet_positivo = max(score1,score2,score3,score4)

    if tweet_positivo == score1:
        respuesta="Tweet 1"
    elif tweet_positivo == score2:
        respuesta="Tweet 2"
    elif tweet_positivo == score3:
        respuesta="Tweet 3"
    else:
        respuesta="Tweet 4"


    tweet_negativo = min(score1,score2,score3,score4)

    if tweet_negativo == score1:
        respuesta2="Tweet 1"
    elif tweet_negativo == score2:
        respuesta2="Tweet 2"
    elif tweet_negativo == score3:
        respuesta2="Tweet 3"
    else:
        respuesta2="Tweet 4"
 

    print(f""" 
El tweet más positivo es el {respuesta} y el más negativo es el {respuesta2}. 
Por otra parte la insertidumbre de los 4 tweets es de {calidad_media}.
Cada tweet tiene una insertidumbre de:
    1: {promedio1}
    2: {promedio2}
    3: {promedio3}
    4: {promedio4}
:) """)
    

    
    

    #counter = dict(collections.Counter(tweet))
    # palabras_repetidas = []
    # for name,val in counter.items():
    #     if val >= 2:
    #         palabras_repetidas.append(name)
    # print(palabras_repetidas)


if __name__ == '__main__':
    tweet1 = 'Gran mexicano y excelente en su área, su muerte es una enorme perdida y debería ser luto nacional!!! '
    
    tweet2=  'Vaya señora que bueno que se asesora por alguien inteligente no por el ignorante del Gatt. '
    
    tweet3 = 'Se me ocurre y sin ver todos los videos de Plazti que me informéis por dónde empiezo. Entiendo que os tendría que decir quién soy y que quiero, vamos conocerme para asesorarme bien. Un saludo '
    
    tweet4 = 'Soy docente universitario, estoy intentando preparar mis clases en modo platzi bien didáctico, (le llamo modo noticiero), descargue una plataforma gratuita de grabación y transmisión de vídeo, se llama Obs estudio! bueno la sigo remando con sus funciones pero sé que saldrá algo!'
    
    analisis_sentimientos(tweet1,tweet2,tweet3,tweet4)

    

# Vaya señora que bueno que se asesora por alguien inteligente no por el ignorante del Gatt.

# Se me ocurre y sin ver todos los videos de Plazti que me informéis por dónde empiezo. Entiendo que os tendría que decir quién soy y que quiero, vamos conocerme para asesorarme bien. Un saludo

# Soy docente universitario, estoy intentando preparar mis clases en modo platzi bien didáctico, (le llamo modo noticiero), descargue una plataforma gratuita de grabación y transmisión de vídeo, se llama Obs estudio!bueno la sigo remando con sus funciones pero sé que saldrá algo!