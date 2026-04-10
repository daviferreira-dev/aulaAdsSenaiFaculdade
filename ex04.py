class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        if valor <= 0:
            return "Valor de depósito deve ser positivo."
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}"
    def sacar(self, valor):
        if valor <= 0:
            return "Valor de saque deve ser positivo."
        elif valor > self.saldo:
            return "Saldo insuficiente para saque."
        else:
            self.saldo -= valor
            return f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}"
    def consultar_saldo(self):
        return f"Saldo atual: R${self.saldo}"
    def mostrar_titular(self):
        return f"Titular da conta: {self.titular}"
conta1 = ContaBancaria("João", 1000)
print(conta1.depositar(500))
print(conta1.sacar(200))
print(conta1.consultar_saldo())
print(conta1.mostrar_titular())
