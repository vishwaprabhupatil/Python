import turtle as t
import random

kachwa=t.Turtle()
screen=t.Screen()
t.colormode(255)

kachwa.speed("fastest")
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)


for _ in range(72):
    kachwa.pencolor(random_color())   
    kachwa.circle(100)
    kachwa.left(5)
    
    
screen.exitonclick()