import sqlite3


# Creating table into database!!!
def connect_db():
    # Connect to sqlite database
    conn = sqlite3.connect('users.db')
    print("DB connection established")
    return conn


def create_tables(conn):
    # cursor object
    cursor = conn.cursor()
    # drop query
    cursor.execute("DROP TABLE IF EXISTS user")
    # create query
    query = """CREATE TABLE user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname CHAR(50) NOT NULL,
            email CHAR(25),
            password CHAR(50)
             )"""
    cursor.execute(query)

    # # create query
    cursor.execute("DROP TABLE IF EXISTS token")
    query = """CREATE TABLE token(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id CHAR(25),
            token CHAR(500),
            expiry int not null
             )"""
    cursor.execute(query)
    # commit and close
    conn.commit()


def close_db_conn(conn):
    conn.close()
    print("DB connection closed")


if __name__ == "__main__":
    conn = connect_db()
    create_tables(conn)
    close_db_conn(conn)
