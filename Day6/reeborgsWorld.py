# Reebors's world is a website for solving challanges using python or other languages
# Go to https://reeborg.ca for documentation and challanges.
# This code is for a special challenge named "maze".

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()