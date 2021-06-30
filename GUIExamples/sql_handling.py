import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def query_connection(conn, query):
    """
    Query the database using the connection
    :param conn: connection object
    :param query: query string
    :return: Result as a list
    """
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

if __name__ == '__main__':
    main()