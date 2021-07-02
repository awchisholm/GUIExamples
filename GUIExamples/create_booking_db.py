import sqlite3
from contextlib import closing
import os

def init_db(database_file, database_sql):
    with closing(connect_db(database_file)) as db:
        with open(database_sql, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

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