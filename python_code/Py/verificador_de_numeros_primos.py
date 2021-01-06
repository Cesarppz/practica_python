def es_primo(numero):
    constante = 0
    for i in range(2, numero ):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            constante += 1
    if constante == 0:
        return True
    else:
        return False        


    

def run():
    numero = int(input("Verifica si tu número es primo: "))
    if es_primo(numero):
        print("El número es primo")
    else:
        print("El número no es primo ")    



if __name__ == '__main__':
    run()