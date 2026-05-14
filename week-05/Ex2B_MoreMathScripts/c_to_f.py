# Convert Celsius to Farrenheit
# Formula: F = (C * 9/5) + 32

# Get input from user
celsius = float(input("Enter tempture in Celsius: "))

# Calculate Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display resluts 
print(f"{celsius} degrees Celsius is {format(fahrenheit, '.2f')} degrees fahrenheit")
