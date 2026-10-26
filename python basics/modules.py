# Working with modules

# Importing entire module
import math

print("Square root:", math.sqrt(49))
print("Factorial:", math.factorial(5))

# Importing specific functions
from random import randint, choice

print("Random number:", randint(1, 10))
print("Random pick:", choice(["apple", "banana", "mango"]))

# Using alias
import datetime as dt

today = dt.date.today()
print("Today's date is:", today)

# Only runs when executed directly
if __name__ == "__main__":
    print("Running modules.py directly")
