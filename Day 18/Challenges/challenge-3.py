########### Challenge 3 - Draw Shapes ########
from turtle import Turtle
from random import choice

turtle = Turtle()
turtle.speed(2)
turtle.pensize(3)
colors = ['LightGreen', 'DarkTurquoise', 'Orange', 'MediumPurple', 'MediumSlateBlue', 'RoyalBlue', 'Crimson', 'Gold', 'Sienna', 'CadetBlue']


def draw_shape(sides):
    angle = 360 / sides
    for j in range(sides):
        turtle.forward(100)
        turtle.right(angle)


for i in range(3, 11):
    random_color = choice(colors)
    turtle.color(random_color)
    draw_shape(i)



