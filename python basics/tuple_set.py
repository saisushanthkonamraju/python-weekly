# Tuples and Sets

# --- TUPLE (immutable, cannot be changed) ---
point = (10, 20)
student = ("Sai", 21, "Hyderabad")

print(student[0])
print(student[1:])

# Unpacking a tuple
name, age, city = student
print(name, "lives in", city)

# Tuple count and index
vals = (1, 2, 2, 3, 4)
print("Count of 2:", vals.count(2))
print("Index of 3:", vals.index(3))


# --- SET (stores only unique items) ---
my_set = {1, 2, 2, 3, 4, 4}
print("Set removes duplicates:", my_set)

my_set.add(5)
my_set.discard(2)
print("Modified set:", my_set)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
