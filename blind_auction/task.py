#Import logo from the ASCII art Python file and print it for better User Experience
from art import logo
print(logo)

#Print the welcome message and create an empty dictionary which will take all the names of the bidders as key and
#all the bids as values for the particular keys
print("Welcome to the secret auction program")
bids = {}

#Introduce a check so that the program keeps on taking more bidding values until everyone has bid
more_bids = True

#Keep running the while loop with input the names as keys and bids as values for our dictionary until no one has been left to bid
while more_bids:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    new_bid = input("Are there more people who would like to bid? (Yes/No): ").lower()
    if new_bid == "yes":
        print("\n" *20)
    else:
        more_bids = False

highest_bid = 0
winner = ""
for name in bids:
    if bids[name] > highest_bid:
        winner = name
        highest_bid = bids[name]

print(f"The winner is {winner} with a bid of ${highest_bid}")
