print("Weclome to rollercoaster!")
height = int(input("What is your height in in? "))
if height >= 60:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age <= 12:
        print("Pay $5")
    elif age <= 18:
        print("Pay $10")
    elif age>=45 and age<=60:
        print("Midlife crises")
    else:
        print("Pay $50")
else:
    print("Sorry not allowed to ride :(")