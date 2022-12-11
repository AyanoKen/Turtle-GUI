from turtle import Turtle, Screen
import random

fishy = Turtle()

screen = Screen()
screen.colormode(255)

fishy.shape("turtle")

fishy.penup()
fishy.left(90)
fishy.forward(200)
fishy.right(90)
fishy.pendown()

for i in range(100):
    sides = i + 4
    angle = (360/sides)

    color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    fishy.pencolor(color)

    for j in range(sides):
        fishy.forward(50)
        fishy.right(angle)




    
    


screen.exitonclick()