import random 
from art import logo, vs
from utils import clear
from game_data import data


def pick_randomly():
    item_dict = random.choice(data)
    return item_dict

def display(itemA, itemB):
    print(f"Compare A: {itemA['name']}, {itemA['description']}, from {itemA['country']}.")
    print(vs)
    print(f"Against B: {itemB['name']}, {itemB['description']}, from {itemB['country']}.")
    
def compare(itemA, itemB, user_guess):
    answer = itemA['follower_count'] > itemB['follower_count']

    return not (answer ^ ( user_guess == "A"))  # xnor ->  not xor

def game():
    
    score = 0
    itemA = pick_randomly()
    
    clear()
    while True:
        print(logo)
        itemB = pick_randomly()

        display(itemA, itemB)

        guess = input("Who has more followers? Type 'A' or 'B'? ")
        clear()
        if compare(itemA, itemB, guess):
            score += 1
        else:
            break
        itemA = itemB.copy()
        

    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")


game()