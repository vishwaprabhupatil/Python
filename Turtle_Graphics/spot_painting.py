import turtle as t
import random


# This part was used to generate the list 'colors'
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append((color.Rgb.r, color.Rgb.g, color.Rgb.b))
# print(rgb_colors)

t.colormode(255)
kachwa=t.Turtle()
screen=t.Screen()
kachwa.speed("fastest")
def pattern(x,y,space,colors):
    color_index=0
    for row in range(10):
        kachwa.penup()
        kachwa.goto(x, y + row * space)

        for dot in range(10):
            kachwa.dot(20, colors[color_index])
            color_index=(color_index+1)%len(colors)
            kachwa.forward(space)
colors=[(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
kachwa.penup()
kachwa.goto(-200, -200)
kachwa.pendown()

pattern(-200,-200,50,colors)
    

screen.exitonclick()