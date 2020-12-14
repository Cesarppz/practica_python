import random

def password_generator():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minisculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    signos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '}', ']', ',', ';', '.', '>', '<', '~', '&', '$', '#',]
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    box = numeros + mayusculas + signos + minisculas
    box_r = []
    for i in range(15):
        factor_r = random.choice(box)
        box_r.append(factor_r)
    password = "".join(box_r)
    return password    

def run():
    generator = password_generator()
    print ("Tu contraseña es " + str(generator))


if __name__ == '__main__':
    run ()