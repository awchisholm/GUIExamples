from guizero import App, Text, TextBox, PushButton, info, Window
import sql_handling 

db = "booking.db"
conn = sql_handling.create_connection(db)
rows = sql_handling.query_connection(conn, "select * from users")
found = str(len(rows))

def check_password():
    conn = sql_handling.create_connection(db)
    query = "select password from users where username = '{0}' and password = '{1}'".format(username.value, password.value)
    rows = sql_handling.query_connection(conn, query)
    logged_in = False
    if len(rows) == 1:
       info("the", "same")
       logged_in = True
    return logged_in

app = App(title=found)
text = Text(app, text="Enter password")
username = TextBox(app)
password = TextBox(app, hide_text=True)
button6 = PushButton(app, command=check_password)

app.display()