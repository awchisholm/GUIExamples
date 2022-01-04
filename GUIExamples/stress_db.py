from guizero import App, TextBox, PushButton, Text, info
import sql_handling 
import time

db = "booking_database.db"

app=App()

def stress_db():
    print('Starting stress db')
    query = "select * from bookings"
    insert = "insert into bookings (customerid, slotid, number) values (2, 2, 2)"
    insertFlag = True
    for index in range(1000):
        if insertFlag:
            sql_handling.execute_sql(db, insert)
            time.sleep(0.001)
        else:
            rows = sql_handling.query_connection(db, query)
    print('Ending stress db')
    
lbl_name = Text(app, text='Stress')
btn_go = PushButton(app, command=stress_db, text='Stress Start')

app.display()