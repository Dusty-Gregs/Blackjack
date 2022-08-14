from art import logo
import random

import os
clear = lambda: os.system('cls')
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

clear()

game_over = False

user_hand = []
global user_score
dealer_hand = []
global dealer_score


def deal(list,amount):
    """Adds random card from deck to list."""
    for _ in range(amount):
        list.append(random.choice(cards))

def over_limit(list,score):
    global user_score
    global dealer_score
    if score > 21:
        if 11 in list:
            list.remove(11)
            list.append(1)
            if score == user_score:
                user_score = sum(list)
            elif score == dealer_score:
                dealer_score = sum(list)

#sum not working for any additions to list
#add if over 21 and includes 11 statement
def dealer_hit(list):
    dealer_more = True
    global dealer_score
    global user_score
    if user_score <= 21 and dealer_score < user_score:
        while dealer_more:
            if dealer_score > 21:
                over_limit(dealer_hand,dealer_score)
                if dealer_score > 21:
                    dealer_more = False
                elif dealer_score >= 17:
                    dealer_more = False
                    dealer_score = sum(list)
                elif dealer_score < 17:
                    deal(list,1)
                    dealer_score = sum(list)
            elif dealer_score >= 17:
                dealer_more = False
                dealer_score = sum(list)
            elif dealer_score < 17:
                deal(list,1)
                dealer_score = sum(list)

def final_hand():
    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}")



play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while not game_over:
    if play_game == 'y':
        print(logo)
        deal(user_hand,2)
        deal(dealer_hand,2)
        user_score = sum(user_hand)
        dealer_score = sum(dealer_hand)
        user_more = True
        while user_more:
            if user_score == 21:
                user_more = False
                dealer_hit(dealer_hand)
                if dealer_score == 21:
                    game_over = True
                    final_hand()
                    print("Draw")
                else:
                    game_over = True
                    final_hand()
                    print("Win with a Blackjack!")
            elif user_score > 21:
                over_limit(user_hand,user_score)
                if user_score > 21:
                    user_more = False
                    game_over = True
                    final_hand()
                    print("You went over. You lose!")
            else:
                print(f"Your cards: {user_hand}, current_score: {user_score}")
                print("Computer's first card: "+str(dealer_hand[0]))
                additional_card = input("Type 'y' to get another card, type 'n' to pass: ")
                valid_input = False
                while not valid_input:
                    if additional_card == 'y':
                        valid_input = True
                    elif additional_card == 'n':
                        valid_input = True
                    else:
                        print("That is not a valid input.")
                        additional_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if additional_card == 'y':
                    deal(user_hand,1)
                    user_score = sum(user_hand)
                else:
                    user_more = False
                    dealer_hit(dealer_hand)
                    if user_score == dealer_score:
                        final_hand()
                        print("Draw")
                        game_over = True
                    elif dealer_score > 21:
                        final_hand()
                        print("You win!")
                        game_over = True
                    elif user_score > dealer_score:
                        final_hand()
                        print("You win!")
                        game_over = True
                    else:
                        final_hand()
                        print("You lose.")
                        game_over = True
    elif play_game == 'n':
        exit()
    else:
        print("That is not a valid input.")
        play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
