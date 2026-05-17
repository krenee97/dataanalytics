# Display the smallest and largest of three numbers

a = 10
b = 25
c = 17

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")
