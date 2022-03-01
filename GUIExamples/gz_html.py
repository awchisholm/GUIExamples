from guizero import App, Text
from tkinter import Label
import webbrowser

app = App()
text = Text(app, text='An example browser link')

# This function handles the click and opens a web browser
def handle_webbrowser(event):
    webbrowser.open(link.cget("text"))

link = Label(app.tk, text="http://stackoverflow.com", fg="blue", cursor="hand2")
link.bind("<Button-1>", handle_webbrowser)

app.add_tk_widget(link)
app.display()
