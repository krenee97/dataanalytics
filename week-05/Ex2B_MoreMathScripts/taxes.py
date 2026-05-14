# Calculate federal tax withheld from monthly salary
# Federal tax rate is 23%

# Get inout from user 
salary = float(input("What is your monthly salary?"))

# Calcualte tax
tax_rate = 0.23
tax_withheld = salary * tax_rate

# Display resluts
print(f"Yout monhtly salary is ${format(salary, '.2f')}")
print(f"Tax withheld at 23% is ${format(tax_withheld, '.2f')}")
