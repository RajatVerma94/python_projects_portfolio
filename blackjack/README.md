# Blackjack

A command-line implementation of a simplified Blackjack game where the player competes against the dealer to get as 
close to 21 as possible without busting.

## How it works

1. The player is dealt two random cards from the deck and shown their total.
2. The dealer is also dealt two cards, but only the first is revealed.
3. The player can choose to "hit" (draw another card) or "stand" (keep their current hand).
4. If the player's total exceeds 21, they bust and lose immediately - the dealer doesn't play.
5. If the player stands without busting, the dealer plays: drawing cards until their total reaches 17 or higher.
6. The two hands are compared:
   - If the dealer busts, the player wins.
   - If the totals are equal, it's a push (tie).
   - Otherwise, the higher hand wins.
7. After each round, the player is asked if they want to play again.

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

## Game rules implemented

- Cards: 2–10 are worth their face value; J, Q, K are worth 10; Ace is worth 11.
- The deck uses card values only (`[11, 2, 3, ..., 10, 10, 10, 10]`) - suits are not tracked.
- Dealer must draw cards until their total reaches 17 or higher (standard casino rule).
- Player bust ends the round immediately; the dealer does not play.

## Sample run

```
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/    
```
```
Are you ready to play a game of Blackjack? Press 'y' for yes or 'n' for no: y
Dealing cards...
Your Cards: [10, 6], current score: 16
Dealer first card is: 7
Type 'y' to Hit or type 'n' to Stand: y
Your cards: [10, 6, 4], current score: 20
Type 'y' to Hit or type 'n' to Stand: n
Your cards: [10, 6, 4], current score: 20
Dealer's cards: [7, 9, 2], current score: 18
You have a bigger hand. You Win!
Are you ready to play a game of Blackjack? Press 'y' for yes or 'n' for no: n
Alright! Come back when you are ready!
```

## Project structure

```
blackjack/
├── task.py              # Game logic
├── art.py               # ASCII logo
└── README.md
```

## What I learned

1. If you would like to randomly choose only few items from a list instead of just one, 
then use the function random.choices(list name, number of item to be added to an empty list. If you want
only one item then use random.choice
2. To add a card to the existing hand, you'd use .append() (one card) or .extend()
(multiple cards), not =. The = sign replaces the variable's content entirely. Whatever was in user_cards
before this line is gone. You're not adding to the hand, you're throwing the hand away and starting fresh each time.
3. The principle to internalize: when you have a loop that does setup work (drawing
cards), the result interpretation should happen after the loop is done, not during. Loops change state;
checks read state. Don't interleave them.

## Built with

- Python 3
- `random` (standard library)
- Local `art.py` module for the ASCII logo

## Possible improvements

- Use Ace = 1 as well for the option of drawing Ace and asking user to treat it as 1 or 11
- We prompt the user "are you ready to play?" each time, which sounds odd after they've already
played. A more natural phrasing would be "want to play another round?" but that's polish for later.
- Input validation for 'y'/'n' prompts - typing anything else currently behaves unexpectedly
- A persistent score counter across multiple rounds (e.g., "You've won 3, lost 2")
- A proper 52-card deck with suits and card depletion (currently it picks from the same pool every draw, which means a card can repeat infinitely)