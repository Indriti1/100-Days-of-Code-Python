#WARNING: Use this Python file only with Reeborg's World
#Hurdle 3 Challenge

# Function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Function for maze escaping
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not right_is_clear() and front_is_clear():
        move()
    else:
        turn_left()