from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
machine = MoneyMachine()
menu = Menu()
isOn = True

while isOn:
    choice = input(f"What would you like? {menu.get_items()}:\n")
    if choice == 'off':
        isOn = False
    elif choice == 'report':
        maker.report()
        machine.report()
    else:
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink) and machine.make_payment(drink.cost):
            maker.make_coffee(drink)
