import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

#cursor.execute("INSERT INTO pessoas VALUES('Maria', 40, 'maria_123@gmail.com')")
#cursor.execute("INSERT INTO pessoas VALUES('Thiago', 38, 'th.sobrinho@gmail.com')")

#banco.commit()

#cursor.execute("SELECT * FROM pessoas")
#print(cursor.fetchall())

#cursor.execute("DELETE FROM pessoas WHERE nome = 'Maria'")
#banco.commit()

#pessoas = [('Ayra', 4), ('Aquilles', 15), ('Lucilene', 38), ('Fatima', 64), ('Vicente', 65)]

#cursor.executemany("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", pessoas)

#banco.commit()

cursor.execute("SELECT * FROM pessoas")
for linha in cursor.fetchall():
    print(linha)