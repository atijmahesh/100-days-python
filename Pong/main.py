from turtle import Screen
from paddle import Paddle 
from ball import Ball  
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #detect r paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    #detect l paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    
    

screen.exitonclick()
