# Blind Auction

A command-line program that lets multiple people enter blind bids and 
announces the highest bidder at the end.

## How it works

1. Each person enters their name and bid amount.
2. The program asks if there's another bidder. If yes, it clears the 
   screen (so the next person can't see previous bids) and loops back.
3. When no more bidders remain, the program finds the highest bid and 
   announces the winner.

## How to run it

1. Make sure Python 3 is installed
2. Open a terminal in this folder
3. Run:
```bash
   python task.py
```

## What I learned

- To enter keys and values in a dictionary by asking the user to input values, we use dictionaries the same way as we 
used lists, by introducing an empty dictionary.
- To get the maximum value of the bid and the name of the bidder, we first introduced two empty/zero variables by the 
name of "highest_bid = 0" and 'winner = "" '. We then looped all the dictionary values in the for loop. The program went 
from one value to another and whichever value was higher was stored in these variables.
- `if bids[name][0]` didn't work because the program doesn't contain a nested list. As per what I was doing initially, 
it was trying to find a value in a list in a dictionary. 
- Clearing the terminal with print("\n" * 20)]. This adds 20 lines between two outputs and in User Interface, it can be 
interpreted as clearing the screen.
- To call a key or a value in a dictionary, we use:
```
dictionary = {
"key1" = "value1",
"key2" = "value2"
}
for key in dictionary:
    print(key)      ----> Prints the keys
    print(dictionary[key])      ----> Prints the values
```

## Built with

- Python 3
- No external libraries (local `art.py` for the logo)

## Possible improvements

- No handling for tie bids (if two people bid the same highest amount, only the first is announced as winner).
- No protection against negative bids - a single negative bid would produce a meaningless "winner is [blank] with $0" result.
- No input validation if a user types text instead of a number for their bid.
- No persistence. Once the program ends, all bids are lost.
