# Working with lists

fruits = ["apple", "banana", "mango"]

# Accessing items
print(fruits[0])
print(fruits[-1])

# Adding items
fruits.append("orange")
fruits.insert(1, "grapes")
print(fruits)

# Removing items
fruits.remove("banana")
popped_item = fruits.pop()
print("Popped:", popped_item)
print("Updated list:", fruits)

# Sorting and reversing
numbers = [45, 12, 89, 3, 27]
numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

# Useful list operations
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
