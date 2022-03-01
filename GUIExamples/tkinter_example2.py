from guizero import App, Text
from tkinter import Spinbox

app = App()
text = Text(app, text="A Spinbox widget")

spinbox = Spinbox(from_=0, to=10)
app.add_tk_widget(spinbox)

app.display()