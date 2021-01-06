# import random


# class Borracho:

#     def __init__(self,nombre):
#         self.nombre=nombre


# class Borracho_normal(Borracho):

#     def __init__(self,nombre):
#         super().__init__(nombre)

#     def camina(self):
#         return random.choice([(-1,0),(1,0),(0,1),(0,-1)])


import random

class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre


class Borracho_normal(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0, 1*(random.choice([1,2,3,4,5,6]))), (0, -1*(random.choice([1,2,3,4,5,6]))), (1, 0*(random.choice([1,2,3,4,5,6]))), (-1, 0*(random.choice([1,2,3,4,5,6])))])