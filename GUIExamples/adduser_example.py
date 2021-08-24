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
    username_newuserwindow.value = ''
    password_newuserwindow.value = ''

def add():
    print('*** add')
    username_newuserwindow.value=''
    password_newuserwindow.value=''
    firstname_newuserwindow.value=''
    surname_newuserwindow.value=''
    email_newuserwindow.value=''
    newuserwindow.show(wait=True)

def adduser():
    print('*** adduser')
    conn = sql_handling.create_connection(db)
    sql_statement = "insert into users (username, password, firstname, surname, email) values ('{0}', '{1}', '{2}', '{3}', '{4}')".format(username_newuserwindow.value, password_newuserwindow.value, firstname_newuserwindow.value, surname_newuserwindow.value, email_newuserwindow.value)
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
    sql_statement = "insert into entries (username, entry, timestamp) values ('{0}', '{1}', '{2}')".format(username_main.value, newentry_entrywindow.value, now_string)
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

def maintainuser():
    print("*** maintain")
    # populate the form with the entry from the database
    conn = sql_handling.create_connection(db)
    query = "select username, password, firstname, surname, email from users where username = '{0}' and password = '{1}'".format(username_newuserwindow.value, password_newuserwindow.value)
    print (query)
    rows = sql_handling.query_connection(conn, query)
    if (len(rows) == 1):
        print("one row found")
        print(rows)
        username_maintainwindow.value = rows[0][0]
        password_maintainwindow.value = rows[0][1]
        firstname_maintainwindow.value = rows[0][2]
        surname_maintainwindow.value = rows[0][3]
        email_maintainwindow.value = rows[0][4]
    # make the maintain window visible
    maintainwindow.show(wait=True)

def updateuser_frommaintain():
    print("*** updateuser_frommaintain")
    # use the values in the form to update the user details
    conn = sql_handling.create_connection(db)
    sql_statement = "update users set username = '{0}', password = '{1}', firstname = '{2}', surname = '{3}', email = '{4}' where username = '{0}' and password = '{1}'".format(username_maintainwindow.value, password_maintainwindow.value, firstname_maintainwindow.value, surname_maintainwindow.value, email_maintainwindow.value)
    print (sql_statement)
    row = sql_handling.execute_sql(conn, sql_statement)
    print(row)
    maintainwindow.hide()

def cancel_frommaintain():
    print("*** cancel_frommaintain")
    maintainwindow.hide()

def deleteuser_frommaintain():
    print("*** deleteuser_frommaintain")
    conn = sql_handling.create_connection(db)
    sql_statement = "delete from users where username = '{0}' and password = '{1}'".format(username_maintainwindow.value, password_maintainwindow.value)
    print (sql_statement)
    row = sql_handling.execute_sql(conn, sql_statement)
    maintainwindow.hide()

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
userprompt_newuserwindow = Text(newuserwindow, text='username', grid=[0,0])
username_newuserwindow = TextBox(newuserwindow, grid=[1,0], )
passprompt_newuserwindow = Text(newuserwindow, text='password', grid=[0,1])
password_newuserwindow = TextBox(newuserwindow, hide_text=True, grid=[1,1])
firstnameprompt_newuserwindow = Text(newuserwindow, text='firstname', grid=[0,2])
firstname_newuserwindow = TextBox(newuserwindow, grid=[1,2])
surnameprompt_newuserwindow = Text(newuserwindow, text='surname', grid=[0,3])
surname_newuserwindow = TextBox(newuserwindow, grid=[1,3])
emailprompt_newuserwindow = Text(newuserwindow, text='email', grid=[0,4])
email_newuserwindow = TextBox(newuserwindow, grid=[1,4])
addbutton_newuser = PushButton(newuserwindow, command = adduser, text = 'Add', grid=[0,5])
maintainbutton_newuserwindow = PushButton(newuserwindow, command = maintainuser, text = 'Maintain', grid=[1,5])
cancelbutton_newuserwindow = PushButton(newuserwindow, command = cancel, text = 'Cancel', grid=[2,5])

addentry_window = Window(app, title='Add an entry', visible = False, layout='grid')
newentry_entrywindow = TextBox(addentry_window, grid=[0,0])
newentryprompt_entrywindow = PushButton(addentry_window, text='Add', command = addentry, grid = [1,0])
oldentries = ListBox(addentry_window, items=getoldentries_raw(), grid = [0,1], enabled=True, command=listentries, multiselect=False)
deletelast_entrywindow = PushButton(addentry_window, text='Delete latest', command=deletelatest, grid=[1,1])

maintainwindow = Window(app, title='Maintain user', visible = False, layout='grid')
usernameprompt_maintainwindow = Text(maintainwindow, text='username', grid=[0,0])
username_maintainwindow = TextBox(maintainwindow, grid=[1,0])
passwordprompt_maintainwindow = Text(maintainwindow, text='password', grid=[0,1])
password_maintainwindow = TextBox(maintainwindow, hide_text=True, grid=[1,1])
firstnameprompt_maintainwindow = Text(maintainwindow, text='firstname', grid=[0,2])
firstname_maintainwindow = TextBox(maintainwindow, grid=[1,2])
surnameprompt_maintainwindow = Text(maintainwindow, text='surname', grid=[0,3])
surname_maintainwindow = TextBox(maintainwindow, grid=[1,3])
emailprompt_maintainwindow = Text(maintainwindow, text='email', grid=[0,4])
email_maintainwindow = TextBox(maintainwindow, grid=[1,4])
updatebutton_maintainwindow = PushButton(maintainwindow, command = updateuser_frommaintain, text = 'Update', grid=[1,5])
deletebutton_maintainwindow = PushButton(maintainwindow, command = deleteuser_frommaintain, text = 'Delete', grid=[2,5])
cancelbutton_maintainwindow = PushButton(maintainwindow, command = cancel_frommaintain, text = 'Cancel', grid=[3,5])

app.display()