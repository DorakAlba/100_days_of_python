COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random as rd
from turtle import Turtle


class CarManager():
    def __init__(self):
        self.cars = []
        self.counter = 0

    def spawn_car(self):
        if self.counter == 5:
            new_car = Turtle()
            new_car.penup()
            new_car.color(rd.choice(COLORS))
            new_car.shape('square')
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.goto(325, rd.randint(-230, 250))
            self.cars.append(new_car)
            self.counter = 0
        else:
            self.counter += 1

    def move(self, iteration=0):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * iteration)

    def collision (self, x, y):
        for car in self.cars:
            if car.distance(x,y)<20:
                return True
