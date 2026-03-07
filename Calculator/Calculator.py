import math
import os


art=logo = """
 _____________________
|  _________________  |
| |              0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1+n2 
def sub(n1, n2):
    return n1-n2

def mult(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def expo(n1,n2):
    return n1**n2

def sqr(n1,n2):
    return math.sqrt(n1)

def clear():
    os.system("cls")




def calculator():
    
    
    print(art, "\n\n\n")
    n1=float(input("Enter the first number: "))
        
    contuni=False
    while contuni==False:
            
        
        print("\n***Choose the operation***")
        print("Press 1 to Add\nPress 2 to Subtract\nPress 3 to Multipy\nPress 4 to Divide\nPress 5 to Raise to power(for root use '1/second number' while choosing the Second number)\nPress 6 for the square root of the first number")
        choice=input("\n")
        if choice!='6':
            n2=float(input("\nEnter the next number: "))

        operations={"1":add, "2":sub, "3":mult, "4":div, "5":expo, "6":sqr}
        symbol={"1":f"{n1} + {n2}", "2":f"{n1} - {n2}", "3":f"{n1} * {n2}", "4": f"{n1} / {n2}", "5":f"({n1})^({n2})", "6": f"√{n1}"}
        function=operations[choice]
        b=function(n1,n2)
        print(f"\n {symbol[choice]} = {b}")
        conti=input(f"Type 'y' to continue calculating with {b}, or 'n' to start a new calculation, or q to end.\n").lower()    
        if conti=='q':
            return conti
        
        if conti=='y':
            n1=b
        elif conti=='n':
            clear()
            calculator()
        else:
            return conti

 
x=calculator()

            
            
            





    





















