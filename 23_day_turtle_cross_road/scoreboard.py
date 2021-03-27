FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-100, 250)
        self.color('Black')
        self.write(f"score: {self.score}", font = FONT)

    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"score: {self.score}", font = FONT)