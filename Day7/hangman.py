import random
from hangman_words import word_list
from hangman_art import logo, stages
from utils import clear

print(logo)
print('Welcome to Hangman game')

chosen_word = random.choice(word_list)
shown_word = ['_' for l in chosen_word]

lives = 6
end_of_game = False

while not end_of_game:
    
    guess = input('Guess a letter:  ').lower()
    clear()
    if guess in chosen_word:
        shown_word = [guess if guess == l else shown_word[i] for i,l in enumerate(chosen_word)] 
    else:    
        lives -= 1
        
        if lives == 0:
            end_of_game = True
            print('You lose.')
            
    print(f"{' '.join(shown_word)}")

    if "_" not in shown_word:
        end_of_game = True
        print('You win.')

    print(stages[lives])

    
    