from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20 , 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('orange')
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

