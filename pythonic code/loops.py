# Pythonic loops

names = ["Sai", "Rahul", "Arjun"]
marks = [85, 92, 78]

# 1. Direct iteration instead of range(len())
for name in names:
    print(name)

# 2. Iterating two lists together with zip
for name, mark in zip(names, marks):
    print(f"{name} -> {mark}")

# 3. Reversed iteration
for name in reversed(names):
    print("Reversed:", name)

# 4. any() and all() checks
scores = [65, 80, 95]
print("All passed (>40)?", all(s > 40 for s in scores))
print("Any top score (>90)?", any(s > 90 for s in scores))
