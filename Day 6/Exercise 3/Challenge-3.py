#WARNING: Use this Python file only with Reeborg's World
#Hurdle 2 Challenge

# Function to turn around
def turn_around():
    turn_left()
    turn_left()


# Function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Function to jump hurdle
def hurdle_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# Repeat hurdle jump until it finds the flag
while not at_goal():
    hurdle_jump()