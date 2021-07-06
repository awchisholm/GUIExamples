from tkinter import Grid
from guizero import App, Text, TextBox, PushButton, info, Window, ListBox
import sql_handling 
import create_booking_db

db = 'adduser.db'
sql = 'create_adduser.sql'
create_booking_db.delete_db(db)
create_booking_db.init_db(db,sql)

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
    print("login")

def dologin():
    global loggedin
    global username_global
    conn = sql_handling.create_connection(db)
    #m = hashlib.sha256()
    #m.update(password.value.encode())
    #hashed_password = m.hexdigest()
    query = "select password from users where username = '{0}' and password = '{1}'".format(username.value, password.value)
    rows = sql_handling.query_connection(conn, query)
    conn.close()
    loggedin = False
    user = ''
    if len(rows) == 1:
        # We have logged in 
        loggedin = True
        user = username.value
    
    show_login_status()
    login_window.hide()
    return

def logout():
    print('logout')

def adduser():
    print('adduser')
    newuserwindow.visible=True

def add():
    print('add')
    conn = sql_handling.create_connection(db)
    sql_statement = "insert into users (username, password) values ('{0}', '{1}')".format(username_newuser.value, password_newuser.value)
    
    print(sql_statement)
    rows = sql_handling.execute_sql(conn, sql_statement)
    print(rows)
    newuserwindow.visible=False

def cancel():
    print('cancel')
    newuserwindow.visible=False

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



app.display()