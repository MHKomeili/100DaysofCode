import menu
import coffee_maker
import money_machine

coffee_mach_1 = coffee_maker.CoffeeMaker()
money_mach_1 = money_machine.MoneyMachine()
today_menu = menu.Menu()
is_on = True
while is_on:
    choice = input(f"What do you like? ({today_menu.get_items()}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_mach_1.report()
        money_mach_1.report()
    else:
        drink = today_menu.find_drink(choice)
        if coffee_mach_1.is_resource_sufficient(drink) and money_mach_1.make_payment(drink.cost):
            coffee_mach_1.make_coffee(drink)
