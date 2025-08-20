#Vamos criar uma agenda simples usando dicionarios!

#Criar agenda com 3 contatos (Nome, telefone)
#Exibir todos os contatos com for.

agenda = {"João" : "(11) 99999-1111", "Maria" : "(11) 99999-2222", "Pedro" : "(11) 99999-3333" }

for chave, valor in agenda.items():
    print(f"{chave}: {valor}")