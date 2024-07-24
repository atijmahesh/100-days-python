MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.0

def sufficient(item):
    ingrs = item["ingredients"]
    for ingr in ingrs:
        if ingrs[ingr] > resources[ingr]:
            print(f"Sorry there is not enough {ingr}.")
            return False
    return True

def dispense(choice):
    global money
    print("Please insert coins.")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickels?: "))
    p = int(input("How many pennies?: "))
    ip = 0.25*q + 0.1*d + 0.05*n + 0.01*p

    if ip < MENU[choice]["cost"]:
        print(f"Not enough money!")
    else:
        # increase money, reduce resources, output change
        money += MENU[choice]["cost"]
        for ingr in MENU[choice]["ingredients"]:
            resources[ingr] -= MENU[choice]["ingredients"][ingr]
        change = round(ip- MENU[choice]["cost"], 2)
        if change > 0:
            print(f"Here is ${change} in change.")
            print(f"Here is your {choice} ☕ Enjoy!")
    
    return True


while True:
    if not sufficient(MENU["espresso"]) and not sufficient(MENU["latte"]) and not sufficient(MENU["cappuccino"]):
        print(f"Machine's all out of resources. Thank you!")
        break
    choice = input("What would you like? (espresso/latte/cappuccino):\n")
    if choice == 'off':
        print("Thanks for using my coffee machine!")
        break
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif choice not in MENU:
        print(f"INVALID CHOICE. ")
        continue
    elif not sufficient(MENU[choice]):
        continue
    else:
        dispense(choice)