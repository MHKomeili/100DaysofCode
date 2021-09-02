import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        if random.randint(1, 6) == 6:
            new_car = Turtle(shape='square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
