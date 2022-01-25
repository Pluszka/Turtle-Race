from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Your bet', prompt='Choose the color of your turtle:')

Andy = Turtle()


screen.exitonclick()