# Greeting
print("Hello and welcome to tip calculator")

total = int(input("What is the total bill? $"))

tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

peoples = int(input("How many people to split the bill? "))

tip = total / 100 * tip_percent
total_cost = total + tip

print(f"Each person should pay ${round(total_cost / peoples, 2)}")