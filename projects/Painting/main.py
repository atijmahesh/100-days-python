import colorgram
from turtle import Turtle, Screen
import random
# rgb_colors = []
# colors = colorgram.extract('./projects/Painting/image.jpg', 50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     col = (r, g, b)
#     rgb_colors.append(col)

# print(rgb_colors)


color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]
def randColor():
    return random.choice(color_list)

screen = Screen()
screen.colormode(255)
pen = Turtle()

pen.penup()
pen.hideturtle()
pen.setheading(225)
pen.forward(300)
pen.setheading(0)
number_of_dots = 100
pen.speed("fastest")

for dot_count in range(1, number_of_dots+1):
    pen.dot(20, randColor())
    pen.forward(50)
    if dot_count%10 == 0:
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)

        

screen.exitonclick()