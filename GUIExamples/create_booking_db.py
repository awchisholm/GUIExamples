import sqlite3
from contextlib import closing
import os

def init_db(database_file, database_sql):
    conn = sqlite3.connect(database_file)   # open the sqlite database file
    cursor = conn.cursor()                  # connect to it and get a cursor - this is like a placeholder in the database
    script = open(database_sql, 'r')        # open the script file containing SQL
    sql = script.read()                     # read the contents of the script into a string called sql
    cursor.executescript(sql)               # execute the SQL 
    conn.commit()                           # commit the changes to make them permanent
    conn.close()                            # close the connection to the database

def connect_db(database_file):
    return sqlite3.connect(database_file)

def delete_db(database_file):
    if os.path.exists(database_file):
        os.remove(database_file)

if __name__ == '__main__':
    database_file = 'booking_database.db'
    database_sql = 'create_booking_db.sql'
    delete_db(database_file)
    init_db(database_file, database_sql)