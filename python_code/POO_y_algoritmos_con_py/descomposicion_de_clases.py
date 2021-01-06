class Personalidad:

    def __init__ (self,carisma,humor,pelo):
        self.carisma = carisma
        self.humor = humor
        self.pelo = pelo

    def descrition (self, hoby):
        if self.carisma > self.humor:
            return(f'Tiene una personalidad carismatica, su color de pelo es {self.pelo} y su hoby es {hoby}')
        else:
            return(f'Tiene una personalidad humoristica y su color de pelo es {self.pelo} y su hoby es {hoby}')


personaje = int(input("""
    Elije un personaje
    maria con 1 
    juan con 2
    """))


    

if __name__ == '__main__':
    maria = Personalidad(50,100,'Marrón')
    juan = Personalidad(100,50,'Negro')
    deporte = 'soccer'

    if personaje == 1:
        print(maria.descrition(deporte))
    else:
        print('Elije otro personaje')