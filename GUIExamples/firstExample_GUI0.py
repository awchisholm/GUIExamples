from guizero import App, Text
app = App(title="Hello there")

firstmessage = Text(app, text="This is big text")
secondmessage = Text(app, text="This is green")
thirdmessage = Text(app, "This is red")
firstmessage.text_size=40
secondmessage.bg="green"
thirdmessage.bg="red"
thirdmessage.font='courier'

app.display()