# String cleaning exercise

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonta Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# Step 3: lowercase
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# Step 4: title case
print(name_1.title())
print(name_2.title())
print(name_3.title())

# Step 5: remove $ from salaries
print(salary_1.replace("$",""))
print(salary_2.replace("$",""))

# Step 6: chain replace and int
salary_1_int = int(salary_1.replace("$", "") . replace(",",""))
print(salary_1_int, type(salary_1_int))