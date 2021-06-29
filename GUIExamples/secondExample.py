from guizero import App, TextBox, PushButton, Text, info
app=App()

def btn_go_clicked():
    info(text = "hello" + txt_name.value, title = '?')

def check_passwords():
    p1 = password_1.value
    p2 = password_2.value
    if p1 == p2:
        info('A','passwords the same')
    else:
        info('A','passwords different')

lbl_name = Text(app, text='Helloooo')
txt_name = TextBox(app)
btn_go = PushButton(app, command=btn_go_clicked, text='Done')

password_1 = TextBox(app, hide_text=True)
password_2 = TextBox(app, hide_text=True)
check_btn = PushButton(app, command=check_passwords, text = 'Check')

app.display()