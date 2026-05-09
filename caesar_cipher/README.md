# Caesar Cipher

A command line Python program which takes input from user of what they would like to encode or decode and takes each
letter of the input and encrypts/decrypts them by a certain amount of letters.

## How it works

1. The program takes input from the user on whether they would like to encode or decode.
2. Then it takes the input of what message would the user like to encode/decode.
3. In case of encoding, user sets the amount of shifts each letter of the message will be shifted. For decoding, user
has to enter the correct shift amount which they could have set themselves or could have gotten from someone who encoded
the message.
4. Based on all the inputs, the output text is printed for the user to see. This continues until the user is done 
encoding/decoding.

## How to run it

1. Make sure Python 3 is installed
2. Open a terminal in this folder
3. Make sure the data files are present in the folder:
   - `task.py` (caesar_cipher)
   - `art.py` (logo)
4. Run:
```bash
python task.py
```

## Sample run
```
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88    
```
```
Type 'encode' to encrypt, type 'decode' to decrypt:

encode

Type your message:

Consistency is Key!

Type the shift number:

12

Your text is encoded and the result is: oazeuefqzok ue wqk!

Type 'yes' to continue encoding/decoding and 'no' to stop

yes

Type 'encode' to encrypt, type 'decode' to decrypt:

decode

Type your message:

oazeuefqzok ue wqk!

Type the shift number:

12

Your text is decoded and the result is: consistency is key!

Type 'yes' to continue encoding/decoding and 'no' to stop

no

Hope you enjoyed encryption and decryption! We'll see you again next time!
```

## Project structure
````
caesar_cipher/
├── task.py              # Encryption/Decryption logic
├── art.py               # Logo
└── README.md
````

## What I learned

1. If we try to shift letters by a position which makes the range go out of the range of the list, then we can use the
modulo (%) function to loop them back in the range of the list.
2. Variables defined inside a function live and die inside the function. We can't use them outside the function.
3. .index() function can be used to locate an item in the list.
4. If we have certain lines of code inside a function with some minor (2 or 3) differences, then we can avoid writing
the same line of codes again and again and tackle this using variables. This is also called Dry Refactoring (Don't Repeat Yourself).
5. Functions communicate with the outside world through their return values and not by assigning some value to an outer
variable.
6. Single Responsibility Principle - Each function should do one job and should do it really well! In our case, caesar()
should encode/decode, while the replay-prompt logic lives in the while loop, they're separate concerns.

## Built with

- Python 3
- Uses a local art.py module for the ASCII logo.

## Possible improvements

1. We are not encrypting symbols, spaces, and numbers. This can be tackled in the future.
2. In case, the user types anything except 'Yes' or 'No' when prompted if they would like to continue or stop, then
there is no fallback mechanism to let the user know they can only type 'Yes' or 'No'
3. We are lowering all letters inputed by the user and are ignoring any capitalization provided by the user for the
letters. This can be addressed in the future.
4. No input validation if user types something other than "encode"/"decode"
5. No input validation on the shift number — typing letters would crash with int()
