#WARNING: Use this Python file only with Reeborg's World
#Hurdle 1 Challenge

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


# Repeat hurdle jump 6 times as there are 6 hurdles
for number in range(1, 7):
    hurdle_jump()