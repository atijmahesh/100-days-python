from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
guess = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
yPos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    t = Turtle("turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(-230, yPos[turtle_index])
    all_turtles.append(t)

if guess:
    is_race_on = True

while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winCol = t.pencolor()
            if winCol == guess:
                print(f"You've won! The {winCol} is the winner!")
            else: 
                print(f"You've lost! The {winCol} is the winner!")

        d = random.randint(0, 10)
        t.forward(d)
    

screen.exitonclick()