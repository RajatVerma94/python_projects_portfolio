print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

#Welcome Message
print("Welcome to treasure_island.")
print("Your mission is to find the treasure.")

#Obstacle 1 -> Go left or right
print("You've arrived at a cross road. You have two options: Go Left or Go Right.")
choice_1 = input("Type L for left or R for right: ").lower()
if choice_1 == "l":
    print("You've arrived at a lake. You can see an island in the middle of the lake.\n"
          "You can either swim to find the treasure right now or you can wait for a boat to arrive")

    #Obstacle 2 -> boat or swim
    choice_2 = input("Type swim to Swim across or type wait for a boat to arrive: ").lower()
    if choice_2 == "swim":
        print("Oh No! You choose to swim but you are attacked by the sharks! Game Over!")
    elif choice_2 == "wait":
        print("You have safely arrived on the island.\n"
              "There is a house with 3 doors of different colors!")

        #Obstacle 3 -> red, yellow, or blue door
        choice_3 = input("Please choose a door to enter Red, Yellow or Blue: ").lower()
        if choice_3 == "red":
            print("Danger! You've encountered a serial killer! Game Over!")
        elif choice_3 == "yellow":
            print("Congratulations! You have found the treasure! You Won!")
        elif choice_3 == "blue":
            print("Boom! You've been trapped inside the room and it is getting flooded. You've drowned. Game Over!")
        else:
            print("Please choose a valid color! Red, Yellow, or Blue.")

    else:
        print("Please choose either swim or wait!")

elif choice_1 == "r":
    print("You've fallen in the magma. Game Over!")
else:
    print("Please enter a valid option.")
