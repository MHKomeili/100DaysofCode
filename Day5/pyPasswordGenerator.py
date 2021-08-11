import random 

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
"M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]

symbols = ["@", "#", "%", "&", "*", "?", "-", "_"]

print("Welcome to PyPasswordGenerator")

nr_letters = int(input('How many letters would you like in your password?\n'))
nr_numbers = int(input('How many numbers would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like in your password?\n'))

chosen_chars = []
for i in range(nr_letters):
    chosen_chars.append(random.choice(letters))
for i in range(nr_numbers):
    chosen_chars.append(random.choice(numbers))
for i in range(nr_symbols):
    chosen_chars.append(random.choice(symbols))

random.shuffle(chosen_chars)
password = ''.join(chosen_chars)

print(f"Here is your password: \t{password} \nkeep it safe.")
