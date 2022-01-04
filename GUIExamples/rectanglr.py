from guizero import App, Text, TextBox, PushButton, error

# Method to calculate the area
def calculate():

    # Validation to check whether they typed in numbers
    if not height.value.isdigit() or not width.value.isdigit():
        error("Input error", "You must type in numbers for height and width")
    # Depth is allowed to be a digit or blank
    elif not depth.value.isdigit() and depth.value != "":
        error("Input error", "You must type in a number for depth")

    # Perform the calculation
    else:
        area = int( height.value ) * int( width.value )
        if depth.value == "":        
            result.value = str(area) + "cm squared"
        else:
            volume = area * int(depth.value)
            result.value = str(volume) + "cm cubed"
        

# Set up the app
app = App("Area and Volume calculator", layout="grid")

width_label = Text(app, text="Width:", grid=[0,0], align="left")
width = TextBox(app, grid=[1,0], align="left", width=30)

height_label = Text(app, text="Height:", grid=[0,1], align="left")
height = TextBox(app, grid=[1,1], align="left", width=30)

depth_label = Text(app, text="Depth:", grid=[0,2], align="left")
depth = TextBox(app, grid=[1,2], align="left", width=30)

button = PushButton(app, calculate, text="Calculate", grid=[1,3])

result_label = Text(app, text="Result:", grid=[0,4], align="left")
result = TextBox(app, grid=[1,4], align="left", width=30)

app.display()
