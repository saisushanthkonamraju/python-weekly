# Variables and Data Types

# Assigning values
name = "Sai"        # str
age = 22            # int
salary = 35000.50   # float
is_passed = True    # bool
result = None       # NoneType

print(name, age, salary, is_passed)

# Multiple assignment
x, y, z = 10, 20, 30
a = b = 100

# Type conversion (casting)
num = "50"
num = int(num)
print("Converted to int:", num, type(num))

pi_str = "3.14"
pi = float(pi_str)
print("Float value:", pi)

# Checking types
print(type(name))
print(isinstance(age, int))
