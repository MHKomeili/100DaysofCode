from turtle import Turtle, Screen


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_right():
    current_heading = tim.heading()
    tim.setheading(current_heading - 5)


def turn_left():
    current_heading = tim.heading()
    tim.setheading(current_heading + 5)


def clear():
    tim.reset()


tim = Turtle()
scn = Screen()
scn.listen()
scn.onkey(key="w", fun=move_forward)
scn.onkey(key="s", fun=move_backward)
scn.onkey(key="a", fun=turn_left)
scn.onkey(key="d", fun=turn_right)
scn.onkey(key="c", fun=clear)
scn.exitonclick()
