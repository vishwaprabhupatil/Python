print("Leap year checker\n")
a=int(input("Enter the year\n"))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("The given year is a leap year")
        else:
            print("The given year is not a leap year")
    else:
        print("The given year is a leap year")
else:
    print("The given year is not a leap year")
                