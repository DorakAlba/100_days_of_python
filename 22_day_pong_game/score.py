from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.speed(0)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,200)
        self.write(f'Score {self.score1} : {self.score2}','center', font = (('Arial'), 10, 'normal'))



    def update_score(self, added1, added2):
        if added1:
            self.score1+=1
        else:
            self.score2+=1
        self.clear()
        self.goto(0,200)
        self.write(f'Score {self.score1} : {self.score2}','center', font = (('Arial'), 10, 'normal'))


