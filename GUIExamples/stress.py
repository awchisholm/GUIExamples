import sqlite3

def query_connection(db_file, query):
    conn = sqlite3.connect(db_file, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

db = "booking_database.db"
query = "select * from bookings"
for index in range(100):
    rows = query_connection(db, query)
