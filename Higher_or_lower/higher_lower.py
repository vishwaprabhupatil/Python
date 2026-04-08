import random
from data import data
import art
import os

def clear():
    os.system("cls")


def highlow():
    A=random.randint(0,len(data)-1)
    score=0
    end=False
    while not end:
        
        B=random.randint(0,len(data)-1)
        print(art.highlow,"\n\n\n\n")
        print(f"Score: {score}")
        if A!=B:
            

            
            dataA=data[A]
            nameA=dataA["name"]
            workA=dataA["description"]
            followersA=dataA["follower_count"]
            countryA=dataA["country"]

            dataB=data[B]
            nameB=dataB["name"]
            workB=dataB["description"]
            followersB=dataB["follower_count"]
            countryB=dataB["country"]
            
            print(f"Compare A: {nameA}, {workA} from {countryA}\n\n")
            print(art.vs,"\n\n")
            print(f"Against B: {nameB}, {workB} from {countryB}\n\n")
            choice=input("Who has more followers? Type 'A' or 'B': ").lower()
            if choice=="a":
                if followersA>followersB:
                    score=score+1
                    clear()
                    print(f"You're right! Current score: {score}")
                    A=B
                    
                else:
                    print(f"Sorry, that's wrong. Final score: {score}")    
                    break
            elif choice=="b":
                if followersB>followersA:
                    score=score+1
                    clear()
                    print(f"You're right! Current score: {score}")
                    A=B
                else:
                    print(f"Sorry, that's wrong. Final score: {score}")    
                    end=True
                    break
            else:
                print("Invalid choice...Try Again")
                clear()
        else: 
            continue
            

highlow()



