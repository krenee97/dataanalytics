# If basics exercise

x = 100
y = 20

# a) If x divided by y is 5
if x / y == 5:
    x = 1
    print("x set correctly?")

# b) If x times y is less than y
if x * y < y:
    print("Whoops, x is less than the value of x")
else:
    print("uh on, x is not less than y")

# c) If x equals y
if x == y:
    print("now x times y equals x")
else:
    x = x + 10
    print("x is not equal to y, x is " + str(x))

# d) If x is greater than y
if x > y:
    print("now x is greater than y")
else:
    x = x * 2
    print("x is not greater than y")

# e) Final print
print(f"The final value of x is {x} and the final value of y is {y}")
