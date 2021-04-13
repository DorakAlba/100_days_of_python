import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
tu = Player()
score = Scoreboard()
screen.onkey(tu.go, 'Up')
manager = CarManager()
for _ in range(5):
    manager.spawn_car()
level = 0
game_is_on = True
while game_is_on:
    manager.spawn_car()
    manager.move(level)
    time.sleep(0.1)
    screen.update()
    if manager.collision(tu.position()[0], tu.position()[1]):
        tu.goto(0, -250)
    if tu.distance(0, 300) < 30:
        tu.goto(0, -250)
        level += 1
        score.update_score()
