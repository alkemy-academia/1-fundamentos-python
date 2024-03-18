# Ejercicio 6
# Escribir un programa que solicite al Usuario que ingrese el nombre de su hijo.
# Posteriomente, preguntar al Usuario
# si desea continuar para volver a solicitor el ingreso del nombre de otro hijo.
# Una vez que el usuario indique que NO desea continuar, mostrar todos los nombres ingresados.

continuar = True
hijos = []
while continuar:
    hijo = input('Ingresa nombre de tu hijo: ')
    hijos.append(hijo)
    x = input('Desea continuar? S / N: ')
    # la funcion lower() convierte todos los carateres a minuscula
    if x.lower() != 's':
        continuar = False

print('Tus hijos son:')
for hijo in hijos:
    print(hijo)
