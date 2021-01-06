import random 


def run():
    numero_aleatorio = random.randint(1,100)
    variable = int(input("Elije un número del uno al 100: "))
    while numero_aleatorio != variable:
        if variable > numero_aleatorio:
            print("Busca un número menor")
        else:
            print("Busca un número mayor") 
        variable = int(input("escoge otro número: "))
    if variable == numero_aleatorio:
        print("Ganaste !!!")
    

if  __name__ == "__main__":
    run()