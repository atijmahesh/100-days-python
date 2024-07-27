from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_position()

    def reset_position(self):
        self.goto(STARTING_POSITION)
    
    def move_up(self):
        newY = self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(), newY)
    
    def move_down(self):
        newY = self.ycor()-MOVE_DISTANCE
        self.goto(self.xcor(), newY)

