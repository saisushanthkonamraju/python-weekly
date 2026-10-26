# Exception Handling

# 1. Basic try-except
try:
    num = 10 / 0
except ZeroDivisionError:
    print("You cannot divide a number by zero!")

# 2. Handling multiple errors
try:
    val = int("hello")
except ValueError as e:
    print("Conversion error:", e)

# 3. try - except - else - finally
try:
    a = 10
    b = 2
    res = a / b
except ZeroDivisionError:
    print("Division error")
else:
    print("Division successful, result is:", res)
finally:
    print("This finally block always executes.")

# 4. Raising custom exception
age = 15
if age < 18:
    try:
        raise ValueError("Age must be at least 18")
    except ValueError as err:
        print("Caught custom validation error:", err)
