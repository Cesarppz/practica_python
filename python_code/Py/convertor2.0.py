def conversor(nombre_moneda, valor_dolar):
    pesos= float(input("Cuántos"+ nombre_moneda+ "Tienes? : "))
    dolares = (pesos / valor_dolar)
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tu tienes " + dolares + " $") 
    
mensaje = """ 
Elije 1 para transformar bolívares a dolares
Elije 2 para transformar pesos mexicanos a dolares
Elije 3 para transformar pesos argentinos a dolares
Elije una opción:  """
tipo_moneda = int(input(mensaje))


if tipo_moneda == 1:   
    conversor("bolivares" , 855871.44)
elif tipo_moneda == 2:
    conversor("Pesos mexicanos", 24)
elif tipo_moneda == 3:
    conversor("Pesos argentinos",65)
else:
    print("Elige una opción valida")    