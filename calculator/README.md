# Calculator

A command-line program that lets user perform basic calculation functions such as ' + ', ' - ', ' * ' and ' / '

## How it works

1. Program asks the user to type the first number.
2. Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
3. Program asks the user to type the second number.
4. Program works out the result based on the chosen mathematical operator.
5. Program asks if the user wants to continue working with the previous result.
6. If yes, program loops to use the previous result as the first number and then repeats the calculation process.
7. If no, program asks the user for the fist number again and wipes all memory of previous calculations.

## How to run it

1. Make sure Python 3 is installed
2. Open a terminal in this folder
3. Run:
```bash
   python task.py
```

## What I learned

- A return function can't be used multiple times within a function, unless it is indented by a loop function or an if/else
statement.
- Anything written after the return function is not taken into consideration by the code as it is an indicator for
code to exit the function.
- We learned about the functions with outputs ---> an output of one function can be used as input of another using return
function.
- We can use variables to store the values of the functions as well, but we need to be careful not to use parenthesis()
when doing this. This is because parenthesis is the trigger for calling the function to start.
- We also learned about recurrsion. It is way to keep a function running indefinetly. To do this, we call the function
once inside itself and once outside the function. Calling it outside triggers it and calling it inside keeps it running 
forever unless stopped forcefully.
- If we want to use functions with outputs to keep running forever by taking output of one as input of another, then we 
need to make sure the first input needs to be outside the while loop. Also, we need to define that the output of second 
function becomes the input of first function or vice versa within the while loop.

## Built with

- Python 3
- No external libraries (local `art.py` for the logo)

## Possible improvements

- If user inputs anything else except the defined operations within the dictionary then the code throws an error.
Can put a checker in the code so, anything else besides the dictionary keys input is not taken into
consideration
- We introduce a spacing of 20 lines each time the user wants to start calculating from the beginning to delude the user
that we have restarted the program. This needs to looked at in the future to improve user experience.
- We can introduce more complex mathematical operations in the future and increase the usability of the program.
