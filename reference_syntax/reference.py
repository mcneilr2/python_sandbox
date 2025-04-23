# Python Syntax

# Variables
x = 5
y = "hello"

# Lists
my_list = [1, 2, 3]
my_list.append(4)

# Dicts
my_dict = {"a": 1, "b": 2}
my_dict["c"] = 3

# Loops
for i in range(5):
    print(i)

# Conditionals
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

########################################

# Python Functions and Classes Cheat Sheet

# Function
def greet(name="world"):
    return f"Hello, {name}!"

# Class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"

########################################

# Python File I/O Cheat Sheet

# Read file
with open("example.txt", "r") as f:
    contents = f.read()

# Write file
with open("example_out.txt", "w") as f:
    f.write("Hello, file!")

########################################

# Python Exception Handling Cheat Sheet

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
finally:
    print("This always runs.")

########################################

# Python List Comprehensions Cheat Sheet

# Square each number
squares = [x*x for x in range(10)]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]

# Dictionary comprehension
square_dict = {f"num_{x}": x * x for x in range(5)}
########################################
