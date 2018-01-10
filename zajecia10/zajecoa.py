import sqlite3

connection = sqlite3.connect('baza.db')

cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS
tekst (id integer, name text, value real)''')

cursor.execute('''INSERT INTO tekst VALUES (1, 'test', 1.3)''')
cursor.execute('''INSERT INTO tekst VALUES (2, 'test2', 1.4)''')

for row in cursor.execute('''SELECT * FROM tekst'''):
    print row

connection.close()