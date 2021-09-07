import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_data = {row.letter: row.code for (index, row) in df.iterrows()}

name = input("Insert your name: ").upper()

nato_equivalent = [nato_data[letter] for letter in name]

print(nato_equivalent)
