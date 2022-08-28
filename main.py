from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_resources = CoffeeMaker()
coffee_menu = Menu()
money = MoneyMachine()

latte = MenuItem("latte", 200, 150, 24, 2.5)
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
cappuccino = MenuItem("cappuccino", 250, 50, 24, 3)
game = True
while game:
    b = input("What do you like?" + coffee_menu.get_items())
    if b == "off":
        game = False
    elif b == "report":
        coffee_resources.report()
        money.report()
    elif b == "latte" or "espresso" or "cappuccino":
        c = coffee_menu.find_drink(b)
        if coffee_resources.is_resource_sufficient(c) and money.make_payment(c.cost):
            coffee_resources.make_coffee(c)
        else:
            game = False
