# map, filter, and reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# 1. map() - apply function to each element
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)

# 2. filter() - select elements that match condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)

names = ["Sai", "Sushanth", "Raj", "Priya"]
short_names = list(filter(lambda name: len(name) <= 3, names))
print("Short names:", short_names)

# 3. reduce() - combine all values into one
sum_all = reduce(lambda a, b: a + b, numbers)
print("Sum of all numbers:", sum_all)

product_all = reduce(lambda a, b: a * b, numbers)
print("Product:", product_all)
