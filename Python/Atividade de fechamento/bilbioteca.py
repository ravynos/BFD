biblioteca = []
print("Bem vindo a biblioteca do Thiago")
while True:
    print("\n--- MENU ---\n")
    print("1 - Cadastrar Livros")
    print("2 - Listar Livros")
    print("3 - Buscar")
    print("4 - Categorias")
    print("5 - Livros por Categoria")
    print("6 - Encerrar programa.")
    menu = int(input("\nSelecione uma opção: "))
    if menu == 1:
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        while True:
            ano = input("Ano: ")
            if ano.isdigit() and len(ano) == 4:
                break
            print("Erro: Insira um ano valido com 4 digitos (apenas números).")
            


    break