# Rule of 72 - how long to double your savings 

# Define known values
current_savings = 5000
interest_rate = 6

# Calcualte years to double using rule of 72
years_to_double = 72 / interest_rate
future_value = current_savings * 2

# Display results 
print("Your current savings is " + str(current_savings))
print("At a " + format(interest_rate, ".0%") + "interest rate, ypur savings account will be woth " + format(float(future_value), ".2f") + "in" + format(years_to_double, ".1f") + " years")
