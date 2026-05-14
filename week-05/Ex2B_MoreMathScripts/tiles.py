# Calculate number of tile boxes needed for a room

import math

# Get input form user
length = float(input("What is the length of the room in feet? "))
width = float(input("What is the width of thr room in feet? "))

# Calculate tiles needed
total_tiles = length * width
boxes_needed = math.ceil(total_tiles / 12)

# Add 10% extra for breakage 
boxes_with_extra = math.ceil(boxes_needed * 1.10)

# Display results 
print(f"You need {boxes_needed} boxes of tiles")
print(f"With 10% extra for breakage, you should buy {boxes_with_extra} boxes")
