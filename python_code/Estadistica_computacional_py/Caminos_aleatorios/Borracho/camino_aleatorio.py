# from borracho import Borracho_normal
# from coordenada import Coordenada
# from campo import Campo 
# from bokeh.plotting import figure,  show


# # def graficar(x, y):
# #     # Creamos una instancia de figure, con su titulo y las etiquetas de los ejes.
# #     grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')

# #     # Ingresamos los datos de X e Y.
# #     grafica.(x, y, legend='distancia media')

# #     # Generamos una gráfica en HTML.
# #     show(grafica)


# def caminata(campo,borracho,pasos,origen):
#     inicio = campo.obtener_cordenadas(borracho)
#     cordenadas_x= []
#     cordenadas_y = []
    
#     cordenadas_x.append(origen.x)
#     cordenadas_y.append(origen.y)
   
#     for _ in range(pasos):
#         campo.mover_borracho(borracho)
#         a = campo.obtener_cordenadas(borracho).x
#         b = campo.obtener_cordenadas(borracho).y
#         cordenadas_x.append(a)
#         cordenadas_y.append(b)

#     return (cordenadas_y,cordenadas_x,inicio.distancia(campo.obtener_cordenadas(borracho)))


# def simular_caminata(pasos,numero_de_intentos,tipo_de_borracho):
#     borracho = tipo_de_borracho(nombre='César')
#     origen = Coordenada(0,0)
#     distancias = []
#     # A continuación voy a colocar el borracho en el campo con los valores antes definidos 
#     #Esto lo voy a hacer las veces que tenga en el número de intentos 
#     for _ in range(numero_de_intentos):
#         campo = Campo()
#         campo.añadir_borracho(borracho,origen)
#         (puntos_x,puntos_y,simular_caminata) = caminata(campo,borracho,pasos,origen)
#         distancias.append(round(simular_caminata,1))
    
#     # graficar(puntos_x,puntos_y)
    
#     return distancias

# # def graficar(x, y):
# #     # Creamos una instancia de figure, con su titulo y las etiquetas de los ejes.
# #     grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')

# #     # Ingresamos los datos de X e Y.
# #     grafica.line(x, y, legend='distancia media')

# #     # Generamos una gráfica en HTML.
# #     show(grafica)

# def main(distancia_a_caminar,numero_de_intentos,tipo_de_borracho):
#     # Donde comienza a correr el codigo 
#     distancias_media_por_caminata = []
#     for pasos in distancia_a_caminar:
#         distancias = simular_caminata(pasos,numero_de_intentos,tipo_de_borracho)
#         distancia_max = max(distancias)
#         distancia_medium = round(sum(distancias) / len(distancias),4)
#         distancia_min = min(distancias)
#         distancias_media_por_caminata.append(distancia_medium)
#         print(f'{tipo_de_borracho.__name__} tuvo una caminata de {pasos} pasos')
#         print(f'Media = {distancia_medium}')
#         print(f'Distancia Max = {distancia_max}')
#         print(f'Distancia Min = {distancia_min}')
#         print(f'_'*30)
    
#     # graficar(distancia_a_caminar, distancias_media_por_caminata)


# if __name__ == '__main__':
#     distancia_a_caminar = [1000,10000,100000]
#     numero_de_intentos = 10
    
#     main(distancia_a_caminar,numero_de_intentos,Borracho_normal)


