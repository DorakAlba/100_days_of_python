from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.speed('fastest')
        self.hideturtle()
        self.penup()
        self.goto(0, 150)
        self.write(f'Score: {self.score}', 'center', font=('Arial', 10, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 150)
        self.write(f'Score: {self.score}', 'center', font=('Arial', 10, 'normal'))
    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', 'center', font=('Arial', 20, 'normal'))
