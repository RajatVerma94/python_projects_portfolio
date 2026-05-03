# PyPassword Generator

A beginner Python program that generates a randomized password based on 
how many letters, numbers, and symbols the user wants.

## How it works

1. The user is asked how many letters, symbols, and numbers their password should contain.
2. The program randomly picks that many characters from each category using `random.choice()`.
3. The chosen characters are combined into a single list and shuffled with `random.shuffle()` 
   so the categories aren't grouped together.
4. The shuffled list is joined into a single string and printed as the final password.

## How to run it

1. Make sure Python 3 is installed
2. Open a terminal in this folder
3. Run:
```bash
   python task.py
```
4. Enter the number of letters, symbols, and numbers when prompted

## Sample run

Welcome to the PyPassword Generator!

How many letters would you like in your password?

6

How many symbols would you like?

2

How many numbers would you like?

2

Your password is: K7!Bq2#mAt

## What I learned

- Using `random.choice()` to pick a single random item from a list, and using it inside 
  a loop to build up a collection of random items.
- The difference between in-place and returning functions: `random.shuffle()` modifies 
  the list directly and returns `None`. Assigning its result to a variable will overwrite 
  the variable with `None`, a bug I hit while building this.
- Why variable naming matters: reusing the same name for both a list and an individual 
  item caused an `AttributeError` because Python silently overwrote my list with a single string.
- Using `"".join(list)` to convert a list of characters into a single string, and choosing 
  the separator carefully (`","` vs `""`) based on what the output should look like.
- Separating *building* a value from *displaying* it: storing the final password in its 
  own variable made the code easier to read than embedding the join inside an f-string.

## Built with

- Python 3
- `random` (standard library)

## Possible improvements

- Add input validation so non-numeric, negative, or zero inputs re-prompt instead of crashing
- Reduce code duplication by writing a helper function that takes a character pool and a count
- Add a password strength indicator based on length and character variety
- Use the `pyperclip` library to copy the password directly to the user's clipboard