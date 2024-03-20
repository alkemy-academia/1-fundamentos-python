"""Desarrollar un programa en Python que contabilice las ventas realizadas por un vendedor y en base a eso calcule su sueldo.
Crear la clase "Vendedor" con los siguientes atributos: nombre, antigüedad (en años), sueldo_básico, categoria (principiante, nivel_medio, experto).
La clase Vendedor también debe contar con un atributo que represente la cantidad de autos vendidos en el mes, pero que inicialmente debe ser igual a cero.
Crear un método para la clase Vendedor, que permita incrementar la cantidad de autos vendidos dado un valor especifico.
Crear otro método que calcule y retorne el sueldo total del vendedor teniendo en cuenta que al sueldo_básico del vendedor se le agrega lo siguiente:
5 % del sueldo básico por cada año de antigüedad.
Por cada auto vendido, se abona una comisión de acuerdo a la categoría del vendedor: $10.000 si es “principiante”, $13000 si es “nivel_medio” o $17.000 si el vendedor tiene categoría “experto”
Probar el funcionamiento de la clase creando distintas instancias y convocando sus métodos.
"""

class Vendedor:
    # atributo de clase
    comision_venta = {
        'principiante': 10000,
        'nivel_medio': 13000,
        'experto': 17000
    }

    def __init__(self, nombre, antiguedad, sueldo_basico, categoria, cantidad_autos_vendidos=0):
        # atributos de instancia
        self.nombre = nombre
        self.antiguedad = antiguedad
        self.sueldo_basico = sueldo_basico
        self.categoria = categoria
        self.cantidad_autos_vendidos = cantidad_autos_vendidos

    def incrementar_autos_vendidos(self, cantidad):
        self.cantidad_autos_vendidos += cantidad

    def calcular_sueldo_total(self):
        monto_antiguedad = self.sueldo_basico * 0.05 * self.antiguedad
        # monto_comision = 0
        # if self.categoria == 'principiante':
        #     monto_comision = 10000 * self.cantidad_autos_vendidos
        # elif self.categoria == 'nivel_medio':
        #     monto_comision = 13000 * self.cantidad_autos_vendidos
        # elif self.categoria == 'experto':
        #     monto_comision = 17000 * self.cantidad_autos_vendidos

        # recupero el elemento del diccionario enviado como clave el valor de la categori, por ejemplo: 'expertp'.
        # De esta manera obtengo el valor de la comision de acuerdo a la categoria correspondiente
        monto_comision = self.comision_venta[self.categoria] * self.cantidad_autos_vendidos
        return self.sueldo_basico + monto_antiguedad + monto_comision

    def imprimir_informacion(self):
        print(f'El vendedor {self.nombre} tiene una antiguedad de {self.antiguedad} años, categoria {self.categoria} y '
              f'un sueldo total de: {self.calcular_sueldo_total()}')


# crear una instancia de vendedor
vendedor1 = Vendedor('Luis Perez', 5, 150000, 'principiante')
vendedor1.incrementar_autos_vendidos(10)
vendedor1.incrementar_autos_vendidos(5)
vendedor1.imprimir_informacion()

print(f'antiguedad: {vendedor1.antiguedad}')

# Puedo acceder al atributo de clase "comision_venta" ya sea desde una instancia o desde la clase misma
print(f'comision: {vendedor1.comision_venta}')
print(f'comision desde afuera: {Vendedor.comision_venta}')
