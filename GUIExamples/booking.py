from guizero import App, Text, TextBox, PushButton, info, Window
import sql_handling 

db = "booking.db"
loggedin = False
user = ""

def show_login_status():
    if loggedin == True:
        loginstatus.bg = 'green'
        loginstatus.value = user
    else:
        loginstatus.bg = 'red'
        loginstatus.value = "select login"

def showlogin():
    login_window.show()

def login():
    global loggedin
    global user
    conn = sql_handling.create_connection(db)
    query = "select password from users where username = '{0}' and password = '{1}'".format(username.value, password.value)
    rows = sql_handling.query_connection(conn, query)
    loggedin = False
    user = ''
    if len(rows) == 1:
       loggedin = True
       user = username.value
    
    show_login_status()
    login_window.hide()
    return

def logout():
    global loggedin
    global user
    loggedin = False
    username.value = ''
    password.value = ''
    user = ''
    show_login_status()

app = App(title="Booking")
loginstatus = Text(app)
show_login_status()

login_window = Window(app, title = "Login", height=300, width=200, layout='grid')
login_window.hide()
userprompt = Text(login_window, text='username', grid=[0,0])
username = TextBox(login_window, grid=[1,0])
passprompt = Text(login_window, text='password', grid=[0,1])
password = TextBox(login_window, hide_text=True, grid=[1,1])
okpass = PushButton(login_window, command = login, text = 'OK', grid=[1,2])
login_button = PushButton(app, command = showlogin, text = 'Login')
logout_button = PushButton(app, command = logout, text = 'Logout')

app.display()