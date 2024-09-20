class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depositado: {cantidad}, Nuevo saldo: {self.__saldo}"
        return "Cantidad no válida"

    def obtener_saldo(self):
        return f"Saldo actual: {self.__saldo}"

cuenta = CuentaBancaria(1000)
print(cuenta.depositar(500))  # Imprime: Depositado: 500, Nuevo saldo: 1500
print(cuenta.obtener_saldo())  # Imprime: Saldo actual: 1500
