from turtle import Turtle, Screen
import random

fishy = Turtle()

screen = Screen()
screen.colormode(255)

fishy.shape("turtle")
fishy.speed(10)

fishy.pensize(8)

for i in range(1000):
    direction = random.choice([90, -90])

    color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    fishy.pencolor(color)

    fishy.right(direction)
    fishy.forward(20)

screen.exitonclick()