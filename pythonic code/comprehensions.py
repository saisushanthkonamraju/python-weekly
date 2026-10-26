# Comprehensions practice

numbers = [1, 2, 3, 4, 5, 6]

# List comprehension: squares
squares = [n * n for n in numbers]
print("Squares:", squares)

# List comprehension with condition: even numbers
evens = [n for n in numbers if n % 2 == 0]
print("Evens:", evens)

# List comprehension with if-else
parity = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print("Parity:", parity)

# Dictionary comprehension
names = ["Sai", "Rahul", "Karthik"]
name_lengths = {name: len(name) for name in names}
print("Lengths dict:", name_lengths)

# Set comprehension
words = ["apple", "banana", "apple", "cherry"]
unique_lens = {len(w) for w in words}
print("Unique lengths:", unique_lens)
