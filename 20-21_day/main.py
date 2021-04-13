from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
suna = Snake()
food = Food()
score = Scoreboard()

screen.onkey(suna.up, "Up")
screen.onkey(suna.down, "Down")
screen.onkey(suna.left, "Left")
screen.onkey(suna.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    suna.move()

    # Detect collision with food.
    if suna.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        suna.extend()

    for segment in suna.segments[1:]:
        if suna.head.distance(segment) < 10:
            score.reset()
            score.update_score()
            suna.reset()

    if suna.head.xcor() > 280 or suna.head.xcor() < -280 or suna.head.ycor() > 280 or suna.head.xcor() < -280:
            score.reset()
            score.update_score()
            suna.reset()
screen.exitonclick()
