from turtle import Turtle, Screen
import time
from snake import Snake
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
suna = Snake()
screen.onkey(suna.up, "Up")
screen.onkey(suna.down, "Down")
screen.onkey(suna.left, "Left")
screen.onkey(suna.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    Snake.move(suna)

screen.exitonclick()
