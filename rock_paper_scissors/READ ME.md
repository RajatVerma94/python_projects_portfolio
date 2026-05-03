# Rock Paper Scissors

A command-line implementation of the classic Rock Paper Scissors game where 
the player competes against a computer opponent that picks its move randomly.

## How it works

1. The user is prompted to choose Rock (0), Paper (1), or Scissors (2)
2. The computer generates a random choice using Python's `random` module
3. Both choices are displayed as ASCII art
4. The winner is determined by classic game rules:
   - Rock crushes Scissors
   - Scissors cuts Paper
   - Paper covers Rock
   - Same choice = draw

## How to run it

1. Make sure Python 3 is installed
2. Open a terminal in this folder
3. Run:
```bash
   python task.py
```
4. Enter `0`, `1`, or `2` when prompted

## What I learned

- Generating random integers with `random.randint()` to simulate computer choices
- Using multi-line strings (triple quotes) to store ASCII art as variables
- Mapping numeric inputs to game states using `if`/`elif` chains
- Comparing two variables to determine win/lose/draw outcomes
- That long `if`/`elif` chains for game logic become unwieldy fast — there's almost certainly a cleaner way using lists or dictionaries

## Built with

- Python 3
- `random` (standard library)

## Possible improvements

- Replace the long `if`/`elif` win-condition chain with a lookup using a list 
  of beats-relationships (e.g., `beats = {0: 2, 1: 0, 2: 1}`)
- Store the ASCII art shapes in a list indexed by choice number to avoid 
  repetitive `if`/`elif` blocks for displaying choices
- Add input validation so non-numeric or out-of-range input re-prompts 
  instead of crashing or producing wrong output
- Add a "best of 3" or "play again" loop using `while`
- Track and display a running score across rounds