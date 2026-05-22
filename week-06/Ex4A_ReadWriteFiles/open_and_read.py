# Practcing read/write - open and read a file 

f = open("about_me.txt", "r")

# Read the entire file
print(f.read())
f.close()

f = open("about_me.txt", "r")

# Read first 50 characters
print(f.read(50))
print(f.read(50))
f.close()

f = open("about_me.txt", "r")
# Read one line at a time
print(f.readline(10))
print(f.readline())
f.close()

f = open("about_me.txt", "r")
# Loop through lines
for i in range(1, 5):
    print(f.readline())
f.close()   

f = open("about_me.txt", "r")
# Read all lines as a list
print(f.readlines(1))
print(f.readlines(10))
print(f.readlines(100))
f.close()