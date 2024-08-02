from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
diff = input("Choose a difficulty ('easy' or 'hard): ").lower()
if diff == "hard":
    guesses = 5
else:
    guesses = 10
r = random.randint(1, 100)
while guesses>0:
    print(f"You have {guesses} attempts remaining to guess the number")
    ip = int(input("Make a guess: "))
    if ip == r:
        print(f"You got it! The answer was {ip}.")
        break
    elif ip < r:
        print("Too low.\nGuess again.")
    else:
        print("Too high.\nGuess again.")
    guesses -= 1
if guesses == 0:
    print("You've run out of guesses, you lose.")
