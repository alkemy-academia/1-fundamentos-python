class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.__area = None

    def calcular_area(self):
        self.__area = self.base * self.altura
        return self.__area

    def get_area(self):
        return self.__area


class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.__area = None

    def calcular_area(self):
        self.__area = 3.14 * self.radio ** 2
        return self.__area

    def get_area(self):
        return self.__area


def obtener_area(figura):
    if hasattr(figura, 'calcular_area'):
        return figura.calcular_area()

    return 0


rectangulo = Rectangulo(4, 6)
circulo = Circulo(10)

print(f'Area del rectagulo: {obtener_area(rectangulo)}')
print(f'Area del circulo: {obtener_area(circulo)}')

# forma de acceder a un atributo privado:
print(f'area del rectangulo: {rectangulo._Rectangulo__area}')
