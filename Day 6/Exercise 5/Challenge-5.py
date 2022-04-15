#WARNING: Use this Python file only with Reeborg's World
#Hurdle 4 Challenge

# Function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Function to jump hurdle
def hurdle_jump():
    turn_left()
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() == True:
        move()
    turn_left()

# Repeat hurdle jump until it finds the flag
while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        hurdle_jump()