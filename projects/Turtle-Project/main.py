from turtle import Turtle, Screen
import random
turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color("dark red")

def draw_shape(sides):
    R = random.random()
    B = random.random()
    G = random.random()

    turtle1.color(R, G, B)
    angle = 360/sides
    for i in range(0, sides):
        turtle1.forward(100)
        turtle1.right(angle)

def randWalk():
    R = random.random()
    B = random.random()
    G = random.random()
    turtle1.color(R, G, B)
    choice = random.randint(1, 4)
    if choice == 1:
        turtle1.right(0)
    elif choice == 2:
        turtle1.right(90)
    elif choice == 3:
        turtle1.right(180)
    else:
        turtle1.right(270)
    turtle1.forward(30)

def randColor():
    return (random.random(), random.random(), random.random())

turtle1.speed("fastest")
def draw_spiro(gapSize):
    for _ in range(int(360/gapSize)):
        turtle1.color(randColor())
        turtle1.circle(100)
        turtle1.setheading(turtle1.heading()+gapSize)
        turtle1.circle(100)

draw_spiro(100)


screen = Screen()
screen.exitonclick()
