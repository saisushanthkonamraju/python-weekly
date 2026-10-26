# Recursion (Function calling itself)

# 1. Countdown
def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(3)

# 2. Factorial: n! = n * (n-1)!
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# 3. Sum of list numbers
def list_sum(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + list_sum(numbers[1:])

print("Sum of list:", list_sum([10, 20, 30]))
