# Hangman Game

A command line implementation of the classic Hangman word guessing game, 
where the player has 6 lives to guess letters and reveal a randomly chosen 
word before the hangman drawing is completed.

## How it works

1. The program loads a large dictionary of English words from a data file 
   and filters it down to game-suitable words (5–9 letters, alphabet only).
2. A random word is chosen and displayed as a row of underscores.
3. The player has 6 lives and guesses one letter at a time.
4. Correct guesses reveal the matching letters in the word. Wrong guesses 
   cost a life and progress the hangman ASCII drawing.
5. The game ends when the player either reveals the full word (win) or 
   runs out of lives (loss).

## How to run it

1. Make sure Python 3 is installed
2. Open a terminal in this folder
3. Make sure the data files are present in the folder:
   - `task.py` (the game)
   - `hangman_art.py` (logo and hangman stages)
   - `words_alpha.txt` (the word list)
4. Run:
```bash
   python task.py
```
5. Guess a letter when prompted

## Sample run
````
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    

````
Are you ready to play hangman?

You have 6 lives left.

Guess a letter: e

e _ _ _ _

Bingo! Correct guess!
````
  +---+
  |   |
      |
      |
      |
      |
=========
````
Guess a letter: z

e _ _ _ _
Wrong guess! Choose another letter. You have 5 lives left.
````
  +---+
  |   |
  O   |
      |
      |
      |
=========
````
You guessed the word eagle. Congratulations! You win!

## Project structure
````
hangman_game/
├── task.py              # Game logic
├── hangman_art.py       # Logo and hangman ASCII stages
├── words_alpha.txt      # Source word list (~370,000 words)
└── README.md
````
## What I learned

- Reading data from an external file using `with open()` and processing each 
  line into a list of clean strings.
- Using a list comprehension with a filter condition to narrow ~370,000 words 
  down to a game-suitable subset based on length and character type.
- Splitting a project across multiple files and importing specific names 
  with `from module import name`, which keeps the main game file focused 
  on game logic instead of being cluttered by data.
- It is very important to know where to place code, within the loop or outside. I learned this by placing the `lives -= 1` inside the for loop, and it cost me all my lives for just one wrong guess.
- Why `if/else` is safer than two separate `if` statements when two 
  outcomes should be mutually exclusive (correct vs. wrong guess).
- Learned that `continue` and `break` let you skip the next iteration and exit the loop respectively, but we should be careful using them as they ignore all the conditions set after them within the loop.

## Built with

- Python 3
- `random` (standard library)
- Word list sourced from the [dwyl/english-words](https://github.com/dwyl/english-words) 
  GitHub project

## Possible improvements

- Track a separate `guessed_letters` list (covering both correct and wrong 
  guesses) so the game can detect repeated guesses and warn the player 
  instead of penalizing them again.
- Refactor `correct_guesses` to avoid duplicate entries when the chosen 
  word contains repeated letters (e.g., guessing 'a' for "aardvark" 
  currently appends 'a' three times).
- Add input validation so multi-character or non-alphabetic guesses 
  re-prompt instead of being treated as wrong guesses.
- Add a "play again?" prompt at the end of each game so players can 
  start a new round without re-running the script.
- Refactor the linear script into functions (`load_words()`, 
  `display_word()`, `play_hangman()`) for better code organization.