print("Welcome to the treasure island. Your mission is to find the treasure")

direction = input('You are at a crossroad. Which way do you want to go? Type "left" or "right"? ')
if direction == "right":
    print("You fell into a hole. Game over!")
elif direction == "left":
    print("Here you are")
    do = input('Which one do you want to do? "swim" or "wait"? ')
    if do == "swim":
        print("Sharks were really hungry. Game over!")
    elif do == "wait":
        door = input('Which door would you like to walk through? "red", "green" or "blue"? ')
        if door == "red":
            print("You chose the room full of fire. Game over!")
        elif door == "green":
            print("Thieves were waiting for you .Game over!")
        elif door == "blue":
            print("You win. Here's the treasure.")
        else:
            print("You chose a door that doesn't exist. Game over!")
    else:
        print("This task made you exhuasted. Game over!")
else:
    print("Unfortunately, you chose the wrong direction. Game over!")