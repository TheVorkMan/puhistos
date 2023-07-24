import sqlite3

def create_connection(db_file):
    """Создает соединение с базой данных SQLite"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('Соединение с базой данных установлено')
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """Создает таблицу в базе данных"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print('Таблица создана успешно')
    except sqlite3.Error as e:
        print(e)

def main():
    # Создаем соединение с базой данных
    conn = create_connection("database.db")

    # Создаем таблицу
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT
        );
    """
    create_table(conn, create_table_sql)

    # Закрываем соединение
    conn.close()

if __name__ == '__main__':
    main()