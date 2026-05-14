# Convert Fahrenheit to Celsius
# Formula: C = (F - 32) * 5/9

# Get input from user
fahrenheit = float(input("Enter temperature in fahrenheit: "))

# Calculate Celsius
celsius = (fahrenheit - 32) * 5/9

# Display results 
print(f"{fahrenheit} degrees Fahrenheit is {format(celsius, '.2f')} degrees Celsius")