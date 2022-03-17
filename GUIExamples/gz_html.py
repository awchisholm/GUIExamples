from guizero import App, Text, PushButton
from tkinter import Label
import webbrowser

app = App()
text = Text(app, text='An example browser link')

# This function handles the click and opens a web browser
def handle_webbrowser(event):
    webbrowser.open(link.cget("text"))

link = Label(app.tk, text="http://stackoverflow.com", fg="blue", cursor="hand2")
link.bind("<Button-1>", handle_webbrowser)

def handle_push():
    webbrowser.open('http://hsdc.ac.uk')

app.add_tk_widget(link)
pb = PushButton(app, command=handle_push)

app.display()
