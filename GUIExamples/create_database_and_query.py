# https://towardsdatascience.com/python-pandas-and-sqlite-a0e2c052456f
import pandas as pd
import sqlite3 as sql
import PySimpleGUI as sg                       

ps3 = pd.read_csv('ps3.csv')
ps3_connection =  sql.connect('ps3.db')
ps3.to_sql('ps3', ps3_connection, if_exists='replace')

query = 'select year, sum(Global_Sales) as Sales from ps3 group by year order by year asc'
sales_by_year = pd.read_sql(query, ps3_connection)

ps3_connection.close()

layout = [[sg.Text(query)],
          [sg.Multiline('Query results will go here', key = '-output-', size=(45,5))],
          [sg.Button('Ok'), sg.Button('Quit')]]

window = sg.Window('Query', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()  # read into event and values
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-output-'].update(sales_by_year)

# Finish up by removing from the screen
window.close()