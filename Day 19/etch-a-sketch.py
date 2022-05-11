from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_clockwise():
    turtle.setheading(turtle.heading() + 10)


def turn_counter_clockwise():
    turtle.setheading(turtle.heading() - 10)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_clockwise, "a")
screen.onkey(turn_counter_clockwise, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()
