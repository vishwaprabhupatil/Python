import random
import os


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     

def clear():
    os.system("cls")
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
     
def compare(user_score, computer_score):
    if user_score==computer_score:
        return "Draw :>"
    elif computer_score==0:
        return "You Lost :( , Opponent has Blackjack"
    elif user_score==0:
        return "You Win with a Blackjack B)"
    elif user_score>21:
        return "Your score went over 21. You lose :("
    elif computer_score>21:
        return "Opponent's score went over 21. You win B)"
    elif user_score>computer_score:
        return "You win B)"
    else:
        return "You lose :("
    

user_card=[]
computer_card=[]


for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())


def Blackjack():
    end_game=False
    print(logo)
    while end_game==False:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"Your cards:{user_card}, Your Score:{user_score}")
        print(f"Computer's First Card: {computer_card[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            end_game=True
        else:
            pick_again=input("Type 'y' to get another card, type 'n' to pass: ")
            if pick_again=='y':
                user_card.append(deal_card())
            else:
                end_game=True
                
    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)
        
    print(f"Your final hand: {user_card}, Final Score: {user_score}")
    print(f"Computer's final hand: {computer_card}, Final Score: {computer_score}\n")    
    print(compare(user_score,computer_score))
    
while input("Do you want to play a game of Blackjack? Type 'y or 'n':")=='y':
    clear()
    Blackjack()
    
    
    