import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

##Welcome Message
print("Welcome to the classic game of Rock Paper Scissors!\n"
      "Choose one of the following: Rock, Paper, Scissors.\n")

#Take input from user
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

#Display user's choice to user
if user_choice == 0:
    print(f"You chose {rock}")
elif user_choice == 1:
    print(f"You chose {paper}")
elif user_choice == 2:
    print(f"You chose {scissors}")
else:
    print("Please enter an integer between 0, 1, or 2")

#Take input from computer
computer_choice = random.randint(0,2)

#Display computer's choice to user
if computer_choice == 0:
    print(f"Computer chose {rock}")
elif computer_choice == 1:
    print(f"Computer chose {paper}")
else:
    print(f"Computer chose {scissors}")

if user_choice == computer_choice:
    print("The game is a draw!")
elif user_choice == 0 and computer_choice == 1:
    print("The paper triumphs rock! You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("The rock triumphs scissors! You win!")
elif user_choice == 1 and computer_choice == 0:
    print("The paper triumphs rock! You win!")
elif user_choice == 1 and computer_choice == 2:
    print("The scissors triumphs paper! You lose!")
elif user_choice == 2 and computer_choice == 0:
    print("The rock triumphs scissors! You lose!")
else:
    print("The scissors triumphs paper! You win!")
