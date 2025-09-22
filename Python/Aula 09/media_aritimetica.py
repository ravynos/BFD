from funcoes_gerais import media_numeros
from funcoes_gerais import cabecalho

relatorio = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar...): ")
    if nome.lower() == 'sair':
        break
    
    notas = []

    for i in range(1, 4):
        nota = float(input(f'Digita a nota {i} de {nome}: '))
        notas.append(nota)
    
    m = media_numeros(notas)
    situacao = "Aprovado" if m >= 7 else "Reprovado"

    #relatorio = []

    relatorio.append([nome, notas[0], notas[1], notas[2], round(m,2), situacao])

cabecalho()
for aluno in relatorio:
    print(f"{aluno[0]:<15}{aluno[1]:<6}{aluno[2]:<6}{aluno[3]:<6}{aluno[4]:<8}{aluno[5]}")