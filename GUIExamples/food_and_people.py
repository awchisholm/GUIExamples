from guizero import App, Combo, Text, Window, PushButton, ListBox
import sqlite3
from contextlib import closing
import os

database_file = 'people_and_food.db'

def do_query(database, q):
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute(q)
    rows = cur.fetchall()
    cur.close()
    return(rows)

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

def handleFood():
    query = 'select Food from foodandbeverage'
    food = do_query(database=database_file, q=query)
    for row in food:
        onerow = f"{row[0]}"
        foodlistbox.append(onerow)

database_sql = 'food.sql'
delete_db(database_file)
init_db(database_file, database_sql)

app = App()

foodlistbox = ListBox(app, width='fill', command = handleFood)

app.display()