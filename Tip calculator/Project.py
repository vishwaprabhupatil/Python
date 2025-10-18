print("Welcome to the tip calculator")
a=float(input("What was the total bill?\n$"))
b=int(input("What percentage tip would you like to give? 10, 12 or 15\n"))
c=int(input("How many people are splitting the bill?\n"))
total=a+(a*(b/100))
split=total/c
print(f"Each person should pay: ${split}")
