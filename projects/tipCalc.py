print("Welcome to the Tip Calculator!")
bill = float(input("What was your total bill? $"))
tip = int(input("How much tip would you like to give? (10, 12, or 15) "))
people = int(input("How many people to split the bill? "))

bill *= (1+(tip/100))

print(f"Each person should pay: ${round(bill/people, 2)}")