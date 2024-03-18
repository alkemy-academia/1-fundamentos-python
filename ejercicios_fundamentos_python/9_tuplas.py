# Otras formas de crear una tupla
tupla_vacia = ()
tupla2 = tuple()

frutas = ('banana', 'naranja', 'pera', 'limon')

# se usan los mismos metodos que en lista:
print(len(frutas)) # 4
print(frutas[1]) # naranja

# Slicing de tuplas
# Se usa para obtener una subtupla especificando un rango de índices por donde comenzar
# y dónde terminar en la tupla;
# el valor de retorno será una nueva tupla con los elementos especificados.

print(frutas[0:len(frutas)])    # todos los items
print(frutas[0:])    # todos los items
print(frutas[1:3])  # No se incluye al item con indice = 3

# convertir a lista
lista_frutas = list(frutas)
print(lista_frutas)

# union de tuplas
tupla_total = frutas + ('kiwi', )
print(tupla_total)

# frutas[0] = 'sandia' # dará error porque no se permite la modificacion de item

# En este punto, accedo al elemento tipo lista y a este le agrego un elemento
x = ('a', 'b', [1, 2])
x[2].append(3)
print(x)
# indice de un elemento
print(x.index('b'))

print(frutas)
# Eliminacion tupla. No se pueden eliminar elementos pero si la tupla entera
del frutas
#print(f'Frutas eliminada: {frutas}') # dara error porque la variable frutas es indefinida
