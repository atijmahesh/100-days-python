import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if choice == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif choice == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
comp = random.randint(0, 2)
print("Computer choose:")
if comp == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif comp == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
if comp == choice:
    print("You tied!")
elif (comp == 0 and choice == 1) or (comp == 1 and choice == 2) or (comp == 2 and choice == 0):
    print("You win!")
else:
    print("You lose!")