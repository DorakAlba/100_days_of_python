from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

import time

screen = Screen()

screen.bgcolor('black')
screen.title('PONG!')
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)
game_is_on = True

right_player = Paddle('1')
left_player = Paddle('2')
ball = Ball()
screen.onkey(right_player.move_up, 'Up')
screen.onkey(right_player.move_down, 'Down')
screen.onkey(left_player.move_up, 'w')
screen.onkey(left_player.move_down, 's')
score = Score()
while game_is_on:
    time.sleep(0.05)
    ball.forwd()
    screen.update()
    # print(ball.xcor(),right_player.ycor())
    # print ((ball.ycor() - left_player.ycor()) , ball.xcor())
    # print(ball.heading())
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.mirror()
    if ball.xcor() < -310 and -50 < (ball.ycor() - left_player.ycor()) < 50:
        # print('true')ww
        ball.reverse(ball.ycor() - left_player.ycor())
        # ball.mirror()
    if ball.xcor() > 310 and -50 < (ball.ycor() - right_player.ycor()) < 50:
        ball.reverse(ball.ycor() - left_player.xcor())

    if ball.xcor() > 350:
        ball.goto(0, 0)
        ball.setheading(150)
        score.update_score(False,True)
    if ball.xcor() < - 350:
        ball.goto(0, 0)
        ball.setheading(30)
        score.update_score(True, False)


screen.exitonclick()
