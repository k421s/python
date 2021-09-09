#variables and comments were altered to make more sense in this language.


#Declare variables and assign variable Data
boxMeal 			= 12
deliveryFee		= 20
taxAmount 		= 0.06
budgetAmount	= 150
taxDisplay		= "6%"
numberPeople	= 0
subTotal			= 0
grandTotal		= 0


# Greet and ask user for the number of guests
# Input to numberPeople
numberPeople	= int(input("Hello, enter the number of guests attending.\n "))

# Calculate subtotal and grand total
subTotal			= numberPeople * boxMeal
grandTotal		= subTotal + (subTotal * taxAmount) + deliveryFee

# subtotal, tax, and grand total output
print("The catered amount before taxes is:",subTotal,"dollars.")
print("The tax amount is:", taxAmount)
print("The total catering cost plus tax and a $20 delivery fee is:",grandTotal)

# If statement tests if the grand total is over budget

if grandTotal > budgetAmount:
	print("Your budget is 150$, you are over budget.")