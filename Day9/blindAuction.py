from art import logo
from utils import clear

print(logo)
print("Welcome to the secret auction program.")

bids = {}
loop_continue = True
while loop_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bids[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        loop_continue = False
    clear()

winner = max(bids, key=bids.get)
print("The winner is {} with a bid of {}".format(winner, bids[winner]))