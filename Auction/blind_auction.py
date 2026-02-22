import os

def clear():
    os.system("cls")

auc={}
winner=[]
print("Welcome to secret auction program")
end=False

while end==False:
    name=input("What is your name?\n")
    bid=int(input("What's your bid?\n$"))
    auc[name]=bid
    yesno=input("Are there any other bidders?Type 'yes' or 'no'")
    if yesno=="no":
        end=True
    elif yesno=="yes":
        clear()

    