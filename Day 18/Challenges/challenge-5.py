########### Challenge 4 - Random Walk with Random Colors ########
from turtle import Turtle
import random

turtle = Turtle()
turtle.speed("fastest")
colors = ['LightGreen', 'DarkTurquoise', 'Orange', 'MediumPurple', 'MediumSlateBlue', 'RoyalBlue', 'Crimson', 'Gold', 'Sienna', 'CadetBlue']


def draw_spirograph(size):
    for i in range(int(360 / size)):
        random_color = random.choice(colors)
        turtle.color(random_color)
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size)


draw_spirograph(5)
