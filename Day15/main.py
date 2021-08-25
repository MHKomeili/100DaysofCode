from utils import clear
from data import MENU, resources

profit = 0


def report():
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: {profit}')


def process_coins():
    print("Insert your coins:")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(order, money):
    price = MENU[order]["cost"]
    if money >= price:
        should_refund = money - price
        global profit
        profit += price
        print(f"Here is ${should_refund} in change.")
        return True
    else:
        print("Sorry, not enough coins. Money refunded.")
    return False


def make_coffee(order):
    ingredients = MENU[order]["ingredients"]
    resources["water"] -= ingredients.get("water", 0)
    resources["milk"] -= ingredients.get("milk", 0)
    resources["coffee"] -= ingredients.get("coffee", 0)
    print(f"Here is your {order} ☕. Enjoy:)")


def is_resource_sufficient(order):
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def maintain_resources():
    """ Full all the resources """

    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100


clear()
is_on = True
while is_on:
    choice = input('What do you like? (espresso/latte/cappuccino): ')
    if choice == "off":
        is_on = False
    elif choice == "report":
        report()
    elif choice == "maintain":
        maintain_resources()
    else:
        if choice not in MENU:
            print("Wrong input")
            continue
        drink = choice
        if is_resource_sufficient(drink):
            paid_money = process_coins()
            status = is_transaction_successful(drink, paid_money)
            if status:
                make_coffee(drink)
