##Welcome Message
print("Hello! Welcome to the world's best Roller Coaster ride!")

##Height Check
#Ask user for their height
height = int(input("Hi! Enter your height in centimeters: "))

if height < 120:
    print("We are Sorry! We can't let you get on this ride due to safety concerns!")
elif height >= 120:
##Age Check
#Ask user for their age
    age = int(input("Enter your age(in years): "))
    if age <= 18:
        print("You need to pay $7 to ride the roller coaster!")
    elif age > 18:
        print("You need to pay $12 to ride the roller coaster!")
    else:
        print("Please enter a valid age!")
else:
    print("Please enter a valid height!")
