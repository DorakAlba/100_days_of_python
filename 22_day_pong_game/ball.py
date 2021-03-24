from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('circle')
        self.speed(6)
        self.setheading(145)

    def forwd(self):
        self.forward(8)
        # new_x = self.xcor() + 10
        # new_y = self.ycor() + 10
        # self.goto(new_x,new_y)

    def mirror(self):
        if 90 < self.heading() < 180 or 0 < self.heading() > 270:
            self.setheading(self.heading()+90)
        else:
            self.setheading(self.heading()-90)

    def reverse(self, distance):
        self.setheading(self.heading()+180 - distance )



