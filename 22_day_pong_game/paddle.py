from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.penup()
        self.color('white')
        self.speed('fastest')
        if player == '1':
            self.goto(350, 0)
        else:
            self.goto(-350, 0)
        self.shape('square')
        # self.width(20)
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        # self.height(350)

    def move_up(self):
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        self.setheading(270)
        self.forward(20)
