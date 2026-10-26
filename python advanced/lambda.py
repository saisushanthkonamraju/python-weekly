# Lambda (anonymous functions)

# Basic lambda: lambda arguments: expression
square = lambda x: x * x
print("Square of 4:", square(4))

add = lambda a, b: a + b
print("Sum:", add(10, 20))

# Lambda with if-else
check_num = lambda n: "Even" if n % 2 == 0 else "Odd"
print("7 is:", check_num(7))

# Sorting list of tuples using lambda
students = [("Sai", 85), ("Rahul", 92), ("Arjun", 78)]
students.sort(key=lambda s: s[1])
print("Sorted by marks:", students)
