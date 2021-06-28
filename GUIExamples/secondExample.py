from guizero import App, TextBox, PushButton, Text, info
app=App()

def btn_go_clicked():
    info(text = "hello" + txt_name.value, title = '?')

lbl_name = Text(app, text='Helloooo')
txt_name = TextBox(app)
btn_go = PushButton(app, command=btn_go_clicked, text='Done')

app.display()