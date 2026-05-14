# Movie list execrise

movies = [
    "Belly",
    "Get Out",
    "Dont Be a Menace to South Central While Drinking your juice in the Hood",
    "Girls Trip",
    "Coming to America",
    "Friday"
]

# Step 3: print descriptive statement
print(f"The list movies inculdes my top {len(movies)} favortie movies")

# Step 4: print comelete list
print(movies)

# Step 4a: sorted() - does not change original list
print(sorted(movies))
print(movies)

# Step 4b: .sort() - changes the original list
movies.sort()
print(movies)
# Step 5: append a new movie
movies.append("Boomerang")
print(f"The list movies inculdes my top {len(movies)} favorite movies")
