# Functions in Python

# Simple function
def greet(name):
    print("Hello", name)

greet("Sai")
greet("Rahul")

# Function with return value
def add(a, b):
    return a + b

total = add(15, 25)
print("Total:", total)

# Default parameter
def welcome_user(name="Guest"):
    print(f"Welcome, {name}!")

welcome_user()
welcome_user("Sai")

# Returning multiple values
def calculate(a, b):
    return a + b, a * b

s, p = calculate(4, 5)
print("Sum:", s, "Product:", p)
