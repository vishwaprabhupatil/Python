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
game_image=[rock,paper,scissors]
a=int(input("What do you choose? Type 0 for Rock, 1 for Papers and 2 for scissors\n"))
print(f"Your choice:\n\n{game_image[a]}\n\n")
b=random.randint(0,2) 
print(f"Computer's choice:\n\n{game_image[b]}\n")
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
