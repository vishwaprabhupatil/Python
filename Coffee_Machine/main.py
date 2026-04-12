from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


off=False

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
coffee_menu=Menu()


while not off:
    choice=input(f"What would you like? (espresso/latte/cappuccino):").lower()
    if choice=="off":
        off=True
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    elif choice=="add":
        coffee_maker.add()
    else:
        drink=coffee_menu.find_drink(choice)    
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        