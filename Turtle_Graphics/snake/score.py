from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(-10,275)
        self.color("white")
        self.write(arg=f"Score:{self.score}",move=False,align="center",font=("Arial",15,"normal"))   
    
    def show_score(self):
        self.score+=1
        self.clear()
        self.write(arg=f"Score:{self.score}",move=False,align="center",font=("Arial",15,"normal"))
        
    def end_score(self):
        self.clear()
        self.home()
        self.write(arg=f"GAME OVER!\n     Score:{self.score}",move=False,align="center",font=("Arial",30,"normal"))
        