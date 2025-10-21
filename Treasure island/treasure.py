print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
dir=input('You are at a cross road. Where do you want to go? Type "Left" or Right"\n')
a=dir.lower()
if a=="left":
    dec=input('You came at a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across the river\n')
    b=dec.lower()
    if b=="wait":
        col=input("You arrive at the island unharmed. There is a house with three door. One Red, One Yellow and One Blue. Which Colour do you choose?\n")
        c=col.lower()
        if c=="yellow":
            print("Congrats! You found the treasure")
        elif c=="red" or c=="blue":
            print("Your entered the room of beasts. Game Over!") 
    elif b=="swim":
        print("The water current was so fast that it drew you away. Game Over")
elif a=="right":
    print("Game Over. Sometimes, the road not taken is never supposed to be taken")
            
        
