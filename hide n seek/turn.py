import random
print("Find out who is going to be a seeker in the game of Hide n Seek\n")
names=input("Enter the list of names who are playing hide n seek, in the form name1, name2, name3,....\n")
split=names.split(", ")
x=random.choice(split)
print(x,"is the seeker")



