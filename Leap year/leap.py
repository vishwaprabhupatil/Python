print("Leap year checker\n")
a=int(input("Enter the year\n"))
b=int(input("Enter a month: "))

def leap(a):
    if a%4==0:
        if a%100==0:
            if a%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
                
def days_in_month(month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap(a) and month==2:
        return 29
    return month_days[month-1]
days=days_in_month(b)
year=""
if leap(a):
    year="leap year"
else:
    year="not a leap year"
print(f"the given year is {year} and the given month has {days} days")

