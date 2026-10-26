# For and While loops

# Simple for loop with range
for i in range(1, 6):
    print("Number:", i)

# Looping through a list
names = ["Sai", "Rahul", "Arjun"]
for name in names:
    print("Hello", name)

# While loop
count = 3
while count > 0:
    print("Count is:", count)
    count -= 1

# Break and Continue
for n in range(1, 10):
    if n == 3:
        continue  # skip 3
    if n == 6:
        break     # stop loop
    print(n)

# For-else example
nums = [2, 4, 6, 8]
target = 5

for x in nums:
    if x == target:
        print("Found!")
        break
else:
    print("Target not found in list")
