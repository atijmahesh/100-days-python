import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Name U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
FONT = ("Ariel", 14, "normal")

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

# Create a turtle for writing state names
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

while len(guessed_states) != 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break
    
    if answer_state in states:
        guessed_states.append(answer_state)

        curState = data[data.state == answer_state]
        writer.goto(curState.x.item(), curState.y.item())
        writer.write(answer_state, font = FONT)

print(missing_states)
