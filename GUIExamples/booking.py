from guizero import App, Text, TextBox, PushButton, info, Window, ListBox
import sql_handling 
import create_booking_db
import hashlib
from datetime import datetime
import time

db = "booking_database.db"
sql_ddl_file = 'create_booking_db.sql'
#create_booking_db.delete_db(db)
#create_booking_db.init_db(db, sql_ddl_file)

loggedin = False
user = ""
userid = 0
slotid = 0

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
    global userid
    m = hashlib.sha256()
    m.update(password.value.encode())
    hashed_password = m.hexdigest()
    query = "select * from administrators where username = '{0}' and password = '{1}'".format(username.value, hashed_password)
    rows = sql_handling.query_connection(db, query)
    print(rows[0][0])
    loggedin = False
    user = ''
    if len(rows) == 1:
        # We have logged in 
        loggedin = True
        user = username.value
        userid = rows[0][0]
    
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
    query = "select distinct slots.date from slots order by date asc"
    rows = sql_handling.query_connection(db, query)
    dates = [row[0].strftime("%Y-%m-%d %H:%M:%S") for row in rows]
    return(dates)

def date_chosen():
    global slotid
    datefeedback.visible = False
    datefeedback.value = ""
    book_button.visible = False
    chosen_date = date_chooser.value
    query = """select slots.maximum_available - total(bookings.number), slots.slotid
	           from slots 
	           left join bookings 
	           on slots.rowid=bookings.slotid 
	           where slots.date like '%""" + chosen_date + "%'"
    availability = sql_handling.query_connection(db, query)
    available_slots = int(availability[0][0])
    slotid = availability[0][1]
    
    if available_slots > 0:
        book_button.visible = True
        datefeedback.value = "" + str(available_slots) + " slots available on " + chosen_date
        datefeedback.visible = True
    else:
        book_button.visible = False
        datefeedback.value = ""
        datefeedback.visible = False
    print(available_slots)
    print(slotid)
    print(query)

def book_now():
    print('Book now')
    print(date_chooser.value)
    print(slotid)
    # Check there are some bookings to be had
    # get details of customer
    # insert into the customer table if required
    # 
    # Choose the first customer for now
    chosen_customer_id = 1
    # Set the number to book to be 2 for now
    number_to_book = 2
    # Get the rowid of the slot we are using

    querystring = "insert into bookings (customerid, slotid, number) values ({customerid}, {slotid}, {number_to_book})"
    query = querystring.format(customerid=int(chosen_customer_id), slotid=int(slotid), number_to_book=int(number_to_book))

    print(query)
    start_the_clock = time.perf_counter()
    availability = sql_handling.execute_sql(db, query)
    stop_the_clock = time.perf_counter()
    time_diff = stop_the_clock - start_the_clock
    print(time_diff, 'performance in seconds')

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
datefeedback = Text(booking_window, '', grid=[1,0])
datefeedback.visible=False
book_button = PushButton(booking_window, command=book_now, text='Book Now', grid=[1,1])
book_button.visible=False

app.display()
