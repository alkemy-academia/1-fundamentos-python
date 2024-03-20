from abc import ABC, abstractmethod


class CuentaBancaria(ABC):
    def __init__(self, saldo):
        self.saldo = saldo

    @abstractmethod
    def extraer(self, monto):
        pass

    def depositar(self, monto):
        self.saldo += monto

    def consultar_saldo(self):
        return f'Saldo actual: {self.saldo}'


class CajaAhorro(CuentaBancaria):
    def __init__(self, saldo):
        super().__init__(saldo)

    def extraer(self, monto):
        if monto > self.saldo:
            return f'Fondos insuficientes'
        else:
            self.saldo -= monto
            return f'Se realizó la extraccion - Saldo actual: {self.saldo}'


class CuentaCorriente(CuentaBancaria):
    def __init__(self, saldo, limite_descubierto=10000):
        super().__init__(saldo)
        self.limite_descubierto = limite_descubierto

    def extraer(self, monto):
        if monto > self.saldo + self.limite_descubierto:
            return f'Fondos insuficientes, se superó el limite al descubierto'
        else:
            self.saldo -= monto
            return f'Se realizó la extraccion - Saldo actual: {self.saldo}'

    def consultar_saldo(self):
        saldo = super().consultar_saldo()
        return f'{saldo} - Limite al descubierto: {self.limite_descubierto}'


caja_ahorro = CajaAhorro(1000)
caja_ahorro.depositar(500)
print(caja_ahorro.extraer(20000))
print(f'Saldo Caja Ahorro: {caja_ahorro.consultar_saldo()}')


cta_corriente = CuentaCorriente(1000)
cta_corriente.depositar(1000)
print(cta_corriente.extraer(5000))
print(f'Saldo Cuenta Corriente: {cta_corriente.consultar_saldo()}')