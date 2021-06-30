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

def check_password():
    global loggedin
    global user
    conn = sql_handling.create_connection(db)
    query = "select password from users where username = '{0}' and password = '{1}'".format(username.value, password.value)
    rows = sql_handling.query_connection(conn, query)
    loggedin = False
    user = ''
    if len(rows) == 1:
       #info("the", "same")
       loggedin = True
       user = username.value
    
    show_login_status()
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

username = TextBox(app)
password = TextBox(app, hide_text=True)
login_button = PushButton(app, command=check_password, text = 'Login')
logout_button = PushButton(app, command = logout, text = 'Logout')

app.display()