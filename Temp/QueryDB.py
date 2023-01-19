import sqlite3


class QueryDB:
    db = sqlite3.connect('teleprogramms.db')

    # Create Cursor
    c = db.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS users (
        login TEXT NOT NULL,
        password TEXT NOT NULL,
        access INTEGER DEFAULT 0
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS films (
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        channel TEXT NOT NULL
    )""")

    db.commit()

    # Удаление таблицы
    # c.execute("DROP TABLE films")

    # Добавление данных
    # c.execute("INSERT INTO users VALUES ('user123', '1234', 0)")
    # c.execute("INSERT INTO users VALUES ('admin', 'admin', 1)")

    # Удаление данных
    # c.execute("DELETE FROM users WHERE rowid > 2")

    # Обновление данных
    # c.execute("UPDATE users SET login = 'user1234' WHERE login = 'user123'")

    # Выборка данных
    # c.execute("SELECT rowid, * FROM users")
    # result = c.fetchall()
    # print(result)
    # print(c.fetchall())
    # print(c.fetchmany(1))
    # print(c.fetchone()[0])

    # for el in items:
    #    print(el[1] + "\n" + el[2])

    @staticmethod
    def insert_db(table_name, value1, value2, value3):
        db = sqlite3.connect('teleprogramms.db')
        c = db.cursor()
        c.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?)", (value1, value2, value3))
        db.commit()
        db.close()

    @staticmethod
    def delete_db(table_name, column, value):
        db = sqlite3.connect('teleprogramms.db')
        c = db.cursor()
        c.execute(f"DELETE FROM {table_name} WHERE {column} = '{value}'")
        db.commit()
        db.close()

    @staticmethod
    def update_db(table_name, column, value, condition, condition_value):
        db = sqlite3.connect('teleprogramms.db')
        c = db.cursor()
        c.execute(f"UPDATE {table_name} SET {column} = '{value}' WHERE {condition} = '{condition_value}'")
        db.commit()
        db.close()

    db.close()
