#Stworz relacyjny model bazy danych biblioteki. Wprowadz do niej prszykladowe dane

import sqlite3

connection = sqlite3.connect('Ksiazka.db')
cursor = connection.cursor()


cursor.execute(
    '''
      CREATE TABLE Ksiazka
        (
          id INTEGER PRIMARY KEY ASC,
          Tytul TEXT,
          Autor TEXT,
          RokWydania INTEGER
        )
    '''
)

cursor.execute(
    '''
      CREATE TABLE Biblioteka
        (
          id INTEGER PRIMARY KEY ASC,
          ksiazkaID INTEGER NOT NULL,
          FOREIGN KEY(ksiazkaID) REFERENCES Ksiazka(id) 
        )
    '''
)

cursor.execute('''INSERT INTO Ksiazka VALUES (1, 'Ksiazka1', 'Mickiewicz', 1992 )''')
cursor.execute('''INSERT INTO Ksiazka VALUES (2, 'Ksiazka2', 'Prus', 1994)''')
cursor.execute('''INSERT INTO Ksiazka VALUES (3, 'Ksiazka3', 'Szymborska', 2008)''')

for row in cursor.execute('''SELECT * FROM Ksiazka'''):
    print row

connection.close()