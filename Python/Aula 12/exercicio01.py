class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def __str__(self):
        return f"o Salario do Funcionario {self.nome} é R$ {self.__salario} por mês"

    def get_salario(self):
        return self.__salario

    def set_salario(self, valor):
        if valor >=0:
            self.__salario = valor
        else:
            print("Salario não pode ser negativo.")

f1 = Funcionario("Ayra Sobrinho", 3000)
print(f1)

f1.set_salario(5000)
print(f1)

f1.set_salario(-100)
print(f1)