# Treasure Island

A text-based adventure game where the player navigates a series of branching 
choices to find hidden treasure — or meet an unfortunate end.

## How it works

The player is presented with three sequential decision points. Each choice 
either advances them deeper into the adventure or ends the game. Only one 
specific path of three correct choices leads to the treasure.

````
The decision tree:
Start
├── Left
│    ├── Swim   → Game Over (sharks)
│    └── Wait
│         ├── Red door    → Game Over (serial killer)
│         ├── Yellow door → You Win!
│         └── Blue door   → Game Over (flooded room)
└── Right       → Game Over (magma)
````
## How to run it

1. Make sure Python 3 is installed on your machine
2. Open a terminal in this folder
3. Run the script:
```bash
   python task.py
```
4. Follow the on-screen prompts and type your choices

## Sample run
Welcome to Treasure Island.

Your mission is to find the treasure.

You've arrived at a cross road. 
You have two options: Go Left or Go Right.

Type L for left or R for right: L

You've arrived at a lake...

Type swim to Swim across or type wait for a boat to arrive: wait

You have safely arrived on the island.

Please choose a door to enter Red, Yellow or Blue: yellow

Congratulations! You have found the treasure! You Won!

## What I learned

- Nested `if`/`elif`/`else` statements for branching logic
- Using `.lower()` to handle case-insensitive user input
- Multi-line strings with `\n` for cleaner output
- Raw string literals (`r'''...'''`) to print ASCII art with backslashes intact
- Designing a decision tree before writing conditional logic

## Built with

- Python 3
- No external libraries

## Possible improvements

- Replace nested `if`/`elif` blocks with a dictionary-based state machine
- Add input validation loops so wrong input re-prompts instead of ending the game
- Add a "play again" option using a `while` loop
- Add unit tests once I've learned `pytest`