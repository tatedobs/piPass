import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (ID int, name text, status int, class int)''')
print (c.execute("SELECT * FROM users"))

def add_user(name, input_id, class_id):
    c.execute("INSERT INTO users(ID, name, status, class_id) VALUES (n)")

conn.commit()
conn.close()
