from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.color("white")
        self.penup()
        
        
    def create_paddle(self,x,y):
        self.goto(x,y)
        self.setheading(90) 
    
    def up(self):
        self.setheading(90)
        self.forward(50)
    
    def down(self):
        self.setheading(90)
        self.backward(50)