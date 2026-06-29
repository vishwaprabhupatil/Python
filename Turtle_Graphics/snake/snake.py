import turtle as t

UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake():
    def __init__(self):
        self.snakes=[]
        
        for square in range(0,3):
            kachwa=t.Turtle(shape="square",undobuffersize=20)
            kachwa.color("white")
            kachwa.penup()
            kachwa.goto(x=0-20*square,y=0)    
            self.snakes.append(kachwa)
        self.head=self.snakes[0]
            
    def move(self):
        for snake in range(len(self.snakes)-1,0,-1):
            newx=self.snakes[snake-1].xcor()
            newy=self.snakes[snake-1].ycor() 
            self.snakes[snake].goto(newx,newy)
        self.snakes[0].forward(10)
    
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
        
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
        
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)    