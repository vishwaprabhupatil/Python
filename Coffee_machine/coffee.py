MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 75,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 50,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



money=0


def report(resources):
    for i in resources:
        if i!="coffee":
            print(f"{i}:{resources[i]}ml")
        else:
            print(f"{i}:{resources[i]}g")
    print(f"Money:₹{money}")
        

def coins():
    print("Please insert coins")
    total=int(input("How many 1 rupee coins?:"))*1
    total+=int(input("How many 2 rupee coins?:"))*2
    total+=int(input("How many 5 rupee coins?:"))*5
    total+=int(input("How many 10 rupee coins?:"))*10
    total+=int(input("How many 20 rupee coins?:"))*20
    return total

def transaction(money_received,cost_of_drink):
    if money_received<cost_of_drink:
        print("Sorry that's not enough money. MONEY REFUNDED!!!")
        return False
    else:
        global money
        change=money_received-cost_of_drink
        money+=money_received-change
        print(f"Here is ₹{change} in change.")
        return True

def ingredients_enough(drink_ingredients):
    for i in drink_ingredients:
        if resources[i]<drink_ingredients[i]:
            print("Sorry! Not enough resources.")
            return False
    return True

def coffee(drink_name,ingredients):
    for item in ingredients:
        resources[item]-=ingredients[item]
    print(f"Here is your {drink_name}. Enjoy :)")
    
                
machine_off=False

while not machine_off:
    choice=input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice=="off":
        machine_off=True
    elif choice=="report":
        report(resources)
    else:
        drink=MENU[choice]
        if ingredients_enough(drink["ingredients"]):
            payment=coins()
            if transaction(payment,drink["cost"]):
                coffee(choice,drink["ingredients"])
            
            
            
            
             