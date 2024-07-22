from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")
auction_dict = {}
while True:
    name = input("What is your name?: ")
    price = int(input("What is your bid price? $"))
    auction_dict[name] = price
    ip = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if ip == "no":
        break
    os.system('clear')

os.system('clear')
maxUser = {}
maxBid = -1
for user in auction_dict:
    if auction_dict[user]>maxBid:
        maxBid = auction_dict[user]
        maxUser = user

print(f"The winner is {maxUser} with a bid of ${maxBid}.")
