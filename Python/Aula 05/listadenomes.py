nomes = []

for i in range(3):
    nome = input('Digite um nome: ')
    nomes.append(nome)

print(50*"-")

for nome in enumerate(nomes):
    print(nome)