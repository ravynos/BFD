import sqlite3

DB = "banco_ficticio.db"

def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()

    # Apaga tabelas antigas para garantir esquema coreto. (útil em ambiente de aula)

    cur.execute("DROP TABLE IF EXISTS pedidos;")
    cur.execute("DROP TABLE IF EXISTS clientes;")
    con.commit()

    #Cria tabela clientes
    cur.execute(""" CREATE TABLE clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT,
                telefone TEXT,
                cidade TEXT
                )
                """)
    
    #Cria a tabela pedidos
    cur.execute("""
            CREATE TABLE pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente INTEGER,
                produto TEXT NOT NULL,
                valor REAL NOT NULL,
                FOREIGN KEY (id_cliente) REFERENCES clientes(id)
                );
                """)
    con.commit()

    #Insert clientes (id previsíveis 1..6)
    clientes = [
        ("Ana Silva", "ana@email.com", "(62)99999-1111", "Goiânia"),
        ("Bruno Santos", "bruno@email.com", "(62)98888-2222", "Anápolis"),
        ("Carlos Oliveira", "carlos@email.com", "(21)98888-3333", "Rio de Janeiro"),
        ("Mariana Costa", "mariana@email.com", "(31)97777-4444", "Belo Horizonte"),
        ("Fernanda Lima", "fernanda@email.com", "(64)95555-5555", "Rio Verde"),
        ("Fábio Mendes", "fabio@email.com", "(62)95555-1111", "Goiânia")
    ]

    cur.executemany("INSERT INTO clientes (nome, email, telefone, cidade) VALUES (?, ?, ?, ?);", clientes)

    con.commit()

    pedidos = [
        (1, "Notebook", 3500.00),
        (1, "Mouse", 120.00),
        (2, "Cadeira Gamer", 950.00),
        (3, "Celular", 2500.00),
        (4, "Teclado", 220.00),
        (5, "Monitor", 890.00),
        (6, "Headset", 310.00),
        (6, "Pen Drive 64GB", 50.00),
    ]

    cur.executemany("INSERT INTO pedidos (id_cliente, produto, valor) VALUES (?, ?, ?);", pedidos)
    con.commit()
    
    print("✅ Banco 'banco_ficticio.db' criado e populado com sucesso!")

    # Mostrar resumo para verificaççao rápida
    print("\nClientes (id | nome | cidade):")
    cur.execute("SELECT id, id_cliente, produto, valor FROM pedidos ORDER BY id;")

    for r in cur.fetchall():
        print(r)

    print("\nPedidos (id | id_cliente | produto | valor):")
    cur.execute("SELECT id, id_cliente, produto, valor FROM pedidos ORDER BY id;")
    
    for r in cur.fetchall():
        print(r)

    con.close

if __name__ == "__main__":
    main()