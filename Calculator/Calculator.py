print("Calculator\n")
num1=float(input("Enter the first number\n"))
num2=float(input("Enter the second number\n"))
print("Choose your operation from 1,2,3 or 4 where,\n1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n")
choice=int(input("Choose here "))
if choice==1:
    result=num1+num2
    print("result=",result)
elif choice==2:
    result=num1-num2
    print("result=",result)
elif choice==3:
    result=num1*num2
    print("result=",result)   
elif choice==4:
    if num2==0:
        print("Error!Division by zero is not defined")
    else:
        result=num1/num2
        print("result=",result)
else:
    print("Please choose an option between 1-4")
    
