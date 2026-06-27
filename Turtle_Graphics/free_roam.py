import turtle as t

t.colormode(255)
kachwa=t.Turtle()
screen=t.Screen()
kachwa.speed("fastest")

def forward():
    kachwa.forward(10)


screen.listen()
screen.onkey(key="w",fun=forward)


screen.exitonclick()