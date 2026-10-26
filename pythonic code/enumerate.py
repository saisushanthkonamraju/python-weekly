# enumerate and zip practice

fruits = ["apple", "banana", "mango"]
prices = [100, 40, 80]

# 1. Enumerate with index
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 2. Enumerate starting from 1
for rank, fruit in enumerate(fruits, start=1):
    print(f"{rank}. {fruit}")

# 3. Zip two lists into a dictionary
fruit_prices = dict(zip(fruits, prices))
print("Fruit price map:", fruit_prices)

# 4. Unzipping pairs
pairs = [(1, "a"), (2, "b"), (3, "c")]
nums, chars = zip(*pairs)
print("Numbers:", nums)
print("Chars:", chars)
