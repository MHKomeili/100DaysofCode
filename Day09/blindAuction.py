from art import logo
from utils import clear

print(logo)
print("Welcome to the secret auction program.")

bids = {}
finished = False
while not finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bids[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        finished = True
    clear()

winner = max(bids, key=bids.get)
print("The winner is {} with a bid of ${}".format(winner, bids[winner]))