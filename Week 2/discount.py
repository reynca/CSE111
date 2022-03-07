#Importing DateTime
from datetime import datetime
date = datetime.now()
day = date.weekday()

#Setting Subtotal Check and Discount Check
subtotal_check = False
discount = False

#Looping if value is 0
while subtotal_check == False:
    subtotal = float(input("\nWhat is the subtotal? "))
    if subtotal != 0:
            subtotal_check = True

while subtotal_check == True:
    if subtotal >= 50 and (day == 1 or day == 2):
        discount_amount = subtotal * 0.1
        subtotal = subtotal * 0.9
        discount = True
    elif subtotal < 50:
        print(f"I'm sorry, you will still need to buy ${50 - subtotal:1.2f}"
        + " more worth of products to get the discount")
    elif (day != 1 or day != 2):
        print("I'm sorry, but it is not a Tuesday or a Wednesday")

    #Setting End Variables
    tax = subtotal * 0.06
    total = subtotal + tax

    #Print Statements 
    print(f"\nTax Amount: ${tax:1.2f}")
    if discount == True:
        print(f"Discount Amount: ${discount_amount:1.2f}")
    print(f"Total: ${total:1.2f}\n")
    subtotal_check = False