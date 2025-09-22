class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Deposito de {valor:.2f} realizado com sucesso")
        else:
            print("Erro: O Deposito deve ser maior que 0.") 

    def sacar(self, valor):
        if valor <= 0:
            print(f"Erro: O valor do saque deve ser maior que 0")
        elif valor > self.__saldo:
            print(f"Saldo Insuficiente. Valor disponivel {self.__saldo:.2f}")
        else:
            self.__saldo -= valor
            print(f"Saque de {valor:.2f} realizado com sucesso.")

    def consultar_saldo(self):
        return f"Saldo Atual: {self.__saldo}"


conta = ContaBancaria(1000)
print(conta.consultar_saldo())

conta.depositar(500)
print(conta.consultar_saldo())

conta.sacar(300)
print(conta.consultar_saldo())

conta.sacar(2000)