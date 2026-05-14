# Description: This script tests various numeric conversion techniques
# Author: Kendra Tyler

# Define variables
a = "101.1"
b = '55'
c = "402 Stevens"
d = 'Number 5'

# Transformation for variable a 
a_float = float(a) # works - converts string to float
a_int = int(float(a)) # works - convert to float first then int
print(a, type(a))
print(a_float, type(a_float))
print(a_int, type(a_int))

# Transformations for variable b
b_int = int(b) # works - converts string to int
b_float = float(b) # works - converts string to float
print(b, type(b))
print(b_int,type(b_int))

# Transformations for varibale c
# c_int = int(c) # error - ValueErroe: can't convert string with letters int
print(c, type(c))

# Transformation for variable d 
# d_int = int(d) # error - valueError: can't convert string letters to int
d_stripped = d.strip()
print(d, type(d))
print(d_stripped, type(d_stripped))