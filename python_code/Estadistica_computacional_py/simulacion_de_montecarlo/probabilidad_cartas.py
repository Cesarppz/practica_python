import random 
import collections

VALORES = ['as','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez','jota','reina','rey']
PALOS = ['Trebol','Corazon','Espada','Rombo']

def crear_baraja():
    cartas = []
    for palo in PALOS:
        for valor in VALORES:
            cartas.append((palo,valor))
    
    return cartas


def obtener_mano(cartas,tamaño_mano):
    mano = random.sample(cartas,tamaño_mano)

    return mano


def main(tamaño_mano,simulaciones):
    baraja = crear_baraja()
    manos = []
    
   
    for _ in range(simulaciones):
        mano = obtener_mano(baraja,tamaño_mano)
        manos.append(mano)
    # print(manos)
    pares = 0
    escalera = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
        
        counter = dict(collections.Counter(valores))
        # print(counter)
       
        for val in counter.values():
            if val >= 2:
                pares+=1
                break

   
    probabilidad_pares= pares/simulaciones
    probabilidad_escalera = escalera/simulaciones

    print(f'La probabilidad de encontrar un par en una tamaño de {tamaño_mano} cartas es de {probabilidad_pares}')
    print(f'La probabilidad de encontrar una escalera en una tamaño de {tamaño_mano} cartas es de {probabilidad_escalera}')

if __name__ == '__main__':
    tamaño_mano = int(input(f'Cúantas cartas quieres?: '))
    simulaciones = int(input(f'Cúantas veces vas a correr la simulación?: '))    
    
    main(tamaño_mano,simulaciones)
    
# import random
# import collections

# palos = ['espada','corazon','trebol','diamante']
# valores = 'A23456789BJQK'

# def crear_baraja():
#     baraja = []
#     for palo in palos:
        
#         for valor in valores:
#             if valor == 'B':
#                 valor = '10'
#             baraja.append((palo,valor))
#     return baraja

# def obtener_mano(baraja,tamanno_mano):
#     return random.sample(baraja,tamanno_mano)

# def coincidencias(mano,tamanno_coincidencia):
#     num_coincidencias = 0
#     valores = []
#     for carta in mano:
#         valores.append(carta[1])
#     counter = dict(collections.Counter(valores))
#     for i in counter.values():
#         if i == tamanno_coincidencia:
#             num_coincidencias += 1
#     return num_coincidencias

# def escalera(mano):
#     valores = []
#     for carta in mano:
#         valores.append(carta[1])
#     for i,val in enumerate(valores):
#         if val == 'A':
#             valores[i] = 1
#         elif val == 'J':
#             valores[i] = 11
#         elif val == 'Q':
#             valores[i] = 12
#         elif val == 'K':
#             valores[i] = 13
#         else:
#             valores[i] = int(val)
#     valores = sorted(valores)
#     escalera = True
#     for i in range(len(valores)-1):
#         if i == 0:
#             if valores[0]==1 and valores[len(valores)-1]==13:
#                 pass
#         elif valores[i]+1 != valores[i+1]:
#             escalera = False
#             break
#     return escalera

# def color(mano):
#     palos = []
#     for carta in mano:
#         palos.append(carta[0])
#     coincidence = True
#     for i in range(len(palos)-1):
#         if palos[i] != palos[i+1]:
#             coincidence = False
#     return coincidence

# def probabilidad_pares(intentos,baraja,tamanno_mano):
#     count = 0
#     for _ in range(intentos):
#         mano = obtener_mano(baraja,tamanno_mano)
#         if coincidencias(mano,2):
#             count += 1
#     return count/intentos

# def probabilidad_un_par(intentos,baraja,tamanno_mano):
#     count = 0
#     for _ in range(intentos):
#         mano = obtener_mano(baraja,tamanno_mano)
#         if coincidencias(mano,2)==1:
#             count += 1
#     return count/intentos

# def probabilidad_dos_pares(intentos,baraja,tamanno_mano):
#     count = 0
#     for _ in range(intentos):
#         mano = obtener_mano(baraja,tamanno_mano)
#         if coincidencias(mano,2)==2:
#             count += 1
#     return count/intentos

# def probabilidad_trio(intentos,baraja,tamanno_mano):
#     count = 0
#     for _ in range(intentos):
#         mano = obtener_mano(baraja,tamanno_mano)
#         if coincidencias(mano,3):
#             count += 1
#     return count/intentos

# def probabilidad_escalera(intentos,baraja,tamanno_mano):
#     count = 0
#     for _ in range(intentos):
#         mano = obtener_mano(baraja,tamanno_mano)
#         if escalera(mano):
#             count += 1
#     return count/intentos

# def probabilidad_color(intentos,baraja,tamanno_mano):
#     count = 0
#     for _ in range(intentos):
#         mano = obtener_mano(baraja,tamanno_mano)
#         if color(mano):
#             count += 1
#     return count/intentos

# def probabilidad_full(intentos,baraja,tamanno_mano):
#     count = 0
#     for _ in range(intentos):
#         mano = obtener_mano(baraja,tamanno_mano)
#         if coincidencias(mano,2) and coincidencias(mano,3):
#             count += 1
#     return count/intentos

# def probabilidad_poquer(intentos,baraja,tamanno_mano):
#     count = 0
#     for _ in range(intentos):
#         mano = obtener_mano(baraja,tamanno_mano)
#         if coincidencias(mano,4):
#             count += 1
#     return count/intentos

# def probabilidad_esc_color(intentos,baraja,tamanno_mano):
#     count = 0
#     for _ in range(intentos):
#         mano = obtener_mano(baraja,tamanno_mano)
#         if escalera(mano) and color(mano):
#             count += 1
#     return count/intentos

# def probabilidad_esc_real(intentos,baraja,tamanno_mano):
#     count = 0
#     for _ in range(intentos):
#         mano = obtener_mano(baraja,tamanno_mano)
#         real = False
#         for i,j in mano:
#             if j == 'A':
#                 real = True
#         if escalera(mano) and color(mano) and real:
#             count += 1
#     return count/intentos

# if __name__ == "__main__":
#     baraja = crear_baraja()
#     intentos = 100000
#     tamanno_mano = 5
#     print(f'Probabilidad de pares: {probabilidad_pares(intentos,baraja,tamanno_mano)}')
#     print(f'Probabilidad de un par: {probabilidad_un_par(intentos,baraja,tamanno_mano)}')
#     print(f'Probabilidad de dos pares: {probabilidad_dos_pares(intentos,baraja,tamanno_mano)}')
#     print(f'Probabilidad de un trio: {probabilidad_trio(intentos,baraja,tamanno_mano)}')
#     print(f'Probabilidad de una escalera: {probabilidad_escalera(intentos,baraja,tamanno_mano)}')
#     print(f'Probabilidad de un color: {probabilidad_color(intentos,baraja,tamanno_mano)}')
#     print(f'Probabilidad de un full: {probabilidad_full(intentos,baraja,tamanno_mano)}')
#     print(f'Probabilidad de un poquer: {probabilidad_poquer(intentos,baraja,tamanno_mano)}')
#     print(f'Probabilidad de una escalera de color: {probabilidad_esc_color(intentos,baraja,tamanno_mano)}')
#     print(f'Probabilidad de una escalera real: {probabilidad_esc_real(intentos,baraja,tamanno_mano)}')