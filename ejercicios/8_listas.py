# Otras formas de crear una lista
lista1 = list()
lista2 = []

# Lista de nombres
nombres = ["Julio", "Micaela", "Santiago", "Gino"]

# Consultar tamaño de la lista
print(f'Tamaño de lista nombres: {len(nombres)}')

# Acceder e Imprimir primer nombre
print(nombres[0]) # Julio

# Add a new name
nombres.append("Valeria") # ["Julio", "Micaela", "Santiago", "Gino", "Valeria"]
print(nombres[-1]) # Valeria

# modificacion de valores de la lista
# ["Julio", "Micaela", "Santiago", "Gino", "Valeria"]
nombres[0] = 'Luis' # tener en cuenta que no se vuelve a ordenar la lista si esta ya estaba ordenada
print(nombres)

# verificar si un elemento pertenece a la lista
print('Micaela' in nombres)

# eliminar elementos
nombres.pop()       # ultimo item - valeria
nombres.pop(0)      # Luis
nombres.remove('Gino')
print(nombres) # ['Micaela', 'Santiago']

# insertar elementos en un lugar especifico
nombres.insert(1, 'Valentina')
print(nombres) # ['Micaela', 'Valentina', 'Santiago']

# agregar una lista a otra
nombres.extend(['Micaela', 'Emilio'])
print(nombres) # ['Micaela', 'Valentina', 'Santiago', 'Micaela', 'Emilio']

# contar la cantidad de ocurrencias de un elemento
print(nombres.count('Micaela'))   # 2

# reverso de una lista
nombres.reverse()
print(nombres) # ['Emilio', 'Micaela', 'Santiago', 'Valentina', 'Micaela']

# Ordenar nombres alfabeticamente
nombres.sort() # ascending
print(nombres) # ['Emilio', 'Micaela', 'Micaela', 'Santiago', 'Valentina']

nombres.sort(reverse=True)    # orden descendiente
print(nombres) # ['Valentina', 'Santiago', 'Micaela', 'Micaela', 'Emilio']