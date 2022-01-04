import sql_handling 
import time

db = "booking_database.db"

insertFlag = True

query = "select * from bookings"
insert = "insert into bookings (customerid, slotid, number) values (2, 2, 2)"

for index in range(100000):
    if insertFlag:
        sql_handling.execute_sql(db, insert)
        #time.sleep(0.0001)
    else:
       rows = sql_handling.query_connection(db, query)

#availability = sql_handling.execute_sql(db, query)
# insert into bookings (customerid, slotid, number) values (2, 2, 2)