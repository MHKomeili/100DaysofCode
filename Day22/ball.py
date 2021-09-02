from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # def start_angle(self):
    #     random_angle = random.randint(135, 225)
    #     random_dir = random.randint(0, 1)
    #     self.setheading(random_dir * 180 + random_angle)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.x_bounce()
        self.goto(0, 0)
        self.move_speed = 0.1
