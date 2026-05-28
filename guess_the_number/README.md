# Guess the Number

A simplified version of the higher or lower game played by randomly selecting an integer between 1 and 100. You get
certain number of chances to make the guess based on the difficulty level you choose.

## How it works

1. The game starts by prompting the user to choose a difficulty level (easy/hard). For easy level of difficulty, you get
10 chances to make a guess, for hard the chances given are just 5.
2. We use random library to select any random integer between 1 and 100. The user is then told to make a guess.
3. If the user's guess is lower, the user is told that the guess is too low and similarly, user is told that the guess is
too high if the guess made by the user is higher than the chosen number
4. The user is prompted to keep going until they run out of chances to guess at which point they are told to try all over
again.

## How to run it

1. Make sure Python 3 is installed
2. Open a terminal in this folder
3. Make sure both files are present:
   - `task.py` (the game logic)
   - `art.py` (the ASCII logo)
4. Run:
```bash
   python task.py
```
5. Follow the on-screen prompts

## Sample run

```
 ▄████  ▄▄ ▄▄ ▄▄▄▄▄  ▄▄▄▄  ▄▄▄▄   ▄▄▄▄▄▄ ▄▄ ▄▄ ▄▄▄▄▄   ███  ██ ▄▄ ▄▄ ▄▄   ▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄  
██  ▄▄▄ ██ ██ ██▄▄  ███▄▄ ███▄▄     ██   ██▄██ ██▄▄    ██ ▀▄██ ██ ██ ██▀▄▀██ ██▄██ ██▄▄  ██▄█▄ 
 ▀███▀  ▀███▀ ██▄▄▄ ▄▄██▀ ▄▄██▀     ██   ██ ██ ██▄▄▄   ██   ██ ▀███▀ ██   ██ ██▄█▀ ██▄▄▄ ██ ██ 
```
```
Welcome to Guess the Number game!
Choose a difficulty level (easy/hard): hard
You chose hard level, you have 5 chances to guess the number.
I'm thinking of a number between 1 and 100!
Make a guess: 50
Your guess is too high.
Wrong guess! Make another attempt.Chances left: 4
Make a guess: 30
Your guess is too high.
Wrong guess! Make another attempt.Chances left: 3
Make a guess: 20
Your guess is too high.
Wrong guess! Make another attempt.Chances left: 2
Make a guess: 10
Your guess is too low.
Wrong guess! Make another attempt.Chances left: 1
Make a guess: 14
Your guess is too low.
You have run out of guesses! Try again!
```

## Project structure

```
guess_the_name/
├── task.py              # Game logic
├── art.py               # ASCII logo
└── README.md
```

## What I learned

1. Global constants that don't change values should be defined on the outermost indentation of the code.
2. Define functions that takes inputs needs to have those inputs defined with those names only that are mentioned when
defining them. Example - We used user_guess, actual_answer, and turns for  the check_guess() function and used same
terms inside that function. But when we call this function from within gameplay() function, we can use any other names
till we know what values are being inputted to the check_guess() function.
3. I don't need to use print functionality everytime, I can use return functionality with double quotes to get the same
result.

## Built with

- Python 3
- `random` (standard library)
- Local `art.py` module for the ASCII logo

## Possible improvements

- We can introduce other levels such as medium or legendary.
- Whenever the user is guessing a number, we are telling them if the number is too high or too low even though user
might be off by a couple of numbers only - we can introduce something like "Close! But still you need to go low/high"
type of instruction whenever user makes a wrong but a close guess.