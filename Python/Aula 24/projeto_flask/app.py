# Passo 1: Importar as classes necessárias do Flask.
# Flask: A Classe principal para criar nossa aplicação.
# render_template: Para renderizar (mostar) nossos arquivos HTML.
# request: Para acesssar os dados enviados pelo formulário (como o nome do usuário)

from Flask import Flask, render_template, request

# Passo 2: Criar uma instãncia da aplicação Flask
# A variável '__name__' ajuda o Flask a saber onde procurar por arquivos como os templates

app = Flask(__name__)

# Passo 3: Definir a rota para o formulário de cadastro
# @app.route('/cadastro', methods=['GET', 'POST']) cria uma URL para nossa aplicação.
# Ex: http://127.0.0.1:5000/cadastro
# methods=['GET', 'POST'] permite que esta rota aceite tanto requisições GET quanto POST.
# GET: Quando o usuário acessa a página pela primeira vez para ver o formulário.
# POST: Quando o usuário preenche e envia o formulário.

@app.route('/cadastro', methods=['GET', 'POST'] )
def cadatro():
    # Passo 4: Verificar o método da requisição
    # Se o método for 'POST', significa que o usuário enviou o formulário.
    if request.method ==  'POST':
    # Passo 4.1: Obter o dado do formulário
    # request.form é um dicionário que contém todos os dados enviados.
    # 'nome' corresponde ao atributo 'name' do campo <input> no HTML.
        nome_usuario = request.form['nome']
    # Passo 4.2: Renderizar a página de resultado
    # Enviamos o nome obtido para o template 'resultado.html'.
    # A variável 'nome' no template receberá o valor de 'nome_usuario'.

        return render_template('resultado.html', nome=nome_usuario)
    
    # Passo 5: Se o método for 'GET' (ou qualquer outro que não seja 'POST')
    # Apenas exibe o formulário de cadastro para o usuário preencher.

        return render_template('cadastro.html')
    
    # Passo 6: Linha necessária para rodar a aplicação quando o script é executado diretamente.

    if __name__ == '__main __':
    # app.run(debug=True) inicia o servidor.
    # debug=True é útil durante o desenvolvimento, pois reinicia o servidor
    # automaticamente a cada mudança no código e mostra erros detalhados no navegador.

        app.run(debug=True)

    