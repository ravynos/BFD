import sqlite3
import sys

DB = "banco_ficticio.db"

def tables_exist(cur):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('clientes', 'pedidos');")
    found =  [r[0] for r in cur.fetchall()]
    return 'clientes' in found and 'pedidos' in found

def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()

    if not tables_exist(cur):
        print("ERRO: tabelas 'cliente' e/ou 'pedidos' não encontrada. Execute primeiro setup_db.py ")
        con.close()
        sys.exit(1)

    try:
        cur.execute("""
        SELECT c.id, c.nome, c.cidade, p.produto, p.valor
        FROM clientes c
        INNER JOIN pedidos p ON c.id = p.id_cliente
        ORDER BY c.id, p.id;
        """)
        rows = cur.fetchall()

        print("\n📦 Tabela de pedidos (INNER JOIN):\n")

        print(f"{'ID':<3} {'Nome':<20} {'Cidade':<18} {'Produtos':<20} {'Valor (R$)':>10}")
        print("-" * 75)

        for idc, nome, cidade, produto, valor in rows:
            print(f"{}")