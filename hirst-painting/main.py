import colorgram
import turtle as t
import random

# colors = colorgram.extract("image.jpg", 20)
# rgb_colors = []
# for color in colors:
#     new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176), (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50), (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73)]


tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.speed(8)
t.colormode(255)


def make_painting(rows, columns):
    tim.setposition(-200, -200)
    current_position = tim.pos()
    for row in range(rows):

        for column in range(columns):
            tim.dot(20, random.choice(color_list))
            tim.forward(50)

        new_position = (current_position[0], current_position[1] + 50)
        tim.setposition(new_position)
        current_position = new_position


make_painting(7, 7)


screen = t.Screen()
screen.exitonclick()
