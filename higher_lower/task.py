##higher_lower
#Import all external libraries required to execute the higher_lower game

import random
from art import *
from game_data import *

#Create a function that will display the two randomly selected options from the game_data list
def selection(previous_guess = None):
    #While selecting option_a at the starting, we want it to be random but if the user makes a correct guess, we want
    #that correct guess as option_a, for this we will introduce a variable called previous_guess which will be None at
    #the start

    if previous_guess is None:
        option_a = random.choice(data)
    else:
        option_a = previous_guess
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(vs)
    option_b = random.choice(data)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")
    return option_a, option_b
    #Here we want to return the values of option_a and option_b so that we can use them as input in the check_answer
    #function

#Create a function to check if the option chosen by the user is correct one or not and store the correct answer and
#user guess in a variable
def check_answer(a, b):
    #We first need to create a variable to store the correct answer
    user_guess = input("Who do you think have more followers on Instagram? Chose 'A' or 'B': ").lower()
    if a['follower_count'] > b['follower_count']:
        correct_answer = 'a'

    #We need to make sure of the edge case where the follower count of both options are same or just in case both the
    #options are the same. In such cases, we will assume that the user's guess is the correct one.
    elif a['follower_count'] == b['follower_count']:
        correct_answer = user_guess
    else:
        correct_answer = 'b'

    return correct_answer, user_guess

#Now, we need to check if the user choose the correct letter by checking it with the correct_answer variable. We will do
#this in the main game play function and this is why we want to get the values of correct answer and user guess as
#output from
def game_play():
    #We need to define a bool variable here to make sure the while loop keeps running until this variable changes.
    game_over = False

    #We need to set the score at 0 when the game starts. We are adding the functionality of score increasing by 1 after
    #each correct guess by the user
    score = 0

    #We need to set the value of previous guess as None for the option_a to be randomly selected at the start of the game.
    previous_guess = None
    while not game_over:
        print(logo)

        #Get back the value of option_a and option_b from selection() function and store it locally in this function
        #with the same variable names. Do the same with the check_answer() function.
        option_a, option_b = selection(previous_guess)
        correct_answer, user_guess = check_answer(option_a, option_b)
        if correct_answer == user_guess:
            score += 1
            print(f"You are right! Current score: {score}")
            print("\n" * 20)

            #Now, if the loop reaches till this point, this means user has guessed correctly, and thus we need to set
            #the previous guess value to the guess that user has made.
            if correct_answer == 'a':
                previous_guess = option_a
            else:
                previous_guess = option_b

        else:
            print(f"Oh No!! You are wrong! Final score: {score}")
            game_over = True

game_play()
