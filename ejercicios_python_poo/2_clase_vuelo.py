"""
Desarrollar un programa en Python que simule la gestión de pasajeros en un vuelo.
Crear una clase llamada Vuelo que tenga la funcionalidad de agregar pasajeros y verificar la disponibilidad de asientos.
Cuando se cree un objeto de tipo Vuelo, se debe indicar la capacidad de asientos que tiene el mismo.
Cuando se agregue un pasajero al vuelo, en primer lugar se debe verificar si existe disponibilidad de asientos, y en caso afirmativo, agregar el pasajero a una colección de datos asociada al vuelo y devolver un valor que indique que se pudo realizar la operación. Caso contrario informar que no se pudo realizar la transacción.
Considerar codificar un método que devuelva el número de asientos disponibles en el vuelo.
Para probar el funcionamiento de la clase, crear un objeto vuelo con su capacidad, y dada una lista de pasajeros (por ejemplo: ["Karina", "Mario", "Ruben", "Carla"]), por cada persona en la lista, mostrar un mensaje indicando si se pudo agregar al vuelo o si no había asientos disponibles.

"""


class Vuelo:
    def __init__(self, cantidad_asientos):
        self.capacidad = cantidad_asientos
        self.pasajeros = []

    def agregar_pasajero(self, nombre):
        # if len(self.pasajeros) < self.capacidad:
        if self.cantidad_asientos_disponibles() > 0:
            self.pasajeros.append(nombre)
            return True
        else:
            return False

    def cantidad_asientos_disponibles(self):
        return self.capacidad - len(self.pasajeros)


vuelo = Vuelo(cantidad_asientos=3)

personas = ["Karina", "Mario", "Ruben", "Carla"]
for persona in personas:
    if vuelo.agregar_pasajero(persona):
        print(f'La persona {persona} se pudo agregar correctamente al vuelo')
    else:
        print(f'La persona {persona} NO se pudo agregar al vuelo porque no existen lugares '
              f'disponibles')

print(f'Asientos disponibles del vuelo: {vuelo.cantidad_asientos_disponibles()}')
