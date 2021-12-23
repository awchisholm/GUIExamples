import sql_handling 

db = "booking_database.db"

query = "select * from bookings"
for index in range(1000000):
    rows = sql_handling.query_connection(db, query)
    print(rows)