import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
race_on = False

user_bet = screen.textinput(title='Your bet', prompt='Choose the color of your turtle:')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

for turtle_index in range(0, 6):
    Andy = Turtle(shape='turtle')
    Andy.color(colors[turtle_index])
    Andy.penup()
    Andy.goto(x=-220, y= 150- turtle_index * 60)
    all_turtles.append(Andy)


def race():
    if user_bet:
        race_on = True
    while race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                winner = turtle.color()
                race_on = False
            distance = random.randint(0, 10)
            turtle.forward(distance)
    retun winner

win = race()
if win == user_bet:
    print('You won!')
else:
    print(f'You lose!')
 print(f'The {win} turtle is the winner!')


screen.exitonclick()