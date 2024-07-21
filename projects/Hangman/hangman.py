import random
from art import stages, logo
from words import word_list
print(logo)

chosen_word = random.choice(word_list)
lives = 6
display = []
for c in chosen_word:
    display += "_"
end = False
print(f"{' '.join(display)}")
print(stages[lives])

while not end:
    guess = input("Guess a letter:\n").lower()
    for c in display:
      if guess == c:
        print(f"{guess} already guessed.")
        continue
    inWord = False
    for i in range(0, len(chosen_word)):
        c = chosen_word[i]
        if c == guess:
            display[i] = guess
            inWord = True
    
    print(f"{' '.join(display)}")
    
    if not inWord:
        print(f"{guess} is not in the word.")
        lives-=1

    if lives == 0:
        end = True
        print(f"You lose!\nThe word was {chosen_word}")
    
    if "_" not in display:
        end = True
        print("You win!")

    print(stages[lives])
    

