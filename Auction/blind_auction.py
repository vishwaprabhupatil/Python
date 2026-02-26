import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def clear():
    os.system("cls")
    
def highest_bid(a):
    highest=0
    winner=""
    for bidder in a:
        amount=a[bidder]
        if amount>highest:
            highest=amount    
            winner=bidder
    print(f"{winner} has the highest bid of ${highest}")

auc={}

print("Welcome to secret auction program")
end=False
print(logo)
while end==False:
    name=input("What is your name?\n")
    bid=int(input("What's your bid?\n$"))
    auc[name]=bid
    yesno=input("Are there any other bidders?Type 'yes' or 'no'\n")
    if yesno=="no":
        end=True
        highest_bid(auc)
    elif yesno=="yes":
        clear()
        


    