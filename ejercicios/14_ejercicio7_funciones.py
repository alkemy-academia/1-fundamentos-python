# Escribir una función que verifique que todos los items de una lista sean del mismo tipo:

def verificar_tipo(lista):
    tipo_dato = type(lista[0])

    for item in lista:
        if not isinstance(item, tipo_dato):
            return False

    return True


lista1 = [1, 2, 3]
print(f'Lista1 tiene todos sus elementos del mismo tipo?: {verificar_tipo(lista1)}')

lista2 = ['f', 'r', 1, True]
print(f'Lista2 tiene todos sus elementos del mismo tipo?: {verificar_tipo(lista2)}')