from platform import python_version_tuple
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
    
def execute_sql(db_file, sql_statement):
    conn = create_connection(db_file)
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()
    cur.execute(sql_statement)
    conn.commit()
    conn.close()
    return cur.lastrowid

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
    
def handlePerson():
    query = 'select FirstName from Person'
    persons = do_query(database=database_file, q=query)
    for person in persons:
        onerow = f"{person[0]}"
        personlistbox.append(onerow)

def handleFavourites():
    query = '''
    select Person.FirstName, FoodAndBeverage.Food from Favourite
    left join Person, FoodAndBeverage
    on Favourite.PersonID=Person.ID and
    Favourite.FoodID=FoodAndBeverage.ID'''
    favourites = do_query(database=database_file, q=query)
    for favourite in favourites:
        onerow = f"{favourite[0]} : {favourite[1]}"
        favouriteslistbox.append(onerow)

database_sql = 'food.sql'
delete_db(database_file)
init_db(database_file, database_sql)

app = App()

foodlistbox = ListBox(app, width='fill', command = handleFood)
personlistbox = ListBox(app, width='fill', command = handlePerson)
favouriteslistbox = ListBox(app, width='fill', command = handleFavourites)

app.display()