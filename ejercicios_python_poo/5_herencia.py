class Figura:
    def calcular_area(self):
        pass


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio ** 2


figuras = [Rectangulo(3, 7), Circulo(10)]

for figura in figuras:
    print(f'Area de {figura.__class__.__name__}: {figura.calcular_area()}')
