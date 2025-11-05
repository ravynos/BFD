nome = input("Qual seu nome? ")
idade = int(input("Qual a sua idade? "))
possui_ingresso = (input("Possui ingresso? "))

if idade >= 18 and possui_ingresso.lower() == "sim":
    print("Acesso permitido!")
else:
    print("Acesso negado!")