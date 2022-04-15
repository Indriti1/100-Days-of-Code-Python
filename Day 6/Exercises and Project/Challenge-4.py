#WARNING: Use this Python file only with Reeborg's World
#Hurdle 3 Challenge

# Function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Function to jump hurdle
def hurdle_jump():
    move()
    in_place_jump()


# Function to jump in-place
def in_place_jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# Repeat hurdle jump until it finds the flag
while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        in_place_jump()