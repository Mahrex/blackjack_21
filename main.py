import art
import random
import os

# All the cards! 
# Ace can be counted as '11' or '1' as per need
# There can be infinite number of drawings
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Creating a function that will return a random card from our cards list
def deal_card():
    return random.choice(cards)

# Creating a function that takes a list as an input and will return the sum of scores
def calculate_scores(cards):
    
    # Checking for a blackjack
    if len(cards) == 2: 
        if 11 in cards and 10 in cards:
            return 0 # Returning 0 --> BLACKJACK!
    
    # Checking for ace cases
    if 11 in cards and sum(cards) > 21:
        
        # Replacing 11 with 1 when score is greater than 21!
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# MAIN GAME LOGIC AND RULES
# Creating a compare method to decide who got the match!
def compare(user_score,dealer_score):
    
    # Checking for various cases
    if user_score == dealer_score:
        print('\nThis is a tie! Scores:- ')
        print(f"User hands: {user_score_to_print} with score: {user_score}")
        print(f"Dealer hands: {dealer_score_to_print} with score: {dealer_score}\n")
        
    elif user_score == 0:
        print('\nCongratulations! You won the game by BLACKJACK!')
        print(f"User hands: {user_score_to_print} with score: {user_score}")
        print(f"Dealer hands: {dealer_score_to_print} with score: {dealer_score}\n")
                
    elif dealer_score == 0:
        print('\nYou lose! Dealer won by blackjack')
        print(f"User hands: {user_score_to_print} with score: {user_score}")
        print(f"Dealer hands: {dealer_score_to_print} with score: {dealer_score}\n")
    
    elif user_score > 21:
        print('\nSorry! You lose as you went over!')
        print(f"User hands: {user_score_to_print} with score: {user_score}")
        print(f"Dealer hands: {dealer_score_to_print} with score: {dealer_score}\n")
        
    elif dealer_score > 21:
        print('\nCongratulation! You won the game as opponent went over!')
        print(f"User hands: {user_score_to_print} with score: {user_score}")
        print(f"Dealer hands: {dealer_score_to_print} with score: {dealer_score}\n")
    
    # Final checks (No other condition satisfies!)
    elif user_score > dealer_score:
            print('\nCongratulations! You won the game!')
            print(f"User hands: {user_score_to_print} with score: {user_score}")
            print(f"Dealer hands: {dealer_score_to_print} with score: {dealer_score}\n")
    else:
        print('\nSorry! You lose the game!')
        print(f"User hands: {user_score_to_print} with score: {user_score}")
        print(f"Dealer scores: {dealer_score_to_print} with score: {dealer_score}\n")
    
# GAME #
while True:

    # Printing the game & logo
    print('WELCOME TO THE GAME OF BLACKJACK')
    print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
    print(art.blackjack_logo)

    # Creating user's and dealer's hands (as a list)
    user_hands = [] # Player cards!
    dealer_hands = [] # Computer cards

    # Giving card (x 2) to both players
    for i in range(2):
        user_hands.append(deal_card())
        dealer_hands.append(deal_card())
        
    # Starting the main game
    game_on = True

    # Playing loop for the user
    while game_on:
        
        # User hands in string mode
        user_hands_in_str = [str(num) for num in user_hands]
        user_score_to_print = ', '.join(user_hands_in_str)
        # print(user_hands_in_str)
            
        # Scores
        user_scores = calculate_scores(user_hands)
        dealer_scores = calculate_scores(dealer_hands)

        # Showing cards to players! (2 --> User, 1 --> Dealer)
        print(f"Your cards are: {user_score_to_print} with current score: {user_scores}")
        print(f"Dealer's first card is {dealer_hands[0]}")

        # Checking for blackjacks
        if user_scores == 0 or dealer_scores == 0 or user_scores > 21:
            game_on = False
        else:
            # Asking user if they want to hit or stand
            draw_again = input('Do you want to hit or stand? (H/S): ')
            if draw_again[0].upper() == 'H':
                user_hands.append(deal_card())
            else:
                game_on = False
        
    # Playing loop for the dealer
    while dealer_scores != 0 and dealer_scores < 17: 
        dealer_hands.append(deal_card())
        dealer_scores = calculate_scores(dealer_hands)

    # Dealer hands in string mode
    dealer_hands_in_str = [str(num) for num in dealer_hands]
    dealer_score_to_print = ', '.join(dealer_hands_in_str)
    
    # Main rules and logic of the game!    
    compare(user_scores,dealer_scores)
    
    # Checking if want to play again
    play_again = input('Do you want to play again? (Y/N): ')
    
    if play_again.upper() == 'Y':
        os.system('cls')
        continue
    else:
        break