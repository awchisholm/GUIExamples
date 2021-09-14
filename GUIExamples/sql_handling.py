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
        conn = sqlite3.connect(db_file, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    except Error as e:
        print(e)

    return conn

def query_connection(db_file, query):
    """
    Query the database using the connection
    :param db_file: database file
    :param query: query string
    :return: Result as a list
    """
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def execute_sql(db_file, sql_statement):
    """
    Execute the provided SQL using the connection
    :param db_file: database file
    :param sql_statement: sql string
    :return: nothing
    """
    conn = create_connection(db_file)
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()
    cur.execute(sql_statement)
    conn.commit()
    conn.close()
    return cur.lastrowid

if __name__ == '__main__':
    main()