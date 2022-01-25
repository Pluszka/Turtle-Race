import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def correct_input():
    user_bet = None
    while not user_bet in COLORS:
        user_bet = screen.textinput(title='Your bet',
        prompt=f'Choose the color of your turtle:\n{COLORS}\n')
    return user_bet


def creating_turts():
    turtles = []

    for turtle_index in range(0, 6):
        Andy = Turtle(shape='turtle')
        Andy.color(COLORS[turtle_index])
        Andy.penup()
        Andy.goto(x=-220, y=150- turtle_index * 60)
        turtles.append(Andy)
    return turtles


def race(participants):
    race_on = True
    while race_on:
        for turtle in participants:
            if turtle.xcor() > 230:
                winner = turtle.color()[0]
                race_on = False
            distance = random.randint(0, 10)
            turtle.forward(distance)
    return winner


def checking(win, user_bet):
    if win == user_bet:
        print('You won!')
    else:
        print(f'You lose!')
    print(f'The {win} turtle is the winner!')


def cleaner(spirits):
    for spirit in spirits:
        spirit.ht()


def game():
    all_turtles = creating_turts()
    checking(correct_input(), race(all_turtles))
    print('Press space to play again.')
    cleaner(all_turtles)
    screen.listen()
    screen.onkey(key='space', fun=game)

game()
screen.exitonclick()
