import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS videogames 
            (name TEXT,game_publisher TEXT)''')
c.execute('INSERT INTO videogames VALUES ("Doom eternal","Bethesda")')
conn.commit()

values=[
("Assassins Creed", "Ubisoft"),
("Mass effect", "Bioware"),
("Call of duty","Activision"),
("Super Mario brothers 2","Nintendo")
]
c.executemany('INSERT INTO videogames VALUES(?,?)',values)
conn.commit()
c.execute('SELECT * FROM videogames')
data=c.fetchall()
print("Printing the entire table:")
print(data)
print("Printing the table with rowid:")
c.execute("SELECT rowid,name FROM videogames")
data=c.fetchall()
print(data)
print("Deleting contents from the record where the rowid is 5:")
c.execute("DELETE FROM videogames WHERE rowid=2")
conn.commit()
c.execute("SELECT * FROM videogames")
data=c.fetchall()
print(data)
c.execute("UPDATE videogames SET name='Mass effect 2' WHERE rowid=3")
conn.commit()
c.execute("SELECT * FROM videogames")
data=c.fetchall()
print(data)