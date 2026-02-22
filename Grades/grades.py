a=int(input("Number of students: "))
studants={}
grades={}
for i in range(a):
    b=input(f"Name of student {i+1}: ")
    c=float(input("Enter their marks: "))
    studants[b]=c
for key in studants:
    if studants[key]>90:
        grades[key]="A"
    elif studants[key]<90 and studants[key]>75:
        grades[key]="B"
    elif studants[key]<75 and studants[key]>65:
        grades[key]="C"
    elif studants[key]<65 and studants[key]>50:
        grades[key]="D"
    elif studants[key]<50 and studants[key]>35:
        grades[key]="E"
    else:
        grades[key]="F"
print(grades)
    
    
    