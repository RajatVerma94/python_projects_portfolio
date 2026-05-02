##BMI Calculator
#Formula for BMI = Weight/(Height)^2, the unit for the same should me Kg/m^2

#Welcome Message
print("Welcome to the BMI Calculator")

#Ask for user's weight and height
weight = round(float(input("What is your weight in Kg? ")), 2)

height = round(float(input("What is your height in meters? ")), 2)

#calculate bmi and round it upto 2 decimal places
bmi = weight / height ** 2
bmi = round(bmi, 2)

#Output to user if they are underweight, normal weight, or overweight
if bmi < 18.5:
    print(f"Your BMI is {bmi}, You are Underweight")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi}, You are of Normal Weight")
else:
    print(f"Your BMI is {bmi}, You are Overweight")
