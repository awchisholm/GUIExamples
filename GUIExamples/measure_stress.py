from guizero import App, TextBox, PushButton, Text, info, Slider, Picture
import sql_handling 
import time
#import pandas as pd
import matplotlib.pyplot as plt

db = "booking_database.db"

app=App()
lbl_name = Text(app, text='Select number of iterations')
slider = Slider(app, start=100, end=10000)

def plot_timings(timings, filename):
    plt.plot(timings)
    plt.title('Time per iteration')
    plt.xlabel('Iteration')
    plt.ylabel('Time in seconds')
    plt.savefig(filename)
    p = plt.close()
    picture.image = filename
    picture.visible = True

def measure_db():
    loop_counter = int(slider.value)
    print('Measuring query performance')
    query = "select * from bookings"
    start_the_clock = time.perf_counter()
    inside_timings = []
    for index in range(loop_counter):
        start_the_clock_inside = time.perf_counter()
        rows = sql_handling.query_connection(db, query)
        stop_the_clock_inside = time.perf_counter()
        time_diff_inside = stop_the_clock_inside - start_the_clock_inside
        inside_timings.append(time_diff_inside)

    stop_the_clock = time.perf_counter()
    time_diff = stop_the_clock - start_the_clock
    time_per_record = time_diff / loop_counter

    plot_timings(inside_timings, 'inside_timings.png')

    print(f'Fetch performance for {loop_counter} records {time_diff}')
    print(f'Average time for 1 record {time_per_record}')
    print('Ending measuring query performance')
    
#lbl_name = Text(app, text='Measure query performance')
btn_go = PushButton(app, command=measure_db, text='Measure query performance')
picture = Picture(app, image='inside_timings.png')
picture.visible = False

app.display()
