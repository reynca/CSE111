import math
w = float(input("\nEnter the width of the tire in mm: "))
a = float(input("\nEnter the aspect ratio of the tire: "))
d = float(input("\nEnter the diameter of the wheel in inches: "))
v = (math.pi * (w ** 2) * a * (w * a + 2540 * d)) / 10000000000
print(f"\nThe approximate volume is {v:1.2f} liters\n")

from datetime import datetime
date = datetime.now()
day = date.weekday()
# print(f"{date:%m-%d-%Y}")

#Check to buy tires
question_check = False
while question_check == False:
    question = input("Would you like to Buy tires of this size?(Yes/No) ")
    question = question.upper()
    if question == "YES":
        user_phone_number = input("What is your phone Number? ")
        question_check = True
    elif question == "NO":
        question_check = True

# Open a text file named dimensions.txt in append mode.
with open("volumes.txt", "at") as volum_file:

    # Print a car's model and dimensions to the file.
    print(f"{date:%m-%d-%Y}", file=volum_file)
    print(f"Width: {w}\nAspect Ratio: {a}\nDiameter {d}", file=volum_file)
    print(f"The approximate volume is {v:1.2f} liters", file=volum_file)
    if question == "YES":
        print(f"User Phone Number: {user_phone_number}", file=volum_file)

print("***Thank you for using this program***")
