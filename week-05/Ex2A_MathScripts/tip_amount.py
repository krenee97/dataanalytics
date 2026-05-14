# Calculate tip amount on a resturant bill
# Uisng input() to get values from the user

# Get values from the user
bill_amount = float(input("What is your restaurant bill amount?"))
tip_percentage = float(input("What tip percentage do you want to leave? (enter as deciaml, e.g. 0.20 for 20%)"))

# Calculate the tip 
tip_amount = bill_amount * tip_percentage

# Old way:
#print("The tip on a $ " + str(bill_amount) + " resturant bill is $ " + format(tip_amount, ".2f"))

# New way usinf f-string:
print(f"The tip on a ${bill_amount} resturant bill is ${format(tip_amount, '.2f')}")

# Note: A pitfall of input() is that it always returns a string, so we must use float() to convert it to a number for math