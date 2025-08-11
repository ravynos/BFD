n1 = float(input("Qual a primeira nota do aluno? "))
n2 = float(input("Qual a segunda nota do aluno? "))
media = (n1 + n2) / 2

print(f"O aluno teve sua primeira nota {n1}, sua segunda nota {n2}, e sua media é {media}.")

if media >= 7:
    print("O Aluno está aprovado.")
elif media >= 5:
    print("Sua nota precisa de atenção.")
else:
    print("Voce está reprovado.")