import turtle as t

t.colormode(255)
kachwa=t.Turtle()
screen=t.Screen()
kachwa.speed("fastest")

def forward():
    kachwa.forward(10)
def backward():
    kachwa.backward(10)
def left():
    kachwa.left(10)
def right():
    kachwa.right(10)
    
def clear():
    kachwa.home()
    kachwa.clear()

screen.listen()
screen.onkey(key="w",fun=forward)
screen.onkey(key="s",fun=backward)
screen.onkey(key="a",fun=left)
screen.onkey(key="d",fun=right)
screen.onkey(key="r",fun=clear)



screen.exitonclick()