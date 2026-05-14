# Calculate net worth given assets and debts

# Define assests 
savings = 5000
car_value = 15000
other_assets = 2000

# Define debts
car_loan = 8000
credit_card = 1500
other_debts = 500

# Calculate totals 
total_assets = savings + car_value + other_assets
total_debts = car_loan + credit_card + other_debts
net_worth = total_assets - total_debts

# Display results 
print("Your total assets are " + str(total_assets))
print("Your total debts are " + str(total_debts))
print("Your net worth is " + str(net_worth))