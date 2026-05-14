# Candy store exercise

# Two tuples - candy types and fruot flavors
candy_types = ("Chocolate", "gummy", "hard candy")
fruit_flavors = ("Strawberry", "watermelon", "mango")

# Create a set of candy combinations
candy_combos = set()
candy_combos .add((candy_types[0], fruit_flavors[0]))
candy_combos .add((candy_types[1], fruit_flavors[1]))
candy_combos .add((candy_types[2], fruit_flavors[2]))

# Pick one combination
todays_combo = (candy_types[0], fruit_flavors[1])

# Display results 
print("Todays candy options inculde:")
print(candy_combos)
