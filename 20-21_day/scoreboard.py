from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.speed('fastest')
        self.hideturtle()
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 150)
        self.write(f'Score: {self.score}', 'center', font=('Arial', 10, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 150)
        self.write(f'Score: {self.score}, High:Score {self.high_score}', 'center', font=('Arial', 10, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            with open('data.txt', mode='w') as data:
                data.write(str(self.score))
            self.high_score = self.score
        self.score = -1

        self.score = 0
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'Game Over', 'center', font=('Arial', 20, 'normal'))
