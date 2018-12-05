import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id int, username text, password text)"

cursor.execute(create_table)

user = [(1, 'jose', 'asdf'),
        (2, 'gary', 'pw')]

insert_query = 'INSERT INTO users VALUES (?, ?, ?)'

cursor.executemany(insert_query, user)

select = "select * from users"
for row in cursor.execute(select):
    print(row)


connection.commit()

connection.close()