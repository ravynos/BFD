import time


print("Bem vindo ao sistema de Gerenciamento de Tarefas")

tarefas = []

while True:
    #Menu de opções.
    print("\n MENU PRINCIPAL")
    print("1 - Adicionar tarefa")
    print("2 - Listar Tarefa")
    print("3 - Marcar Tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Listar Categorias")
    print("6 - Sair")

    #Input do usuário para selecionar qual opção do Menu ele deseja usar.

    opcao = input("Selecione uma opção: ")

    #Opção 1 - Cadastrar tarefa.
    if opcao == "1":
        print("# Adicionar Tarefa\n")
        nome_tarefa = input("Qual o nome da tarefa? ")
        categoria_tarefa = input("Qual a categoria da tarefa? ")

        #Criando um dicionario com as informções da tarefa
        nova_tarefa = {
            "nome_tarefa": nome_tarefa,
            "categoria_tarefa": categoria_tarefa,
            "status": False
        }

        tarefas.append(nova_tarefa)
        print("\nTarefa cadastrada com sucesso.")

        time.sleep(1)

    #Opção 2 - Listar Tarefa
    elif opcao == "2":
        if len(tarefas) == 0:
            print("Não há tarefas cadastrada.")
        else:
            for indice, tarefa in enumerate(tarefas):
                print(f"{indice+1} [{tarefa['nome_tarefa']} ({tarefa['categoria_tarefa']})]")
                
        time.sleep(1)

    #Opção Numero 6 encerrando o programa
    elif opcao == "6":
        break

    else:
        print("/n Opção inválida. Tente novamente")