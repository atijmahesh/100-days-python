import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
loopCount = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if loopCount%6==0:
        car_manager.gen_car()
    car_manager.move_cars()

    if car_manager.collides(player.xcor(), player.ycor()):
        print("here")
        game_is_on = False
    
    if player.ycor() >= 280:
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.level_up()

    loopCount += 1

screen.exitonclick()
