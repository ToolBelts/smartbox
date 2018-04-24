import sqlite3

sql_create_table = "create table if not exists ideas(id integer primary key, product text , title text, description text, vote int default 0)"

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

cursor.execute(sql_create_table)

query_remove = "delete from ideas"

connection.commit()

cursor.execute(query_remove)

connection.commit()
