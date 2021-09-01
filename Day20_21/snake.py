from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0,0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].setposition(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_part = Turtle(shape="square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.segments.append(new_part)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
