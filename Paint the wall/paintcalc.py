#logic: Assuming 5 sq.m of area takes 1 can of paint 
#number of cans= selected area/5sq.m
import math
def paintcalc(height,width,can1):
    can_num=math.ceil((height*width)/can1)
    print(f"You'll need {can_num} cans of paint")
h=float(input("Enter the height of the wall: "))
w=float(input("Enter the width of the wall: "))
c=5

paintcalc(height=h,width=w,can1=c)