def check (palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palindromo = palabra[::-1]
    if palindromo == palabra:
        return True
    else:
        return False 
        


def run ():
    palabra = input("Coloca una palabra aquí: ")
    es_palindromo = check(palabra)
    if es_palindromo == True:
        print("Es un palíndromo :)")
    else :
        print("No es un palíndromo :(")


if __name__ == '__main__':
    run()