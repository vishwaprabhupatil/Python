print("Welcome to the ride!")
price=0
a=int(input("Please enter your height in cms\n"))
if a>120:
    print("Your are allowed to ride the roller coaster\n")
    b=int(input("Please enter your age\n"))
    if b<12:
        price=price+5
        print(f"The ticker price for you is ${price}")
    elif b<18:
        price=price+7
        print(f"The ticket price for you is ${price}")
    elif b>=50:
        print("We are sorry! Your are not allowed in this roller coaster")
    else:
        price=price+12
        print(f"The ticket price for your is ${price}")
else:
    print("Please increase your height to ride this roller coaster")
if price!=0:
    c=input("Do you want a photo? Y or N\n")
    if c=="Y":
        price=price+3
        print(f"Your final bill is ${price}")
    elif c=="N":
        price=price+0
        print(f"Your final bill is ${price}")
    else:
        print("Please enter a valid option!")    
    d=input("Y or N\n")
    if d=="Y":
        price=price+3
        print(f"Your final bill is ${price}")
    elif d=="N":
        price=price+0
        print(f"Your final bill is ${price}")
      
        




