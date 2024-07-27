from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.write(f"Score = {self.score}", align="center", font=('ArcadeClassic', 24, 'normal'))
    
    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=('ArcadeClassic', 24, 'normal'))
    
    def game_over(self):
        self.goto((0,0))
        self.write(f"GAME OVER.", align="center", font=('ArcadeClassic', 24, 'normal'))