import sqlite3

#ESTABLISH A CONNECTION AND A CURSOR
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

#QUERY ALL DATA BASED ON CONDITION
cursor.execute("Select * from events WHERE date = '2088.10.15'")
rows = cursor.fetchall()
print(rows)

#INSERT NEW ROWS
new_rows = [('Cats', 'Cat City', '2088.10.17'), ('Hens', 'Hen City', '2088.10.17')]
cursor.executemany("INSERT INTO events VALUES(?,?,?)",new_rows)
connection.commit()

#QUERY ALL DATA
cursor.execute("Select * from events")
rows = cursor.fetchall()
print(rows)
