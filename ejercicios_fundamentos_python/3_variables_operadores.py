a = 28
b = 1.5
c = 'Hola'
d = True
e = None
rango_10 = range(10)

print(rango_10)
print(type(d))

# desempaqueta de strings
h, i, j, k, l, m = "python"
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)

# formas de imprimir un string con variables
print('Contenido de la variable c y a: ' + c + ' - ' + str(a))
print(f'Contenido de la variable c: {c}')

# Modulo de un numero
print(f'modulo de a: {a % 2}')

# Operadores lógicos y de comparacion
print(f'Es la variable a menor a 30? {a<30}')
print(3 > 2 and 4 < 2)
print(not 3 < 2)

# conversion de tipos
z = str(a)

print(type(int(z)))

# operador is
print(f'la variable e es None? {e is not None}')

