# Functional programming basics

# Pure function (no side effects, always returns same output for same input)
def add_tax(price):
    return price + (price * 0.18)

print("Tax price:", add_tax(100))

# Passing functions as arguments (Higher-order function)
def apply_operation(func, num):
    return func(num)

def square(n):
    return n * n

def double(n):
    return n * 2

print("Square:", apply_operation(square, 5))
print("Double:", apply_operation(double, 5))

# Using functools partial
from functools import partial

def power(base, exp):
    return base ** exp

square_func = partial(power, exp=2)
print("Square using partial:", square_func(7))
