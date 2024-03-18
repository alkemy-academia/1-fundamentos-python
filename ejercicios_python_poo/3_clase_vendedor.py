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
    def __init__(self, nombre, antiguedad, sueldo_basico, categoria, cantidad_autos_vendidos=0):
        self.nombre = nombre
        self.antiguedad = antiguedad
        self.sueldo_basico = sueldo_basico
        self.categoria = categoria
        self.cantidad_autos_vendidos = cantidad_autos_vendidos

    def incrementar_autos_vendidos(self, cantidad):
        self.cantidad_autos_vendidos += cantidad

    def calcular_sueldo_total(self):
        pass
