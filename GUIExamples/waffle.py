from guizero import App, Waffle

app = App()

x=1
y=2
my_waffle = Waffle(app)
my_waffle.pixel(x,y).color = "red"
my_waffle[x,y].dotty = True

app.display()
