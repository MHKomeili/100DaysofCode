from turtle import Turtle
FONT = ("Courier", 24, "normal")
LEVEL_POSITION = (-200, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_POSITION)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=FONT)
