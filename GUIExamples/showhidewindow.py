from guizero import App, Window, PushButton

def open_window():
    window.show()

app = App(title="My app", height=300, width=200)
window = Window(app, title = "2nd Window", height=300, width=200)
window.hide()

PushButton(app, text="open 2nd window", command=open_window)

app.display()
