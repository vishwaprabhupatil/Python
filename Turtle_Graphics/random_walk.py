import turtle as t
import random
kachwa=t.Turtle()
screen=t.Screen()
t.colormode(255)
kachwa.down()
screen.screensize(640,480)

dir=[0,90,180,270]
size=2
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)


kachwa.speed("fastest")
for _ in range(200):
    kachwa.pencolor(random_color())
    kachwa.forward(30)
    kachwa.setheading(random.choice(dir))
    kachwa.pensize(size)
    size+=0.1

screen.exitonclick()



















