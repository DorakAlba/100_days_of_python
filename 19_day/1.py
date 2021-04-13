import turtle
import random

# t = turtle.Turtle()
sc = turtle.Screen()
sc.setup(width=500, height=500)
bet = sc.textinput(title="bake your be", prompt="select you turtle")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

race_active = True
turtles = []
for tur in range(0, 6):
    ben = turtle.Turtle(shape='turtle')
    ben.penup()
    ben.color(colors[tur])
    ben.goto(x=-230, y=(tur * 40) - 100)
    turtles.append(ben)

while race_active:
    for turke in turtles:
        turke.forward(random.randint(0, 10))
        if turke.position()[0] > 200:
            race_active = False
            wiiner = turke.pencolor()
if bet == wiiner:
    print(f"your {bet} turkey won!")
else:
    print(f"{wiiner} is winer,  you turkey {bet} lost")
# sc.listen()
# sc.onkey(move_forward, 'w')
# sc.onkey(move_back, 's')
# sc.onkey(rotate_l, 'a')
# sc.onkey(rotate_r, 'd')
# sc.onkey(t.reset, 'r')
sc.exitonclick()
