# Lambdas and generators - multiplier functions

# Doubler lambda
doubler = lambda n: n * 2
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

# Triple lambda
tripler = lambda n: n * 3
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

# Mutiplier function that creates lambds
def multiplier(x): 
    return lambda n: n * x

# Create multipler variables
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septuplar = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

# Test each one 
print(quadrupler(8))
print(quintupler(8))
print(sextupler(8))
print(septuplar(8))
print(octupler(8))
print(nonupler(8))
print(decupler(8))