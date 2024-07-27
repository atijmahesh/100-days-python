from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
    
    def gen_car(self):
        # Generate a new car and add it to the cars list
        self.cars.append(Car())
    
    def increase_speed(self):
        # Increase the speed of all cars
        for car in self.cars:
            car.level_up()
    
    def move_cars(self):
        # Move all cars and remove or reset them if they move off-screen
        for car in self.cars:
            car.move()
            if car.xcor() < -310:
                car.goto(300, random.randint(-250, 250))

    def collides(self, player_x, player_y):
        for car in self.cars:
            car_half_width = 20 
            car_half_height = 10 
            car_left = car.xcor() - car_half_width
            car_right = car.xcor() + car_half_width
            car_top = car.ycor() + car_half_height
            car_bottom = car.ycor() - car_half_height

            if (car_left < player_x < car_right) and (car_bottom < player_y < car_top):
                return True

        return False


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2) 
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))
        self.move_dist = STARTING_MOVE_DISTANCE
    
    def move(self):
        new_x = self.xcor() - self.move_dist
        self.goto(new_x, self.ycor())
    
    def level_up(self):
        self.move_dist += MOVE_INCREMENT
