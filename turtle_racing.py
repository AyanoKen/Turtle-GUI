from turtle import Turtle, Screen
import random

def create_turtle(turtle_color, position):
    dummy = Turtle()
    dummy.shape("turtle")
    dummy.color(turtle_color)
    dummy.penup()
    dummy.goto(-400, position)

    return dummy

def run_game():
    screen = Screen()

    colors = ["red", "orange", "yellow", "green", "blue", "purple", "bisque", "aquamarine"]
    turtle_list = []
    width = 1000
    height = 600

    screen.setup(width= width, height= height)

    offset = height / len(colors)

    for i in range(len(colors)):
        y_axis = (height/2) - (i * offset) - (offset/2)

        turtle_list.append(create_turtle(colors[i], y_axis)) 


    user_choice = screen.textinput(title= "Make a bet", prompt= "Choose a turtle to bet on")

    if user_choice: 
        start_race = True
    else:
        start_race = False

    while start_race:
        for i in range(len(turtle_list)):
            move_distance = random.randint(0, 10)
            turtle_list[i].forward(move_distance)

            if turtle_list[i].xcor() >= width / 2:
                start_race = False
                print(f"The winner is the {colors[i]} turtle")

                if user_choice.lower() == colors[i]:
                    print("You win!")
                else:
                    print("You lose! Try again")


    screen.exitonclick()

run_game()