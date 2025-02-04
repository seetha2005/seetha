import pyodbc
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-0LIN9UK;"
    "DATABASE=FlaskAppDB;"
    "Trusted_Connection=yes;"
)

# Create a cursor
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE CurrentUsers (
        ID INT PRIMARY KEY IDENTITY(1,1),
        Name VARCHAR(100),
        Email VARCHAR(100) UNIQUE
    )
''')
conn.commit()

cursor.execute("INSERT INTO CurrentUsers (Name, Email) VALUES (?, ?)", ("John Doe", "john@example.com"))
conn.commit()

cursor.execute("SELECT * FROM CurrentUsers")
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE CurrentUsers SET Name = ? WHERE ID = ?", ("Jane Doe", 1))
conn.commit()

cursor.execute("DELETE FROM CurrentUsers WHERE ID = ?", (1))
conn.commit()

cursor.close()
conn.close()