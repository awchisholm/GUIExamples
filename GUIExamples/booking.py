from guizero import App, Text, TextBox, PushButton, info, Window, ListBox
import sql_handling 
import create_booking_db
import hashlib
from datetime import datetime

db = "booking_database.db"
sql = 'create_booking_db.sql'
create_booking_db.delete_db(db)
create_booking_db.init_db(db,sql)

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
    m = hashlib.sha256()
    m.update(password.value.encode())
    hashed_password = m.hexdigest()
    query = "select password from administrators where username = '{0}' and password = '{1}'".format(username.value, hashed_password)
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
    global loggedin
    global user
    loggedin = False
    username.value = ''
    password.value = ''
    user = ''
    show_login_status()

def handle_booking():
    booking_window.show()

def get_available_dates():
    conn = sql_handling.create_connection(db)
    query = "select distinct slots.date from slots order by date asc"
    rows = sql_handling.query_connection(conn, query)
    #dates = [row[0].strftime("%m/%d/%Y, %H:%M:%S") for row in rows]
    dates = [row[0].strftime("%Y-%m-%d %H:%M:%S") for row in rows]
    #.strftime("%m/%d/%Y, %H:%M:%S")
    return(dates)

def date_chosen():
    chosen_date = date_chooser.value
    conn = sql_handling.create_connection(db)
    query = """select slots.maximum_available - total(bookings.number)
	           from slots 
	           left join bookings 
	           on slots.slotid=bookings.slotid 
	           where slots.date like '%""" + chosen_date + "%'"
    availability = sql_handling.query_connection(conn, query)
    datefeedback.value = "" + str(int(availability[0][0])) + " slots available"
    datefeedback.visible=True
    book_button.visible=True
    print(availability[0][0])
    print(query)

def book_now():
    print('Book now')
    # insert into customers (customerid, firstname, surname) values (3, 'Steve', 'Woods')
    # INSERT into bookings (bookingid, customerid, slotid, number)   values(5, 3, 3, 2)
    # delete from bookings where bookingid = 5
    # delete from customers where customerid=3

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

booking_button = PushButton(app, command=handle_booking, text = 'Booking')

booking_window = Window(app, title='Booking', height=300, width=600, layout='grid')
booking_window.hide()

datetext = Text(booking_window, 'Choose date', grid=[0,0])
date_chooser = ListBox(booking_window, items=get_available_dates(), command = date_chosen, grid=[0,1])
datefeedback = Text(booking_window, 'Chosen date', grid=[1,0])
datefeedback.visible=False

book_button = PushButton(booking_window, command=book_now, text='Book Now', grid=[1,1])
book_button.visible=False

app.display()