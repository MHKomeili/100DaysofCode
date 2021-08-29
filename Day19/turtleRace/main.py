from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
_y = -75

for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=_y)
    turtles.append(new_turtle)
    _y += 30

if user_bet:
    is_race_on = True

score_board = []
while is_race_on:
    for turtle in list(set(turtles) - set(score_board)):
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() >= 250:
            score_board.append(turtle)
    if len(score_board) == 6:
        is_race_on = False

winner = score_board[0].pencolor()
if winner == user_bet:
    print(f"You've won, {winner} is the winner.")
else:
    print(f"You've lost, {winner} is the winner.")
screen.exitonclick()
