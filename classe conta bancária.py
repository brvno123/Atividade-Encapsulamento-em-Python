class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Erro: o valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Erro: saldo insuficiente para saque.")
        elif valor <= 0:
            print("Erro: o valor do saque deve ser positivo.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def ver_saldo(self):
        return self.__saldo


conta = ContaBancaria("Ana", 1000)

print(f"Titular: {conta.titular}")
print(f"Saldo inicial: R${conta.ver_saldo():.2f}")

conta.depositar(500)
print(f"Saldo após depósito: R${conta.ver_saldo():.2f}")

conta.sacar(300)
print(f"Saldo após saque: R${conta.ver_saldo():.2f}")

conta.sacar(1500)
print(f"Saldo final: R${conta.ver_saldo():.2f}")