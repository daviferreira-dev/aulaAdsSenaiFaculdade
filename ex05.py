class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")
        else:
            print("Valor invalido para depósito.")
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Valor invalido para saque.")
    def mostrar_saldo(self):
        status = "Devendo ao banco." if self.saldo < 0 else "Em dia"
        print(f"Saldo atual: R${self.saldo} - Status: {status}")
    def mostrar_titular(self):
        return self.titular

class Banco:
    def __init__(self):
        self.correntistas = []
    def abrir_conta(self):
        nome = input("Digite o nome do titular: ")
        conta = ContaBancaria(nome)
        self.correntistas.append(conta)
        print("Conta aberta com sucesso!!!")
    def encontrar_conta(self, nome):
        for conta in self.correntistas:
            if conta.mostrar_titular() == nome:
                return conta
        return None
    def depositar_fundos(self):
        nome = input("Digite o nome do titular: ")
        conta = self.encontrar_conta(nome)
        if conta:
            try:
                valor = float(input("Digite o valor a ser depositado: "))
                conta.depositar(valor)
            except ValueError:
                print("Valor inválido para depósito.")
        else:
            print("Correntista não encontrada.")
    def sacar_fundos(self):
        nome = input("Digite o nome do titular: ")
        conta = self.encontrar_conta(nome)
        if conta:
            try:
                valor = float(input("Digite o valor a ser sacado: "))
                conta.sacar(valor)
            except ValueError:
                print("Valor inválido para saque.")
        else:
            print("Correntista não encontrada.")
    def mostrar_saldo_correntista(self):
        nome = input("Digite o nome do titular: ")
        conta = self.encontrar_conta(nome)
        if conta:
            conta.mostrar_saldo()
        else:
            print("Correntista não encontrada.")
    def listar_contas(self):
        if not self.correntistas:
            print("Nenhuma conta cadastrada.")
            return
        print("Lista de Correntistas ")
        for conta in self.correntistas:
            print(f"Titular: {conta.mostrar_titular()} - Saldo: R${conta.saldo}")

def main():
    banco = Banco()
    while True:
        print("\n --- Menu Bancário---")
        print("1. Abrir Conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Mostrar Saldo")
        print("5. Listar Correntistas")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            banco.abrir_conta()
        elif escolha == '2':
            banco.depositar_fundos()
        elif escolha == '3':
            banco.sacar_fundos()
        elif escolha == '4':
            banco.mostrar_saldo_correntista()
        elif escolha == '5':
            banco.listar_contas()
        elif escolha == '6':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
main()