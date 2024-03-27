import datetime
from abc import ABC, abstractmethod


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado_agregar):
        # for e in self.empleados:
        #     if e.dni == empleado_agregar.dni:
        #         print(f'Empleado {e.nombre}, {e.apellido} ya existe en la Empresa, no se puede agregar')
        #         return

        lista_filtrada = list(filter(lambda emp: emp.dni == empleado_agregar.dni, self.empleados))
        if lista_filtrada:
            print(f'Empleado {e.nombre}, {e.apellido} ya existe en la Empresa, no se puede agregar')
            return

        self.empleados.append(empleado_agregar)

    def eliminar_empleado(self, empleado_eliminar):
        for e in self.empleados:
            if e.dni == empleado_eliminar.dni:
                self.empleados.remove(empleado_eliminar)
                return

        print(f'Empleado {empleado_eliminar.nombre}, {empleado_eliminar.apellido} no se registra en la Empresa, '
              f'no se puede Eliminar')

    def mostrar_empleados(self):
        print('Empleados de la empresa:')
        for e in self.empleados:
            e.mostrar_salario()

    # redefinicion del metodo
    def empleado_con_mas_clientes(self):
        empleados_por_comision = [e for e in self.empleados if isinstance(e, EmpleadoPorComision)]
        empleado_con_mas_clientes = max(empleados_por_comision, key=lambda empleado: empleado.clientes_captados)
        return empleado_con_mas_clientes


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


empresa = Empresa('La Tarde')

empleado_fijo1 = EmpleadoSalarioFijo('24522326', 'Laura', 'Gomez', 2000, 150000)
empleado_fijo2 = EmpleadoSalarioFijo('24522327', 'Salvador', 'Perez', 2024, 200000)

empleado_comision1 = EmpleadoPorComision('24522329', 'Roberto', 'Castillo', 1998, 200000, 15, 60000)
empleado_comision2 = EmpleadoPorComision('24522328', 'Carolina', 'Juarez', 1990, 700000, 30, 5000)
empleado_comision3 = EmpleadoPorComision('24522399', 'Esteban', 'Ramirez', 1980, 150000, 50, 70000)

# creo este empleado que tiene el mismo dni que otro, por lo tanto no se deberia agregar
empleado = EmpleadoSalarioFijo('24522326', 'Laura', 'Lorenzeti', 2000, 150000)

empleados = [empleado_fijo1, empleado, empleado_fijo2, empleado_comision1, empleado_comision2, empleado_comision3]

# agrego empleados
for e in empleados:
    empresa.agregar_empleado(e)

print('-----------------------------------')
# mostrar empleados
empresa.mostrar_empleados()

print('-----------------------------------')
# eliminar empleado
empleado2 = EmpleadoSalarioFijo('24522398', 'Pepe', 'Lorenzeti', 2000, 150000)
empresa.eliminar_empleado(empleado2)

print('-----------------------------------')
# eliminar un empleado que si existe
empresa.eliminar_empleado(empleado_fijo1)

print('Empleados despues de eliminar a Laura -----------------------------------')
# mostrar empleados
empresa.mostrar_empleados()

print('-----------------------------------')
empleado_mas_clientes = empresa.empleado_con_mas_clientes()
print(f'El empleado con mas clientes captados es: {empleado_mas_clientes.nombre} {empleado_mas_clientes.apellido} con '
      f'{empleado_mas_clientes.clientes_captados} clientes captados')