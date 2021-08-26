import random
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def rules():
    return '''Here are the rules:
paper beats rock,
rock beats scissors, 
scissors beats paper\n'''

def lap():
    return '''"s" --> start
"r" --> rules
"q" --> quit\n'''

def RPS(player:int, computer:int) -> str:
    winner = ''
    if player == 0 and computer == 2:
        winner = 'player'
    elif player == 2 and computer == 0:
        winner = 'computer'
    else:
        if player > computer:
            winner = 'player'
        elif computer > player:
            winner = 'computer'
        else:
            winner = 'draw'
    return winner


rock = '''
    _______
---'  _____)
      (_____)
      (_____)
      (____)
---.__(___)    
'''

paper = '''
    _______
---'  _____)____
         _______)
         ________)
        ________)
---.__________)    
'''

scissors = '''
    _______
---'    ___)____
           _____)
        _________)
       (___)
---.___(__)    
'''

moves = [rock, paper, scissors]

greeting ='''
 
 =======================================
| Welcome to Rock, Paper, Scissors game |
 =======================================
'''
clear()
print(greeting) 
print('In order to Start the game, insert "s", to get the rules of the game, insert "r" and to quit, insert "q"')

while True:
    choice = input(lap())
    clear()
    if choice == 's':
        player = int(input('Let it all begin. What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors:\n'))
        computer = random.randint(0,2)

        print(moves[player])
        print('\n'+'_'*100 +'\n')
        print('Computer chose:')
        print(moves[computer])
        print('\n'+'_'*100 +'\n')

        winner = RPS(player, computer)
        if winner == 'computer':
            print('Oh, You lose :(')
        elif winner == 'player':
            print('Hooray, you won ;)')
        else:
            print('That was Close, a draw')
    elif choice == 'r':
        print(rules())
    elif choice == 'q':
        print("Goodbye, have fune :)")
        break
    else:
        print('Wrong input.')