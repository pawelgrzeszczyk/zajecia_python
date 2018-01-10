# Zmodyfikuj poprzedni program tak aby transakcja dodawania wartosci zostala anulowana
#Przetestuj rownierz inne metody zarzadzajace transakcjami

import sqlite3

connection = sqlite3.connect('ksiazki.db')

cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS
ksiazka (id integer, t text, a text, rok integer)''')

cursor.execute('''INSERT INTO ksiazka VALUES (1, 'Ksiazka1', 'Mickiewicz', 1992 )''')
cursor.execute('''INSERT INTO ksiazka VALUES (2, 'Ksiazka2', 'Prus', 1994)''')
cursor.execute('''INSERT INTO ksiazka VALUES (3, 'Ksiazka3', 'Szymborska', 2008)''')
cursor.execute('''DELETE FROM ksiazka WHERE id=3''')
cursor.execute('''UPDATE ksiazka set rok = 2000 WHERE id= 1 ''')
cursor.execute('''INSERT INTO ksiazka VALUES (4, 'Ksiazka4', 'Marchewka', 1994)''')


for row in cursor.execute('''SELECT * FROM ksiazka'''):
    print row

connection.close()