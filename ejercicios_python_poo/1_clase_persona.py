class Persona:
    def __init__(self, un_nombre, una_edad):
        self.nombre = un_nombre
        self.edad = una_edad

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años')

    def es_mayor_edad(self):
        #if self.edad >= 18:
        #    return True
        #else:
        #    return False

        return True if self.edad >= 18 else False

persona1 = Persona("Santi", 8)
persona1.saludar()
print(f'Es {persona1.nombre} mayor de edad?: {persona1.es_mayor_edad()}')

persona2 = Persona("Laura", 19)
persona2.saludar()
print(f'Es {persona2.nombre} mayor de edad?: {persona2.es_mayor_edad()}')
