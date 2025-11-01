import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

a=int(input("What do you choose? Type 0 for Rock, 1 for Papers and 2 for scissors\n"))
if a==0:
    print("Your choice:\n\n",rock,"\n\n")
elif a==1:
    print("Your choice:\n\n",paper,"\n\n") 
elif a==2:
    print("Yours choice:\n\n",scissors,"\n\n") 
print("Computer's choice:\n\n")
b=random.randint(0,2)
if b==0:
    print(rock)
elif b==1:
    print(paper) 
elif b==2:
    print(scissors) 
if a==0 and b==1:
    print("\n\nYou lose!")
elif a==0 and b==2:
    print("\n\nYou win!")
elif a==1 and b==0:
    print("\n\nYou win!")
elif a==1 and b==2:
    print("\n\nYou lose!")
elif a==2 and b==0:
    print("\n\nYou lose!")
elif a==2 and b==1:
    print("\n\nYou win!") 
elif a==b:
    print("It's a draw!")
