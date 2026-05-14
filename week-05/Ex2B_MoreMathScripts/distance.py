# Calculate distance between two coordinates
import math

# Get input from user
x1 = float(input("Enter x1:  "))
y1 = float(input("Enter y1:  "))
x2 = float(input("Enter x2:  "))
y2 = float(input("Enter y2:  "))

# Calcualte distance 
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display result
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {format(distance, '.2f')}")
