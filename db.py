import sqlite3
import string
from random import choice

# connects table
db = sqlite3.connect("users.db")
cursor = db.cursor()

# creates table if one doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id TEXT,
username TEXT,
password TEXT
)
""")
db.commit()

# generates random id
def generate_id():
    id = ""
    for i in range(10):
        if choice((0,1))==0:
            id += choice(string.ascii_letters)
        else:
            id += choice(string.digits)

    return id

# adds a user to the database
def add_user(username, password):
    cursor.execute(f'''
SELECT * FROM users WHERE username = '{username}'                   
''')

    if cursor.fetchone() is None:

        cursor.execute(f'''
INSERT INTO users VALUES
('{generate_id()}','{username}','{password}')
''')
        db.commit()
        return True
    
    else:
        return False

# checks a users credentials
def check_user(username, password):
    cursor.execute(f'''
SELECT * FROM users WHERE username = '{username}' and password = '{password}'
''')
    if cursor.fetchone() is None:
        return False
    else:
        return True