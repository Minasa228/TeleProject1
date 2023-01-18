import sqlite3


def login(text1, text2):
    db = sqlite3.connect('teleprogramms.db')
    c = db.cursor()
    a = c.execute(f"SELECT login, password FROM users WHERE login = '{text1}' AND password = '{text2}'")
    db.commit()
    if not c.fetchone():
        return(0)
    else:
        return(1)

    c.close()
    db.close()
