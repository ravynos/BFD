# Importando o módulo SQLite
import sqlite3

# Criando conexão com o banco
conn = sqlite3.connect('SCC/cadastro.db' )
c = conn.cursor()
# Criando tabela de usuários
c.execute( '''CREATE TABLE IF NOT EXISTS clientes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
idade INTEGER
)''' )

# Salvando alterações e fechando conexão conn.commit()
conn.commit()
conn.close()