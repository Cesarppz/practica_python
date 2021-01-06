

class Coordenada:

    def __init__(self,x,y):
        self.x = x
        self.y = y 

    def mover(self,delta_x,delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    def distancia(self,otra_coodenada):
        distancia_x = (self.x - otra_coodenada.x)
        distancia_y = self.y - otra_coodenada.y  
        
        return (distancia_x**2 + distancia_y**2)**0.5
