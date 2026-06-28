import turtle as t
import random

t.colormode(255)
colors=['red','green','orange','yellow','blue','purple']


screen=t.Screen()
screen.setup(width=500,height=400)
bet=screen.textinput(title="Make your bet", prompt= "Which turtle will win the race?, Enter a color:")
race_on=False

all_turtle=[]


for turtle_index in range(0,6):
    new_turtle=t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=-150+turtle_index*60)    
    all_turtle.append(new_turtle)
    
if bet:
    race_on=True
    while race_on:
        for turtle in all_turtle:
            if turtle.xcor()>230:
                winner=turtle.pencolor()
                race_on=False
            else:
                dist=random.randint(0,10)
                turtle.forward(dist)
                

if bet==winner:
    screen.title("You win!")
else:
    screen.title(f"You lose! {winner} is the winner.")


screen.exitonclick()