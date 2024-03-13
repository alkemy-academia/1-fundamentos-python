# Otras formas de crear un diccionario
dict1 = {}
dict2 = dict()


persona = {
    'nombre': 'Ana',
    'apellido': 'Lopez',
    'edad': 25,
    'skills': ['JavaScript', 'React', 'Node', 'Python'],
    'direccion': {
        'calle': 'Maipu',
        'codigo_postal': '4700'
    }
}

print(len(persona)) # 6

# acceso a elementos
print(persona['nombre'])
print(persona['skills'])
print(persona['skills'][1])
# print(persona['dni']) dará error

# para evitar errores al acceder a atributos se puede usar el metodo GET
print(persona.get('apellido'))
print(persona.get('dni', 'Ningun DNI'))

# agregar elementos
persona['trabajo'] = 'Instructor'
persona['skills'].append('HTML')
print(persona)

# verificar si existe elemento por su clave
print('trabajo' in persona)

# eliminacion de elementos
persona.pop('apellido')        # Elimina el item con clave "apellido"
persona.popitem()              # Elimina el ultimo item
del persona['edad']            # Elimina el item con clave "edad"
print(persona)

# obtener lista de claves y valores
print(persona.keys())
print(persona.values())

# cambiando dic a lista de tuplas
lista = persona.items()
print(lista)