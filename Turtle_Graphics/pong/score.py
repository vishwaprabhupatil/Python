from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.lscore=0
        self.rscore=0    
        self.goto(-150,200)
        self.write(arg=f"Score:{self.lscore}",move=False,align="center",font=("Comic Sans MS",40,"normal"))
        self.goto(150,200)
        self.write(arg=f"Score:{self.rscore}",move=False,align="center",font=("Comic Sans MS",40,"normal"))
        
        
        
    def incr_lscore(self):
        self.lscore+=1
        self.clear()
        self.goto(-150,200)
        self.write(arg=f"Score:{self.lscore}",move=False,align="center",font=("Comic Sans MS",40,"normal"))
        self.goto(150,200)
        self.write(arg=f"Score:{self.rscore}",move=False,align="center",font=("Comic Sans MS",40,"normal"))
        
        
    def incr_rscore(self):
        self.rscore+=1
        self.clear()
        self.goto(150,200)
        self.write(arg=f"Score:{self.rscore}",move=False,align="center",font=("Comic Sans MS",40,"normal"))
        self.goto(-150,200)
        self.write(arg=f"Score:{self.lscore}",move=False,align="center",font=("Comic Sans MS",40,"normal"))
        
        
    def end(self):
        
        self.write(arg=f"GAME ENDED",move=False,align="center",font=("Comic Sans MS",40,"normal"))
        
        