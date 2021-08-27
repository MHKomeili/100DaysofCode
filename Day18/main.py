# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_colors)

from turtle import Turtle, Screen
import random

color_list = [(238, 251, 245), (250, 228, 15), (213, 12, 8), (199, 11, 36), (10, 98, 61), (5, 39, 32), (232, 228, 5),
              (64, 221, 157), (198, 68, 19), (32, 91, 189), (43, 212, 71), (235, 148, 38), (32, 30, 153),
              (242, 247, 251), (15, 22, 54), (67, 9, 49), (245, 38, 148), (14, 206, 222), (65, 203, 230), (62, 20, 10),
              (229, 164, 7), (226, 19, 111), (14, 154, 22), (246, 58, 14), (98, 75, 8), (248, 11, 9), (223, 140, 205),
              (66, 241, 160),
              ]

tim = Turtle()
scr = Screen()
scr.colormode(255)
tim.penup()
tim.hideturtle()
tim.setposition(-300, -300)
for i in range(10):
    tim.setposition(-300, tim.ycor() + 50)
    for j in range(10):
        tim.setx(tim.xcor() + 50)
        tim.dot(20, random.choice(color_list))


scr.exitonclick()