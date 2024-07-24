from art import logo, vs
from game_data import data
import random
import os

print(logo)
def game():
    one = random.choice(data)
    two = random.choice(data)
    #ensure they're different
    while one == two:
        two = random.choice(data)

    print(f"Compare A: {one['name']}, a {one['description']}, from {one['country']}.")
    print(vs)
    print(f"Against B: {two['name']}, a {two['description']}, from {two['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if (guess == 'a' and one['follower_count']>two['follower_count']) or (guess == 'b' and two['follower_count']>one['follower_count']):
        return True
    else:
        return False

score = 0
while True:
    os.system("clear")
    print(logo)
    if score != 0:
        print(f"You're right! Current score: {score}.")
    outcome = game()
    if outcome == False:
        break
    score +=1

os.system("clear")
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")