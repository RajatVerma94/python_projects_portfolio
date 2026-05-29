# Higher Lower

A famous game of higher or lower, that lets you guess who has more Instagram following among the two given options.
You can make a streak by continuing to guess correctly. Let the streak begin!

## How it works

1. Game starts with giving the user/player two options "A and B" displaying their Name, description, and the
home country the option belongs to.
2. User has to one of the option which they feel have more Instagram followers. The Program compares the user guess
with the correct answer and gives the user a score of 1. If the user chooses the wrong 
answer then the games ends.
3. If the user choose the correct answer in step 2 then the correct answer from step 2 becomes the option A
and option B is randomly selected. Then the user is prompted to choose again.
4. This continues until the user chooses the wrong answer once. The Final score is displayed at the end.
5. Advised to play among a group of friends to see who can get the highest streak!

## How to run it

1. Make sure Python 3 is installed
2. Open a terminal in this folder
3. Make sure both files are present:
   - `task.py` (the game logic)
   - `art.py` (the ASCII logo)
   - `game_data.py` (the list of profiles)
4. Run:
```bash
   python task.py
```
5. Follow the on-screen prompts

## Sample run

```
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Real Madrid CF, a Football club, from Spain.

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: NBA, a Club Basketball Competition, from United States.
Who do you think have more followers on Instagram? Chose 'A' or 'B': a
You are right! Current score: 1

    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Real Madrid CF, a Football club, from Spain.

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Justin Timberlake, a Musician and actor, from United States.
Who do you think have more followers on Instagram? Chose 'A' or 'B': a
You are right! Current score: 2

    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Real Madrid CF, a Football club, from Spain.

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Kim Kardashian, a Reality TV personality and businesswoman, from United States.
Who do you think have more followers on Instagram? Chose 'A' or 'B': b
You are right! Current score: 3

    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Kim Kardashian, a Reality TV personality and businesswoman, from United States.

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Neymar, a Footballer, from Brasil.
Who do you think have more followers on Instagram? Chose 'A' or 'B': a
You are right! Current score: 4

    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Kim Kardashian, a Reality TV personality and businesswoman, from United States.

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Kevin Hart, a Comedian and actor, from United States.
Who do you think have more followers on Instagram? Chose 'A' or 'B': a
You are right! Current score: 5

    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Kim Kardashian, a Reality TV personality and businesswoman, from United States.

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: LeBron James, a Basketball player, from United States.
Who do you think have more followers on Instagram? Chose 'A' or 'B': a
You are right! Current score: 6

    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Kim Kardashian, a Reality TV personality and businesswoman, from United States.

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Dwayne Johnson, a Actor and professional wrestler, from United States.
Who do you think have more followers on Instagram? Chose 'A' or 'B': a
Oh No!! You are wrong! Final score: 6
```

## Project structure

```
guess_the_name/
├── task.py              # Game logic
├── art.py               # ASCII logo
├── game_data.py
└── README.md
```

## What I learned

1. When calling a dictionary nested within a list, you can store the directory you want in a variable using a random
function or some specific function. Then you can call it using variable_name['key name'] and you can output the
value associated with that key.
2. First hand experienced and applied the output of one function to another function.
3. Learned about the None functionality. We can set the input as None by assigning a variable 'None' value. This can 
later be changed to other values, based on the situation.
4. You can get the value of same variables using the return function, and then you can call the same function and assign
#those values to the same variables and use them in other function. Example:
```
def selection(previous_guess = None):
     ...
     ...
     return option_a, option_b
 .
 .
 option_a, option_b = selection(previous_guess)
```

## Built with

- Python 3
- `random` (standard library)
- Local `art.py` and `game_data.py` modules for the ASCII logo and the list of profiles to compare

## Possible improvements

- We are creating a space of 20 lines after each correct guess, although this seems like a new window has opened, but
still not good enough UX.
- We can show the count of Instagram followers to the user to confirm to them that we are not incorrectly marking them.
- We can create a list of bigger dictionary or directly import a data file from kaggle and also work with pandas.