#Import the art logo from art file but don't print it yet. We need to ask the user if they would like to play or not
from art import logo
import random

#Ask the user if they would like to play and if yes then continue with the play and if it's no then break from the loop
#and output a reply to come back again
should_play = True
while should_play:
    play = input("Are you ready to play a game of Blackjack? Press 'y' for yes or 'n' for no: ").lower()
    if play == 'y':
        print(logo)
        #Create a list of all cards
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        print("Dealing cards...")
        user_cards = random.choices(cards, k=2)  #This here indicates that you want two items in list as k=2

        print(f"Your Cards: {user_cards}, current score: {sum(user_cards)}")

        # Create an empty list of cards which will get appended with all the cards that lands in dealer's hand
        dealer_cards = random.choices(cards, k=2)
        print(f"Dealer first card is: {dealer_cards[0]}")

        #Define the rules of sum being equal to greater than 21 and also if it's less than 21 then the user could draw
        #more cards
        player_busted = False
        if sum(user_cards) == 21:
            print(f"Your Cards: {user_cards}, current score: {sum(user_cards)}\nBlackjack!")
        elif sum(user_cards) > 21:
            print(f"Your Cards: {user_cards}, current score: {sum(user_cards)}\nIt's a Bust! You lose")
            player_busted = True
        else:
            continue_draw = True
            while continue_draw:
                hit_or_stand = input("Type 'y' to Hit or type 'n' to Stand: ").lower()
                if hit_or_stand == 'y':
                    user_cards.append(random.choice(cards))
                    if sum(user_cards) > 21:
                        continue_draw = False
                        player_busted = True
                        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\nIt's a Bust! You lose")
                    elif sum(user_cards) == 21:
                        continue_draw = False
                        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\nBlackjack! You win!")
                    else:
                        continue_draw = True
                        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                else:
                    continue_draw = False

        if not player_busted:
        #Now we should reveal the dealer's second card and the sum. The rule that if the sum of dealer's card are less
        #than 17 then he/she should keep drawing should also come into play here.

            while sum(dealer_cards) < 17:
                dealer_cards.append(random.choice(cards))
            if sum(dealer_cards) > 21:
                print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\n"
                    f"Dealer's cards: {dealer_cards}, current score: {sum(dealer_cards)}\n"
                    f"It's a Bust! You Win")
            elif sum(dealer_cards) == sum(user_cards):
                print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\n"
                    f"Dealer's cards: {dealer_cards}, current score: {sum(dealer_cards)}\n"
                    f"It's a Push")
            elif sum(dealer_cards) > sum(user_cards):
                print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\n"
                    f"Dealer's cards: {dealer_cards}, current score: {sum(dealer_cards)}\n"
                    f"Dealer has a bigger hand. You lose!")
            else:
                print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\n"
                    f"Dealer's cards: {dealer_cards}, current score: {sum(dealer_cards)}\n"
                    f"You have a bigger hand. You Win!")

    else:
        should_play = False
        print("Alright! Come back when you are ready!")
