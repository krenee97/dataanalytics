# Working with exceptions - try/except blocks

# ValueError
try:
    int("hello")
except ValueError:
    print("ValueError: Oops, that value cannot be converted to an integer.")
else:
    print("No error occurred!")
finally:
    print("Let's try another one...")

# NameError
try:
    m = banana
except NameError:
    print("NameError: Oops, looks like you tried to assign an undefined object ro a variable")
else:
    print(m)
finally:
    print("Let's try another one...")

# TypeError
try:
    print("hello" + 5)
except TypeError:
    print("TypeError: Oops, you cannot add a string and an integer.")
else:
    print("No error occurred!")
finally:
    print("Let's try another one...")

#SyntaxError
try:
    eval("if if if")
except SyntaxError:
    print("SyntaxError: Oops,  your code has a syntax error.")
else:
    print("No error occurred!")
finally:
    print("Let's try another one...")
