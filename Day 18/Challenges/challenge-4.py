########### Challenge 4 - Random Walk ########
from turtle import Turtle
from random import choice

turtle = Turtle()
turtle.speed(10)
turtle.pensize(11)
colors = ['LightGreen', 'DarkTurquoise', 'Orange', 'MediumPurple', 'MediumSlateBlue', 'RoyalBlue', 'Crimson', 'Gold', 'Sienna', 'CadetBlue']
angles = [0, 90, 180, 270]


def move_randomly(angle):
    turtle.setheading(angle)
    turtle.forward(30)


for i in range(250):
    random_color = choice(colors)
    random_angle = choice(angles)
    turtle.color(random_color)
    move_randomly(random_angle)


# ########### Challenge 4 - Random Walk with Random Colors ########
# import turtle as t
# import random
#
# turtle = t.Turtle()
# t.colormode(255)
# t.speed(10)
# t.pensize(12)
# angles = [0, 90, 180, 270]
#
#
# def move_randomly(angle):
#     t.setheading(angle)
#     t.forward(25)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# for i in range(400):
#     random_angle = random.choice(angles)
#     t.color((random_color()))
#     move_randomly(random_angle)


