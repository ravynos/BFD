#Criar um dicionario com dados de um livro.
#Imprimir informações formatadas.

#Dados
#Python para Iniciantes
#Titulo: Python para iniciantes
#Autor: Ana Silva
#Ano 2023

livro = {"Titulo": "Python para iniciantes", "Autor" : "Ana Silva", "Ano" : "2023"}

print(f"Titulo: {livro['Titulo']}")
print(f"Autor: {livro['Autor']}")
print(f"Ano: {livro['Ano']}")

print("\n Informações do livro.")
for chave, valor in livro.items():
    print(f"{chave}: {valor}")