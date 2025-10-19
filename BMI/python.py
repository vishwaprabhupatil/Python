print("BMI calculator\n")
a=input("Enter your Weight in kg\n")
b=input("Enter your height in metres\n")
c=float(a)
d=float(b)
e=c/(d**2)
result=(round(e, 2))
print(f"Your BMI is {result} kg/m\u00b2")
if result<18.5:
    print("You are underweight")
elif result<25:
    print("Your have a normal weight")
elif result<30:
    print("Your are overweight")
elif result<35:
    print("You are obese")
else:
    print("You are clinically obese")
    
   