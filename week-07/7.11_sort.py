# Kendra Tyler
# 5/19/2026

 # sort_index() and rank()

import pandas as pd

# create DataFrame
df = pd.DataFrame({
    "Student": ["Amy", "Bob", "Cara", "Dan"],
    "Score": [88, 95, 79, 91]
}, index = [3,1,2,0])

print("ORIGINAL DATAFRAME")
print(df)

# Sort by index
print("\nSORTED INDEX")
print(df.sort_index())

# Rank scores
df["Rank"] = df["Score"].rank(ascending=False)

print("\nWITH RANKINGS")
print(df)