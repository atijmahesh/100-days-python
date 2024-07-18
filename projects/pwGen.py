import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
lets = int(input("How many letters would you like in your password?\n"))
syms = int(input("How many symbols would you like?\n"))
nums = int(input("How many numbers would you like?\n"))

total = lets+syms+nums
password  = ""
for i in range(0, total):
    choice = random.randint(0, 2)
    if (lets==0 and syms == 0) or choice == 0:
        #rand num
        r = random.randint(0, 9)
        password += numbers[r]
        nums-=1
    elif (lets==0 and nums == 0) or choice == 1:
        #rand sym
        r = random.randint(0, 8)
        password += symbols[r]
        syms-=1
    elif (syms==0 and nums==0) or choice == 2:
        #rand letter
        r = random.randint(0, 25)
        password += letters[r]
        lets-=1

print(f"Your password is: {password}")
    