from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    ans = ""
    if direction == "decode":
        shift*=-1
    for c in text:
        if c.isalpha() == False:
            ans += c
            continue
        idx = alphabet.index(c)
        idx+=shift
        if idx>25: 
            idx-=26
        ans += alphabet[idx]
    print(f"The {direction}d text is: {ans}")

print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift%=26
    caesar(text, shift, direction)
    repeat = input("Do you want to go again? (type yes or no)\n").lower()
    if repeat == "no":
        break