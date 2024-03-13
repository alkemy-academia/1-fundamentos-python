"""
Escribir una función que devuelva un diccionario donde la clave sea el nombre de un lenguaje y el valor, la cantidad de
veces que se ha encontrado ese lenguaje en una lista proporcionada.

Lista de entrada de datos de Ejemplo:
data = [
    {"name": "Virgin Islands (British)", "languages": ["English"]},
    {"name": "Cameroon", "languages": ["English", "French"]},
    {"name": "Argentina", "languages": ["Spanish", "Guaraní"]},
    {"name": "Spain", "languages": ["Spanish"]},
    {"name": "United States of America", "languages": ["English"]}
]

"""


def top_lenguajes(data):
    lenguajes = []

    # Recopilar todos los lenguajes de todos los países en la lista
    for pais in data:
        lenguajes.extend(pais["languages"])

    # Contar la frecuencia de cada lenguaje
    cantidad_lenguajes = {}
    for lenguaje in lenguajes:
        """
         Aqui se actualiza el diccionario 'cantidad_lenguajes'. 
         Si lenguaje no está presente en el diccionario, se agrega con un valor inicial de 0 
         (usando get()). 
         Luego, se incrementa en 1 el valor asociado a la clave lenguaje usando + 1. 
         Esto significa que cada vez que se encuentre un nuevo lenguaje o se mencione uno 
         ya existente, se aumentará en 1 la cantidad de veces que ha sido mencionado en el 
         diccionario 'cantidad_lenguajes'.
        """
        cantidad_lenguajes[lenguaje] = cantidad_lenguajes.get(lenguaje, 0) + 1

    """
    Aqui se aplica la funcion 'sorted' a la cual se envia la lista de items del diccionario (items()),
    y ademas se indica mediante el atributo 'key' una funcion lambda que indica que en cada 
    iteracion se compare el elemento que representa a la cantidad de lenguajes 
    (elemento con indice 1 en la tupla de cada iteracion).
    En cada iteracion que realice la funcion 'sorted' el elemnto sera por ejemplo:
    ('English', 3)
    """
    lenguajes_ordenados = dict(sorted(cantidad_lenguajes.items(), key=lambda lenguaje: lenguaje[1], reverse=True))

    return lenguajes_ordenados


# Lista de datos proporcionada
datos = [
    {"name": "Virgin Islands (British)", "languages": ["English"]},
    {"name": "Cameroon", "languages": ["English", "French"]},
    {"name": "Argentina", "languages": ["Spanish", "Guaraní"]},
    {"name": "Spain", "languages": ["Spanish"]},
    {"name": "United States of America", "languages": ["English"]}
]

# Obtener los 10 lenguajes más hablados
result_lenguajes = top_lenguajes(datos)

print("Los lenguajes más hablados:", result_lenguajes)
