from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
import sqlite3

app = Flask(__name__)
app.secret_key = '1234'

# Rota para a página inicial ('/')
@app.route('/')
def index():
    # Renderiza o template 'index.html' e passa o título da página
    return render_template('index.html', titulo='Página Inicial')

# Rota para processar o formulário de cadastro
@app.route('/cadastro_clientes', methods=['GET', 'POST'] )
def cadastrar():
    if request.method == 'POST':

        #nome = request.form['nome']
        #idade = request.form['idade']

        nome = request.form.get('nome', '').strip()
        idade = request.form.get('idade', '').strip()

        # ----Bloco de Validação----

        # Validação 1: Nome vazio
        if not nome:
            flash('O campo nome é obrigatório.', 'error')
            return redirect(url_for('cadastrar'))
        
        if len(nome) < 3:
            flash('O Nome deve ser pelo menos 3 letras.', 'error')
            return redirect(url_for('cadastrar'))
        
        #Passo para gravar no banco
        try:
            conn = sqlite3.connect("cadastro.db")
            c = conn.cursor()

            c.execute(
            "INSERT INTO clientes (nome, idade) VALUES (?, ?)", (nome, idade))
            conn.commit()

            flash(f'Usuário {nome} cadastrado com sucesso', 'success')
        
        except sqlite3.Error as e:
            #Captura erros do próprio banco de dados
            flash(f'Erro no banco de dados: {e}', 'error')

        finally:
            #Finaliza a conexão, mesmo se der erro
            if conn:
                conn.close()

        return redirect(url_for('cadastrar'))
     
    return render_template('cadastro_clientes.html')

@app.route('/clientes')
def listar():
    #Conectar ao banco de dados
    conn = sqlite3.connect('cadastro.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    #Consultar todos os usuários
    c.execute("SELECT * FROM clientes")
    dados = c.fetchall()

    conn.close()

    return render_template('clientes.html', clientes=dados)

@app.route('/editar_cliente/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = sqlite3.connect('cadastro.db')
    #Essa função permite acessar as colunas pelo nome.
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # Metodo GET, para buscar o cliente na tabela.
    if request.method == 'GET':
        #Busca o cliente pelo ID
        c.execute("SELECT * FROM clientes WHERE id=?", [id])
        cliente_encontrado = c.fetchone()
        conn.close()

        #Faz a validação, caso o id não seja encontrado.
        if cliente_encontrado is None:
            flash('Cliente não encontrado!', 'error')
            return redirect(url_for('listar'))
        
        return render_template("editar_cliente.html", cliente=cliente_encontrado)
    
    # Metodo POST para salvar a edição
    elif request.method == 'POST':
        nome = request.form.get('nome', '').strip() # .strip e usado para remover espaços em branco no inicio e no final do campo
        idade = request.form.get('idade', '').strip()

        if not nome or not idade.isdigit():
            flash('Dados inválidos. Verifique os campos .', 'error')
            conn.close()
            return redirect(url_for('editar', id=id))
        
        try:
            c.execute("UPDATE clientes SET nome = ?, idade = ? WHERE id=?", (nome, int(idade), id))
            conn.commit()
            flash('Dados atualizados com sucesso!', 'success')

            conn.close()
            return redirect(url_for('listar'))

        except sqlite3.Error as e:
            flash(f'Erro ao atualizar: {e}', 'error')
            conn.close()
            return redirect(url_for('editar', id=id))      

@app.route('/remover_cliente/<int:id>', methods=['GET', 'POST'])
def remover(id):
    conn = sqlite3.connect('cadastro.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    if request.method == 'GET':
        c.execute("SELECT * FROM clientes WHERE id=?", [id])
        cliente_encontrado = c.fetchone()
        conn.close()

        if cliente_encontrado is None:
            flash('Cliente não encontrado!', 'error')
            return redirect(url_for('listar'))
        
        return render_template("remover_cliente.html", cliente=cliente_encontrado)
    
    elif request.method == 'POST':
        try:
            c.execute("DELETE FROM clientes WHERE id=?", [id])
            conn.commit()
            flash('Cliente removido com sucesso!', 'success')

            conn.close()
            return redirect(url_for('listar'))
        
        except sqlite3.Error as e:
            flash(f'Erro ao atualizar: {e}', 'error')
            conn.close()
            return redirect(url_for('editar', id=id))


if __name__ == '__main __':
    # app.run(debug=True) inicia o servidor.
    # debug=True é útil durante o desenvolvimento, pois reinicia o servidor
    # automaticamente a cada mudança no código e mostra erros detalhados no navegador.

    app.run(debug=True)