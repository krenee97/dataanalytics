# Math and stats using math, statistics, and random modules

import math
import statistics
import random

# Sample data list
data = [15, 22, 8, 35, 14, 27, 19, 42, 11,33]

# Math Module
print(f"Square root of 144: {math.sqrt(144)}")
print(f"Pi: {math.pi}")
print(f"Ceiling of 4.2: {math.ceil(4.2)}")
print(f"Floor of 4.8: {math.floor(4.8)}")

# Statistics module
print(f"Mean: {statistics.mean(data)}")
print(f"Median: {statistics.median(data)}")
print(f"Mode: {statistics.mode(data)}")
print(f"Standard devation: {round(statistics.stdev(data), 2)}")

# Random module
print(f"Random number between 1-100: {random.randint(1,100)}")
print(f"Random choice from data: {random.choice(data)}")