# Python Operators

# Arithmetic
a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** 2)

# Comparison
print(a > b)
print(a == b)
print(a != b)

# Logical
has_license = True
has_car = False
print(has_license and has_car)
print(has_license or has_car)
print(not has_license)

# Assignment
score = 10
score += 5
score *= 2
print("Final score:", score)

# Membership (in, not in)
fruits = ["apple", "mango", "banana"]
print("mango" in fruits)
print("grapes" not in fruits)

# Ternary operator (one-line if)
status = "Adult" if a >= 18 else "Minor"
print("Status:", status)
