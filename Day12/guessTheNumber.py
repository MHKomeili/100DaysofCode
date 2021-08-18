import random
from art import logo

def pick_number():
    number = random.randint(1,100)
    return number


def compare(answer, guess):
    if answer > guess:
        return "Too low"
    elif answer < guess:
        return "Too high"
    else:
        return "Correct"


LEVEL_TRIES = {"easy": 10, "hard": 5}

def game():
    print(logo)

    print("Welcome to Guess The Number game :)")
    print("I'm thinking of a number between 1 and 100.")
    game_level = input("Choose difficulty. type 'easy' or 'hard': ")
    user_tries = LEVEL_TRIES[game_level]
    print(f"You have {user_tries} attempts left to guess the number.")

    answer = pick_number()

    while user_tries:
        guess = int(input("make a guess: "))
        result = compare(answer, guess)
        print(result)
        if result == "Correct":
            break
        
        user_tries -= 1
        print(f"You have {user_tries} attempts left to guess the number.")

    if user_tries == 0:
        print(f"You lose. the number was {answer}.")
    else:
        print("You won.")

game()