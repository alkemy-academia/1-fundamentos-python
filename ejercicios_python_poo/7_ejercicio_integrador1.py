import datetime
from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, dni, nombre, apellido, anio_ingreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso

    @abstractmethod
    def obtener_salario(self):
        pass

    def mostrar_salario(self):
        return print(f"{self.nombre} {self.apellido} es un {self.__class__.__name__} y tiene un salario de {self.obtener_salario()}")

    def obtener_antiguedad(self):
        anio_actual = datetime.datetime.now().year
        return anio_actual - self.anio_ingreso


class EmpleadoSalarioFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, sueldo_basico):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.sueldo_basico = sueldo_basico

    def obtener_adicional_antiguedad(self):
        antiguedad = self.obtener_antiguedad()
        if antiguedad < 2:
            return 0

        if 2 <= antiguedad <= 5:
            return self.sueldo_basico * 0.05

        if antiguedad > 5:
            return self.sueldo_basico * 0.10

    def obtener_salario(self):
        return self.sueldo_basico + self.obtener_adicional_antiguedad()


class EmpleadoPorComision(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, salario_minimo, clientes_captados, monto_por_cliente):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def obtener_salario(self):
        salario_por_clientes = self.monto_por_cliente * self.clientes_captados
        if salario_por_clientes <= self.salario_minimo:
            return self.salario_minimo

        return salario_por_clientes

    @classmethod
    def empleado_con_mas_clientes(cls, lista_empleados):
        empleado_max_cliente = None
        clientes_max = -1
        for emp in lista_empleados:
            if isinstance(emp, cls):
                if emp.clientes_captados > clientes_max:
                    clientes_max = emp.clientes_captados
                    empleado_max_cliente = emp

        # empleados_por_comision = [e for e in lista_empleados if isinstance(e, cls)]
        # empleado_max_cliente = max(empleados_por_comision, key=lambda em: em.clientes_captados)

        return empleado_max_cliente


empleado_fijo1 = EmpleadoSalarioFijo('24522326', 'Laura', 'Gomez', 2000, 150000)
empleado_fijo2 = EmpleadoSalarioFijo('24522327', 'Salvador', 'Perez', 2024, 200000)

empleado_comision1 = EmpleadoPorComision('24522329', 'Roberto', 'Castillo', 1998, 200000, 15, 60000)
empleado_comision2 = EmpleadoPorComision('24522328', 'Carolina', 'Juarez', 1990, 700000, 70, 5000)
empleado_comision3 = EmpleadoPorComision('24522399', 'Esteban', 'Ramirez', 1980, 150000, 50, 70000)

empleados = [empleado_fijo1, empleado_fijo2, empleado_comision1, empleado_comision2, empleado_comision3]

for e in empleados:
    e.mostrar_salario()

empleado_mas_clientes = EmpleadoPorComision.empleado_con_mas_clientes(empleados)
print(f'El empleado con mas clientes captados es: {empleado_mas_clientes.nombre} {empleado_mas_clientes.apellido} con '
      f'{empleado_mas_clientes.clientes_captados} clientes captados')
