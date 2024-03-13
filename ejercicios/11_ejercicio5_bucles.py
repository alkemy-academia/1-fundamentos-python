# Ejercicio 5
# Escribir un bucle que imprima 7 lineas cuyo resultado sea el siguiente triangulo:
    #
    ##
    ###
    ####
    #####
    ######
    #######

caracter = '#'
for i in range(1, 8):
    print(caracter)
    caracter = caracter + '#'

# En Python se puede realizar la multiplicación de cadenas de texto.
# Al multiplicar una cadena por un número entero,
# la cadena se repetirá ese número de veces.
for i in range(1, 8):
    print("#" * i)
