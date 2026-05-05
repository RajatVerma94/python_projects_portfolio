import random

#Create an ASCII list of stages that needs to displayed to player to let them know how many lives are remaining.
from hangman_art import logo, stages

# Load words from the words_alpha.txt data file
with open("words_alpha.txt") as file:
    all_words = [line.strip() for line in file]

# Filter to game-suitable words: 5-9 letters, alphabet only
word_list = [word for word in all_words if 5 <= len(word) <= 9 and word.isalpha()]

#Use Random library to get a random word from words_alpha text file
print(logo)
print("Are you ready to play hangman?")

chosen_word = random.choice(word_list)

#Create a variable, everytime user guesses wrong, this gets deducted by 1 and user knows how many lives he has left
lives = 6
print(f"You have {lives} lives left.")

#Use a placeholder to replace each letter of the chosen word with a blank
placeholder = ""
for letter in chosen_word:
    placeholder += "_ "
print(placeholder)

#We will be using while loop to keep taking the input/guesses from the player and a variable to display every correct
#guess the player has made
game_over = False
#We need to create a list which keeps getting updated after every correct guess because if we don't then all the correct
#guesses will reset to zero after exiting the while loop
correct_guesses = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter + " "
            #This is where we update the list of correct guesses
            correct_guesses.append(letter)
        elif letter in correct_guesses:
            #We would need to update the display by comparing it to the list of correct guesses
            display += letter + " "
        else:
            display += "_ "
    print(display)

    #We need to deduct one life for each wrong guess inside the while loop and reset the lives value outside the loop
    if guess not in chosen_word:
        lives -= 1
        life_word = "life" if lives == 1 else "lives"
        print(f"Wrong guess! Choose another letter. You have {lives} {life_word} left.")
    else:
        print("Bingo! Correct guess!")

    # We need to print the hangman ASCII here to let the user feel the excitement/rush until the word is guessed
    print(stages[lives])

    #Here we set the conditions of when the game_over becomes true. If player has run out of lives or guessed the word
    if "_ " not in display:
        game_over = True
        print(f"You guessed the word {chosen_word}. Congratulations! You win!")

    elif lives == 0:
        game_over = True
        print(f"All lives are over. The word was {chosen_word}. You lose!")
