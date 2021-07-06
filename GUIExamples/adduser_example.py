from tkinter import Grid
from guizero import App, Text, TextBox, PushButton, info, Window, ListBox
import sql_handling 
import create_booking_db

db = 'adduser.db'
sql = 'create_adduser.sql'

loggedin = False
username_global = ""

def show_login_status():
    global username_global
    if loggedin == True:
        loginstatus.bg = 'green'
        loginstatus.value = username_global
    else:
        loginstatus.bg = 'red'
        loginstatus.value = "select login"

def login():
    global loggedin
    global username_global
    print('login')
    conn = sql_handling.create_connection(db)
    #m = hashlib.sha256()
    #m.update(password.value.encode())
    #hashed_password = m.hexdigest()
    query = "select password from users where username = '{0}' and password = '{1}'".format(username_main.value, password_main.value)
    print(query)
    rows = sql_handling.query_connection(conn, query)
    conn.close()
    loggedin = False
    username_global = ''
    if len(rows) == 1:
        # We have logged in 
        print('logged in')
        loggedin = True
        username_global = username_main.value
        addentry_window.show(wait=True)

    return

def logout():
    print('logout')

def adduser():
    print('adduser')
    newuserwindow.show(wait=True)
    #newuserwindow.visible=True
    #app.disable = True

def add():
    print('add')
    conn = sql_handling.create_connection(db)
    sql_statement = "insert into users (username, password) values ('{0}', '{1}')".format(username_newuser.value, password_newuser.value)
    print(sql_statement)
    rows = sql_handling.execute_sql(conn, sql_statement)
    print(rows)
    newuserwindow.hide()


def cancel():
    print('cancel')
    newuserwindow.hide()

def getoldentries():
    conn = sql_handling.create_connection(db)
    query = "select entry from entries"
    rows = sql_handling.query_connection(conn, query)
    print(rows)
    result = ''.join([str(item[0])+'\n' for item in rows])  # convert list to string with a newline between each
    print(result)
    return result

def addentry():
    print("addentry")
    conn = sql_handling.create_connection(db)
    sql_statement = "insert into entries (username, entry) values ('{0}', '{1}')".format(username_newuser.value, newentry_window.value)
    print(sql_statement)
    rows = sql_handling.execute_sql(conn, sql_statement)
    print(rows)
    oldentries.value = getoldentries()

create_booking_db.delete_db(db)
create_booking_db.init_db(db,sql)

app = App(title="Booking", layout='grid')

userprompt_main = Text(app, text='username', grid=[0,0])
username_main = TextBox(app, grid=[1,0])
passprompt_main = Text(app, text='password', grid=[0,1])
password_main = TextBox(app, hide_text=True, grid=[1,1])
loginbutton_main = PushButton(app, command = login, text = 'Login', grid=[2,0])
logoutbutton_main = PushButton(app, command = adduser, text = 'Add user', grid=[3,0])

newuserwindow = Window(app, title='New user', visible=False, layout='grid')
userprompt_newuser = Text(newuserwindow, text='username', grid=[0,0])
username_newuser = TextBox(newuserwindow, grid=[1,0])
passprompt_newuser = Text(newuserwindow, text='password', grid=[0,1])
password_newuser = TextBox(newuserwindow, hide_text=True, grid=[1,1])
loginbutton_newuser = PushButton(newuserwindow, command = add, text = 'Add', grid=[2,0])
logoutbutton_newuser = PushButton(newuserwindow, command = cancel, text = 'Cancel', grid=[3,0])

addentry_window = Window(app, title='Add an entry', visible = False, layout='grid')
newentryprompt_window = PushButton(addentry_window, text='Add', command = addentry, grid = [1,0])
newentry_window = TextBox(addentry_window, grid=[0,0])
oldentries = TextBox(addentry_window, text=getoldentries(), grid = [0,1], multiline=True, height=10, width=40, scrollbar=True, enabled=False)

app.display()