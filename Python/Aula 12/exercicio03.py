class Cliente:
    def __init__(self, nome, email, cpf, saldo_inicial=0):
        self.nome = nome
        self.email = email
        self.__cpf = cpf
        self.__saldo = saldo_inicial

    def get_cpf(self):
        return self.__cpf
    
    def get_saldo(self):
        return self.__saldo
    
    def adicionar_saldo(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False
    
    def exibir_dados(self):
        return f"Cliente: {self.nome}, Email: {self.email}"
    
c1 = Cliente("Ayra Sobrinho", "ayra@sobrinho.com.br", "123.456.789.01", 1000)

print(c1.nome)
print(c1.email)
print(c1.get_cpf())
print(c1.get_saldo())

c1.adicionar_saldo(500)
print(c1.get_saldo())