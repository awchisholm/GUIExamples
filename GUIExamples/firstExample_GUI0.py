from guizero import App, Text
app = App(title="This is my first GUI")

message = Text(app, text='GUIs are cool.')
app.display()