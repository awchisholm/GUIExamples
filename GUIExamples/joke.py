from guizero import App, Text, PushButton

# Method to call when button pressed
def display_joke():
   punchline.value = "Poke him on"
   
# Set up the app
app = App("Joke teller")

joke = Text(app, "How do you get Pikachu on a bus?")
punchline = Text(app, text="", color="red")
button = PushButton(app, display_joke, text="Display punchline")

app.display()