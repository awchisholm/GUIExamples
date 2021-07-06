from os import truncate
from tkinter import Grid
from guizero import App, Text, TextBox, PushButton, info, Window, ListBox
from datetime import datetime

import sql_handling             # import my sql_handling module
import create_booking_db        # import my create books db module

db = 'adduser.db'               # the file containing the sqlite database
sql = 'create_adduser.sql'      # the file containing the SQL DDL commands to create the database

def login():
    print('*** login')
    conn = sql_handling.create_connection(db)
    #m = hashlib.sha256()
    #m.update(password.value.encode())
    #hashed_password = m.hexdigest()
    query = "select password from users where username = '{0}' and password = '{1}'".format(username_main.value, password_main.value)
    rows = sql_handling.query_connection(conn, query)
    conn.close()
    if len(rows) == 1:
        # We have logged in 
        print('logged in')
        addentry_window.show(wait=True)
    else:
        password_main.value = ''
        username_main.value = ''
    oldentries.value = getoldentries()
    return

def logout():
    print('*** logout')
    username_newuser.value = ''
    password_newuser.value = ''

def add():
    print('*** add')
    newuserwindow.show(wait=True)

def adduser():
    print('*** adduser')
    conn = sql_handling.create_connection(db)
    sql_statement = "insert into users (username, password) values ('{0}', '{1}')".format(username_newuser.value, password_newuser.value)
    rows = sql_handling.execute_sql(conn, sql_statement)
    newuserwindow.hide()

def cancel():
    print('*** cancel')
    newuserwindow.hide()

def getoldentries_rawall():
    print('*** getoldentries_rawall')
    conn = sql_handling.create_connection(db)
    query = "select entry, timestamp from entries where username = '{0}' order by timestamp desc".format(username_main.value)
    rows = sql_handling.query_connection(conn, query)
    return rows

def getoldentries_raw():
    print('*** getoldentries_raw')
    rows = getoldentries_rawall()
    result = [row[0] for row in rows]
    print(result)
    return(result)

def getoldentries():
    print('*** getoldentries')
    rows = getoldentries_raw()
    result = ''.join([str(item[0])+'\n' for item in rows])  # convert list to string with a newline between each
    print(result)
    return result

def updatelistbox(items):
    oldentries.clear()
    for index in range(len(items)):
        oldentries.insert(index, items[index])

def addentry():
    print("*** addentry")
    now = datetime.now()
    now_string = now.strftime("%Y%m%d%H%M%S.%f")
    items = getoldentries_raw()
    updatelistbox(items)
    addentry_window.show(wait=True)
    conn = sql_handling.create_connection(db)
    sql_statement = "insert into entries (username, entry, timestamp) values ('{0}', '{1}', '{2}')".format(username_main.value, newentry_window.value, now_string)
    rows = sql_handling.execute_sql(conn, sql_statement)
    items = getoldentries_raw()
    updatelistbox(items)

def listentries(value):
    print("***listentries")
    print(value)

def deletelatest():
    print("*** deletelatest")
    rows = getoldentries_rawall()
    if len(rows) > 0:
        conn = sql_handling.create_connection(db)
        sql_statement = "delete from entries where timestamp = {0}".format(rows[0][1])
        row = sql_handling.execute_sql(conn, sql_statement)
    items = getoldentries_raw()
    updatelistbox(items)

create_booking_db.delete_db(db)
create_booking_db.init_db(db,sql)

app = App(title="Booking", layout='grid')

userprompt_main = Text(app, text='username', grid=[0,0])
username_main = TextBox(app, grid=[1,0])
passprompt_main = Text(app, text='password', grid=[0,1])
password_main = TextBox(app, hide_text=True, grid=[1,1])
loginbutton_main = PushButton(app, command = login, text = 'Login', grid=[2,0])
logoutbutton_main = PushButton(app, command = add, text = 'Add user', grid=[3,0])

newuserwindow = Window(app, title='New user', visible=False, layout='grid')
userprompt_newuser = Text(newuserwindow, text='username', grid=[0,0])
username_newuser = TextBox(newuserwindow, grid=[1,0], )
passprompt_newuser = Text(newuserwindow, text='password', grid=[0,1])
password_newuser = TextBox(newuserwindow, hide_text=True, grid=[1,1])
loginbutton_newuser = PushButton(newuserwindow, command = adduser, text = 'Add', grid=[2,0])
logoutbutton_newuser = PushButton(newuserwindow, command = cancel, text = 'Cancel', grid=[3,0])

addentry_window = Window(app, title='Add an entry', visible = False, layout='grid')
newentry_window = TextBox(addentry_window, grid=[0,0])
newentryprompt_window = PushButton(addentry_window, text='Add', command = addentry, grid = [1,0])
#oldentries = TextBox(addentry_window, text=getoldentries(), grid = [0,1], multiline=True, height=10, width=40, scrollbar=True, enabled=True)
oldentries = ListBox(addentry_window, items=getoldentries_raw(), grid = [0,1], enabled=True, command=listentries, multiselect=False)
deletelast_window = PushButton(addentry_window, text='Delete latest', command=deletelatest, grid=[1,1])

app.display()