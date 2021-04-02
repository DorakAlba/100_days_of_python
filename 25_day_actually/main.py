import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('Us States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
tu = turtle.Turtle()
tu.penup()
tu.hideturtle()
tu.color('black')
data = pd.read_csv('50_states.csv')

print(data)
answered = 0
game_on = True
answer = []
while game_on:
    take_answer = screen.textinput(title=f'{answered}/50 States Correct', prompt='State name')
    if take_answer in data.values and take_answer not in answer:
        answer.append(take_answer)
        answered += 1
        x = data[data['state'] == take_answer]['x'].item()
        y = data[data['state'] == take_answer]['y'].item()
        tu.goto(x, y)
        tu.write(take_answer, align='center', font=(('Arial'), 10, 'normal'))
    if answered ==50:
        game_on = False
screen.exitonclick()
