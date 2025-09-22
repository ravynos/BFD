class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = float(preco)
        self.__estoque = int(estoque)

    def __str__(self):
        return f"Produto: {self.nome:.2f}, Preço: R$ {self.__preco}, Estoque: {self.__estoque}"

    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    def get_estoque(self):
        return self.__estoque
    
    def aplicar_desconto(self, percentual):
        if 0 <= percentual <= 100:
            desconto = self.__preco * (percentual / 100)
            self.__preco -= desconto
            print(f"Desconto de {percentual}% aplicado. Novo preço: {self.__preco:.2f}")
        else:
            print