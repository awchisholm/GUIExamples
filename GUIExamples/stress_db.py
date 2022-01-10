from guizero import App, TextBox, PushButton, Text, info, Slider, CheckBox
import sql_handling 
import time

db = "booking_database.db"

app=App()
lbl_name = Text(app, text='Select number of iterations')
slider = Slider(app, start=100, end=10000)
insert_or_query = CheckBox(app, 'Check to insert, uncheck to query')

def stress_db():
    print('Starting stress db')
    query = "select * from bookings"
    insert = "insert into bookings (customerid, slotid, number) values (2, 2, 2)"
    insertFlag = int(insert_or_query.value)
    print(insertFlag)
    print(slider.value)
    for index in range(slider.value):
        if insertFlag == 1:
            sql_handling.execute_sql(db, insert)
            time.sleep(0.001)
        else:
            rows = sql_handling.query_connection(db, query)
    print('Ending stress db')
    
btn_go = PushButton(app, command=stress_db, text='Stress Start')

app.display()