from turtle import Turtle, Screen

fishy = Turtle()
screen = Screen()

fishy.shape("turtle")

turn_amount = 5

def move():
    fishy.forward(5)

def turn_left():
    fishy.left(turn_amount)

def turn_right():
    fishy.right(turn_amount)

screen.listen()

screen.onkeypress(key="w", fun= move)
screen.onkeypress(key="a", fun= turn_left)
screen.onkeypress(key="d", fun= turn_right)

screen.exitonclick()