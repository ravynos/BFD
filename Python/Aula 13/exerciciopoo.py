class Jogador:
    def __init__(self, nome, profissão, dano, iniciativa):
        self.nome = nome
        self.profissão = profissão
        self.dano = dano
        self.iniciativa = iniciativa

    def mover(self):
        print("Andar")
        print(f"{self.nome} se moveu.")

    def atacar(self):
        print(f"{self.nome}atacou!")

    def defender(self):
        print(f"{self.nome} se defendeu de um ataque")

    def receber_dano(self):
        print(f"{self.nome} recebeu dano")


class Guerreiro(Jogador):
    def atk_espada(self):
        print(f"{self.nome} realizou um ataque com sua espada, desferindo {self.dano} em seu inimigo.\n")
    
    def defender_escudo(self):
        print(f"{self.nome} defendeu com seu escudo")

class Mago(Jogador):
    def __init__(self, nome, profissão, dano, iniciativa, efeito):
        super().__init__(nome, profissão, dano, iniciativa)
        self.efeito = efeito

    def atk_magico(self):
        print(f"{self.nome} realizou um ataque magico, e causou efeito de {self.efeito} ")


j1 = Guerreiro("Arnald", "Guerreiro", 10, 5)
print("=== STATUS === \n")
print(f"Nome: {j1.nome}\nProfissão: {j1.profissão}\nDano:{j1.dano}\nIniciativa:{j1.iniciativa}\n")

j1.atk_espada()

j2 = Mago("Gandalf", "Mago", 20, 2, "Lentidão")
print(f"Nome: {j2.nome}\nProfissão: {j2.profissão}\nDano:{j2.dano}\nIniciativa:{j2.iniciativa}\n")

j2.atk_magico()