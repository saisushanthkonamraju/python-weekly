# Iterators and Enumerate

# Using iter() and next()
fruits = ["apple", "banana", "mango"]
it = iter(fruits)

print(next(it))
print(next(it))
print(next(it))

# Enumerate - loop with index
students = ["Sai", "Rahul", "Karthik"]

# Default index (starts from 0)
for index, name in enumerate(students):
    print(f"Index {index}: {name}")

# Custom start index (e.g. 1)
for roll_no, name in enumerate(students, start=1):
    print(f"Roll No {roll_no}: {name}")
