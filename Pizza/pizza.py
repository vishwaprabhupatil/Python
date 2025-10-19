print("Welcome to Pizza Deliveries\nSmall Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25\n")
print("Pepperoni for Small Pizza: +$2\nPepperoni for Medium or Large Pizza: +$3\n")
print("Extra cheese for any size pizza\n")
bill=0
a=input("What pizza size do you want? S,M or L\n")
b=input("Do you want pepperoni? Y or N\n")
c=input("Do you want extra cheese? Y or N\n")
if a=="S":
    bill=bill+15
elif a=="M":
     bill=bill+20
elif a=="L":
     bill=bill+25
if b=="Y":
    if a=="S":
        bill=bill+2
    else:
        bill=bill+3
if c=="Y":
    bill=bill+1
    print(f"Your Final Bill is ${bill}")
else:
    print(f"Your Final Bill is ${bill}")

    
                
        
        