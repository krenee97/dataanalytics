# Calculate charter van rental for a tour group
import math

# Get input from user
tourists = int(input("How mant tourists are there?"))

# Define known values 
van_capacity = 15
van_cost = 250

# Calculate vans needed
vans_needed = math.ceil(tourists / van_capacity)

# Calculate total cost and cost per person
total_cost = vans_needed * van_cost
cost_per_person = total_cost / tourists

# Display resluts 
print(f"Number of vans needed: {vans_needed}")
print(f"Total cost to rent vans: ${format(total_cost, '.2f')}")
print(f'Cost per person: ${format(cost_per_person, '.2f')}')
