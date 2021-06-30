from guizero import App, Text

def double_click():
    double_click_me.value = "Thanks"

app = App()

double_click_me = Text(app, text="Double click me")
double_click_me.when_double_clicked = double_click

app.display()
