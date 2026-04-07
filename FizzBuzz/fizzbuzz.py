# while counting from 1 to n, if the number is divisible by 3, print says fizz
# if the number is divisible by 5, the print says buzz
# and if the number is divisible by both, 3 and 5, then the print says fizzbuzz
count=[]
n=int(input("Enter the end of the count (n): "))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        count.append("fizzbuzz")
    elif i%3==0:
        count.append("fizz")
    elif i%5==0:
        count.append("buzz")
    else:
        count.append(i)
print(count)
        