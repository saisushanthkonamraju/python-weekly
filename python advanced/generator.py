# Generators in Python

# Generator function uses yield
def count_up(n):
    for i in range(1, n + 1):
        yield i

# Using next() with generator
counter = count_up(3)
print(next(counter))
print(next(counter))
print(next(counter))

# Fibonacci generator
def fibonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

print("Fibonacci series:")
for num in fibonacci(6):
    print(num, end=" ")
print()

# Generator expression (memory efficient)
squares_gen = (x * x for x in range(1, 6))
print("Generator output:", list(squares_gen))
