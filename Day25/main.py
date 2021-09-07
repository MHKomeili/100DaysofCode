import turtle
import pandas as pd
FONT = ("Courier", 10, "normal")


writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

screen = turtle.Screen()
screen.title("U.S States Quiz")
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What is another State's name? ").title()

    if guess == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        # missing_states = []
        # for s in states:
        #     if s not in guessed_states:
        #         missing_states.append(s)
        pd.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    if guess in states:
        x = int(data[data["state"] == guess].x)
        y = int(data[data["state"] == guess].y)
        writer.goto(x, y)
        writer.write(f"{guess}", align="center", font=FONT)
        guessed_states.append(guess)

screen.exitonclick()
