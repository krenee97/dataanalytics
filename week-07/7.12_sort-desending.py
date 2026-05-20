# Kendra Tyler
# 5/19/2026

# sort_index() and rank()
# display results in desending

import pandas as pd

# Create DataFrame
df = pd.DataFrame({ 
    "Student": ["Amy", "Bob", "Cara", "Dan"]
    "Score": [88, 95, 79, 91]
}, index=[3, 1, 2, 0])

print("ORIGINAL DATAFRAME")
print(df)
print()

# -------------------------------------
# Sort