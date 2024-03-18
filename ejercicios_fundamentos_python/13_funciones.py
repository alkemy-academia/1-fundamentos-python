def cuadrado(x):
    return x * x


for i in range(10):
    print(f'El cuadrado de {i} es {cuadrado(i)}')


def calcular_edad(anio_nacimiento, anio_actual=2024):
    edad = anio_actual - anio_nacimiento
    return edad

x = calcular_edad(1958)
print(f'Edad: {x}')


def sumar_numeros(*numeros):
    print(f'Tipo de variable numeros: {type(numeros)}')
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sumar_numeros(2, 3, 5))
print(sumar_numeros(2, 3, 5, 9, 4, 6))


def mostrar_datos(**data):
    print(f'Tipo de datos de data: {type(data)}')
    for item in data.values():
        print(f'{item}')


mostrar_datos(nombre='Luisa', edad=34, oficio='Instructora')