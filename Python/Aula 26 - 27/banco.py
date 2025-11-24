# Importando o módulo SQLite
import sqlite3

# Criando conexão com o banco
conn = sqlite3.connect('banco.db' )
c = conn.cursor()
# Criando tabela de usuários
c.execute( '''CREATE TABLE IF NOT EXISTS usuarios (
id INTEGER PRIMARY KEY,
nome TEXT,
email TEXT
)''' )

# Salvando alterações e fechando conexão conn.commit()
conn.commit()
conn.close()