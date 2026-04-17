from turtle import Turtle,Screen

kachwa=Turtle()
kachwa.shape("triangle")
kachwa.color("red")
kachwa.down()
screen=Screen()
screen.screensize(1980,1080)

def draw_shape(sides):
    angle=360/sides
    for _ in range(sides):
        kachwa.forward(100)
        kachwa.left(angle)

colors=['green', 'blue', 'yellow', 'orange', 'cyan', 'black','purple',"red"]

for i in range(3,11):
    draw_shape(i)
    kachwa.color(colors[i-3])
    
    

    

        
kachwa.home()






screen.exitonclick()

