from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0 
    if sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

def compare(user_score, comp_score):
    print(f"User score: {user_score}")
    print(f"Computer score: {comp_score}")
    if user_score == comp_score:
        return "It's a draw!"
    elif comp_score == 0 or user_score > 21:
        return "The computer won! You lost!"
    elif user_score == 0 or comp_score > 21:
        return "You won! The computer lost!"
    elif user_score > comp_score:
        return "You won! The computer lost!"
    else:
        return "The computer won! You lost!"

def blackjack_round():
    user_cards = []
    computer_cards = []
    game_end = False
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

    while not game_end:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)
        print(f"User cards: {user_cards}. User score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_end = True
        else:
            draw = input("Do you want to draw another card? Type 'y' or 'n': ")
            if draw == 'y':
                user_cards.append(deal_card())
            else:
                game_end = True

    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    comp_score = calculate_score(computer_cards)
    result = compare(user_score, comp_score)
    print(f"Computer's final hand: {computer_cards}. Computer's final score: {comp_score}")
    print(result)

def blackjack():
    print(logo)
    print("Welcome to blackjack!")
    while True:
        blackjack_round()
        again = input("Do you want to play again? Type 'y' or 'n': ")
        if again == 'n':
            break
        os.system("clear")
        print(logo)

blackjack()
