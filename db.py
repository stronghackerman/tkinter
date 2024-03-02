import sqlite3
import string
from random import choice
from cryptography.fernet import Fernet

key = b'8Rtg89kJ0sXkiOdJ5Cy7ySGqNBCMp9VR2a_xOU-kBas='
e = Fernet(key)

# connects table
db = sqlite3.connect('users.db')
cursor = db.cursor()

# creates table if one doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
id TEXT,
username TEXT,
password TEXT
)
''')
db.commit()

# encrypt function
def encrypt(to_encrypt):
    return e._encrypt_from_parts(to_encrypt.encode(), 0, b'\xbd\xc0,\x16\x87\xd7G\xb5\xe5\xcc\xdb\xf9\x07\xaf\xa0\xfa')

# generates random id
def generate_id():
    id = ''
    for i in range(10):
        if choice((0,1))==0:
            id += choice(string.ascii_letters)
        else:
            id += choice(string.digits)

    return id

# adds a user to the database
def add_user(username, password):
    username = encrypt(username).decode()
    password = encrypt(password).decode()

    cursor.execute('''
    SELECT * FROM users WHERE username = ?
''', (username,))


    if cursor.fetchone() is None:

        cursor.execute('''
        INSERT INTO users VALUES (?, ?, ?)
''', (generate_id(), username, password))

        db.commit()
        return True
    
    else:
        return False

# checks a users credentials
def check_user(username, password):
    username = encrypt(username).decode()
    password = encrypt(password).decode()

    cursor.execute('''
    SELECT * FROM users WHERE username = ? AND password = ?
''', (username, password))

    if cursor.fetchone() is None:
        return False
    else:
        return True