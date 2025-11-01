row1=["🗺️","🗺️","🗺️"]
row2=["🗺️","🗺️","🗺️"]
row3=["🗺️","🗺️","🗺️"]
print(f"{row1}\n{row2}\n{row3}\n")
map=[row1,row2,row3]
pos=input("Enter the position where you'd want to keep your treasure(column x row):")
print("\n")
hor=int(pos[0])
ver=int(pos[1])
map[ver-1][hor-1]="X"
print(f"{row1}\n{row2}\n{row3}\n")




