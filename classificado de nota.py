nota = int(input("Qual a nota do aluno? "))

if nota >= 9:
    print("Ótimo")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
else:
    print("Insuficiente")