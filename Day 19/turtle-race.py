from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()


def create_turtle(turtle_name, turtle_color, y_coordinate):
    turtle_name.fillcolor(turtle_color)
    turtle_name.penup()
    turtle_name.goto(x=-230, y=y_coordinate)


def move_forwards(turtle_name):
    rand_distance = random.randint(0, 10)
    turtle_name.forward(rand_distance)


is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = -140
turtle_list = []

for color in colors:
    y_axis += 40
    new_turtle = Turtle(shape="turtle")
    create_turtle(new_turtle, color, y_axis)
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        move_forwards(turtle)


screen.exitonclick()