from utils import clear
from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


def calculator():
    print(logo)
    operations = {'+': add, 
                '-': subtract, 
                '*': multiply, 
                '/': divide,
                }

    num1 = float(input("What is the first number?: "))

    symbols = '\n'.join(list(operations.keys()))

    while True:
        print(symbols)
        operator = input("Choose the operator: ")
        num2 = float(input("What is the second number?: "))
        answer = operations[operator](num1, num2)
        
        print(f"{num1} {operator} {num2} = {answer}")
        
        num1  = answer
         
        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation.: ") == 'n':
            clear()
            calculator()
        
        

calculator()