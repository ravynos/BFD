biblioteca = []
while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Mostrar categorias únicas")
    print("5 - Contar livros por categoria")
    print("6 - Sair")
    opcao = input("Escolha: ")
    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        while True:
            ano = input("Ano: ")
            if ano.isdigit():
                break
            print("Erro: Insira um ano válido (apenas números).")
        categoria = input("Categoria: ")
        biblioteca.append({"titulo": titulo, "autor": autor, "ano": ano, "categoria": categoria})
    elif opcao == "2":
        if not biblioteca:
            print("Nenhum livro cadastrado.")
        for l in biblioteca:
            print(f"{l['titulo']} - {l['autor']} ({l['ano']}) - {l['categoria']}")
    elif opcao == "3":
        busca = input("Título do livro: ").lower()
        encontrados = [l for l in biblioteca if busca in l['titulo'].lower()]
        if encontrados:
            for livro in encontrados:
                print(f"Encontrado: {livro['titulo']} - {livro['autor']}")
        else:
            print("Nenhum livro encontrado.")
    elif opcao == "4":
        categorias = {l["categoria"] for l in biblioteca}
        print("Categorias:", categorias if categorias else "Nenhuma categoria cadastrada.")
    elif opcao == "5":
        contagem = {}
        for l in biblioteca:
            contagem[l["categoria"]] = contagem.get(l["categoria"], 0) + 1
        print("Quantidade por categoria:", contagem if contagem else "Nenhum livro cadastrado.")
    elif opcao == "6":
        break
    else:
        print("Opção inválida!")