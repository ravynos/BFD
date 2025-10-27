from app import app
from flask import render_template
@app.route('/')
@app.route('/index.html')
def index():
    nome="Projeto Simples"
    return render_template('index.html')
def sobre():
    nome="sobre"
    return render_template('sobre.html')
def contatos():
    nome="contatos"
    return render_template('contatos.html')