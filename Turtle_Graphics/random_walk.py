from turtle import Turtle,Screen
import random
kachwa=Turtle()
screen=Screen()
kachwa.down()
screen.screensize(640,480)
colors=['green', 'blue', 'yellow', 'orange', 'cyan', 'black','purple',"red"]
dir=[0,90,180,270]
size=2
kachwa.speed("fastest")
for _ in range(200):
    kachwa.color(random.choice(colors))
    kachwa.forward(30)
    kachwa.setheading(random.choice(dir))
    kachwa.pensize(size)
    size+=0.1

screen.exitonclick()



















