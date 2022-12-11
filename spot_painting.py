from turtle import Turtle, Screen
import random

fishy = Turtle()

screen = Screen()
screen.colormode(255)

fishy.shape("turtle")

fishy.penup()
fishy.left(180)
fishy.forward(500)
fishy.left(90)
fishy.forward(200)
fishy.left(90)


for side in range(10):
    for i in range(10):

        color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        fishy.dot(20, color)
        fishy.forward(50)

    color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    fishy.dot(20, color)

    if side % 2 == 0:
        fishy.left(90)
        fishy.forward(50)
        fishy.left(90)
    else:
        fishy.right(90)
        fishy.forward(50)
        fishy.right(90)
    
    

screen.exitonclick()