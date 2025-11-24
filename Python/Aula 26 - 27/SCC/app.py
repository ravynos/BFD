from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
import sqlite3

app = Flask(__name__)
app.secret_key = '1234'

# Rota para processar o formulário de cadastro
@app.route('/cadastro_clientes', methods=['GET', 'POST'] )
def cadastrar():
    if request.method == 'POST':

        nome = request.form['nome']
        idade = request.form['idade']

        conn = sqlite3.connect("cadastro.db")
        c = conn.cursor()

        c.execute(
        "INSERT INTO clientes (nome, idade) VALUES (?, ?)", (nome, idade)
        )

        conn.commit()
        
        #Verifica se o usuário foi inserido corretamente no banco.
        c.execute("SELECT * FROM clientes WHERE nome = ? AND idade = ?" , (nome, idade))
        usuario_cadastrado = c.fetchone()
        conn.close()

        #Exibe mensagem de sucesso ou erro dependendo do retorno
        if usuario_cadastrado:
            flash('Usuario cadatrado com sucesso', 'sucess')
        else:
            flash('Erro ao cadatrar o usuário.', 'error')

        #Redireciona para a pagina de cadastro novamente
        return redirect(url_for('cadastrar'))
    
    return render_template('cadastro_clientes.html')

@app.route('/clientes')
def listar():
    #Conectar ao banco de dados
    conn = sqlite3.connect('cadastro.db')
    c = conn.cursor()

    #Consultar todos os usuários
    c.execute("SELECT * FROM clientes")
    dados = c.fetchall()

    conn.close()

    return render_template('clientes.html', clientes=dados)

