import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

# cursor.execute(
#     "CREATE TABLE IF NOT EXISTS produtos(id INTEGER, nome TEXT, preco REAL)")

produtos = [(1, "Laranja", 1.99), (2, "Morango", 5.99), (3, "Kiwi", 12.99)]

cursor.executemany("INSERT INTO produtos (id, nome, preco) VALUES (?,?,?)", produtos)

conexao.commit()

cursor.execute("SELECT * FROM produtos")
for linha in cursor.fetchall():
    print(linha)

