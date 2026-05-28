from random import randint
from art import logo

#Define how many chances you want the user to have for the respective difficulty level and make them a global constant
#as these are not supposed to change values no matter.
EASY_CHANCES = 10
HARD_CHANCES = 5

#Define a functionality of choosing a difficulty level, so that the program knows how many lives to give the user to
#make a guess and identify the number. In case user types anything else other than 'easy' or 'hard' then tell them so.
def difficulty():
    level = input("Choose a difficulty level (easy/hard): ").lower()
    if level == "easy":
        print(f"You chose {level} level, you have {EASY_CHANCES} chances to guess the number.")
        return EASY_CHANCES
    elif level == "hard":
        print(f"You chose {level} level, you have {HARD_CHANCES} chances to guess the number.")
        return HARD_CHANCES
    else:
        return "Invalid difficulty level. Choose either 'easy' or 'hard'!"

#Define a functionality that takes in the input of every guess given by the user and compares it with the actual answer
#chosen by the random functionality and then either deducts the chances of the user or prompt them when they have
#guessed correctly. We also keep track of the number of chances left here.
def check_guess(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Your guess is too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Your guess is too low.")
        return turns - 1
    else:
        print(f"Bingo! You have guessed the {actual_answer} number correctly.")

#Define the gameplay() functionality when prompts the user that teh game has begun and to make a guess and keep going
#until the user has correctly guessed the number or have run out of chances to make a guess.
def gameplay():
    print(logo)
    print("Welcome to Guess the Number game!")
    turns = difficulty()
    print("I'm thinking of a number between 1 and 100!")
    answer = randint(1, 100)

    guess = 0
    while guess != answer:
        guess = int(input("Make a guess: "))
        turns = check_guess(guess, answer, turns)
        if turns == 0:
            print(f"You have run out of guesses! Try again!")
            return
        elif guess != answer:
            print(f"Wrong guess! Make another attempt.Chances left: {turns}")

gameplay()
