import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO cars (title, content, price, shifter, transmission, consumption, motorPower, emissionCO2) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('Titre', 'descripttion', '150' ,'Automatique', 'traction', '5.0 L', '185cv', '125g/km')
            )

cur.execute("INSERT INTO cars (title, content, price, shifter, transmission, consumption, motorPower, emissionCO2) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('Titre2', 'descripttion Test', '160' ,'Manuelle', 'propulsion', '6.0 L', '150cv', '125g/km')
            )

connection.commit()
connection.close()