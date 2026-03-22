import random
import os

number=random.randint(0,100)

def hard():
  
    attempts=5
    global number
    print(f"You chose the hard level. You have {attempts} attempts to guess")
    for i in range(attempts):
        guess=int(input("Enter your guess: "))
        
        if guess>number:
            attempts=attempts-1
            print(f"Too High...Try something lower\n(You have {attempts} attempt left)")
        elif guess<number:
            attempts=attempts-1
            print(f"Too low...Try something higher\n(You have {attempts} attempt left)")
        else:
            print(f"The number was {number}. YOU WON")
            return 0

def easy():
  
    attempts=10
    global number
    print(f"You chose the easy level. You have {attempts} attempts to guess")
    for i in range(attempts):
        guess=int(input("Enter your guess: "))
        
        if guess>number:
            attempts=attempts-1
            print(f"Too High...Try something lower\n(You have {attempts} attempt left)")
        elif guess<number:
            attempts=attempts-1
            print(f"Too low...Try something higher\n(You have {attempts} attempt left)")
        else:
            print(f"The number was {number}. YOU WON")
            return 0

end=False

while not end:
    level=input("Choose the level you want to play. 'easy' or 'hard': ")
    if level=='easy':
        easy()
    elif level=='hard':
        hard()
    else:
        print("You've chosen an invalid level")

    quit=input("Do you want to try again? 'y' or 'n': ")
    if quit=='y':
        end=False
    else:
        print("BYE")
        end=True

                
