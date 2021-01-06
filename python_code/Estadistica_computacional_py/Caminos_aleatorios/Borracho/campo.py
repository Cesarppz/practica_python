

class Campo:

    def __init__(self):
        self.donde_esta_el_borracho = {}

    def añadir_borracho(self,borracho,coordenada):
        self.donde_esta_el_borracho[borracho]=coordenada

    def mover_borracho(self,borracho):
        delta_x,delta_y = borracho.camina()
        ubicaion_actual = self.donde_esta_el_borracho[borracho]
        nueva_ubicacion = ubicaion_actual.mover(delta_x,delta_y)
        self.donde_esta_el_borracho[borracho]= nueva_ubicacion
    
    def obtener_cordenadas(self,borracho):
        return self.donde_esta_el_borracho[borracho]