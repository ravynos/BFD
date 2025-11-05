# Importa a classe Flask e as funções render_template e url_for
from flask import Flask, render_template, url_for

# Cria a aplicação Flask
app = Flask(__name__)

# Rota para a página inicial ('/')
@app.route('/')
def index():
    # Renderiza o template 'index.html' e passa o título da página
    return render_template('index.html', titulo='Página Inicial')

# Rota para a página de produtos ('/produtos')

@app.route('/produtos')
def produtos():
    # Exemplo de uma lista de produtos (variável) que será passada para o template
    lista_de_produtos = [
        {'nome': 'Notebook Gamer', 'preco': 'R$ 5.000,00'},
        {'nome': 'Mouse sem fio', 'preco': 'R$ 150,00'},
        {'nome': 'Teclado Mecânico', 'preco': 'R$ 350,00'},
        {'nome': 'Monitor 4K', 'preco': 'R$ 2.000,00'}
    ]

# Renderiza o template 'produtos.html', passando o título e a lista de produtos
    return render_template('produtos.html', titulo='Nossos Produtos', produtos = lista_de_produtos)

# Rota para a página de contato ('/contato')
@app.route('/contatos')
def contatos():
    # Renderiza o template 'contato.html' e passa o título
    return render_template('contatos.html', titulo='Contatos')

# Executa a aplicação em modo de depuração

if __name__ == '__main__':
    app.run(debug=True)