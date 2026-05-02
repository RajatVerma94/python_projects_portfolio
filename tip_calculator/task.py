#Adding Welcome Message
print("Welcome to the tip calculator that helps you split bills and avoid any awkward conversations later!")

#Ask user for the total bill and the percentage of tip that user would like to give
bill = float(input("What was the total bill? $"))
tip_percentage = round(float(input("What percentage tip would you like to give? ")), 2)

#Ask user about the number of people to split the bill with
people = int(input("How many people to split the bill? "))

#Calculate total bill by adding the tip to the bill amount
total_bill = bill + bill * tip_percentage / 100
total_bill = round(total_bill, 2)
print(f"Your total bill including the tip is: ${total_bill}")

#Calculate each person's share
individual_bill = round(total_bill/people, 2)
print(f"Each person should pay: ${individual_bill}")
