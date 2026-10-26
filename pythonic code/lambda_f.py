# Lambda and f-strings

# 1. Sorting by custom key using lambda
items = [("Laptop", 75000), ("Mouse", 500), ("Keyboard", 2500)]
items.sort(key=lambda x: x[1])
print("Sorted by price:", items)

# 2. Useful f-string formatting
name = "Sai"
balance = 45000.758

# Decimal formatting
print(f"Account holder: {name}, Balance: Rs.{balance:.2f}")

# Width and alignment
print(f"{'User':<10} | {'Score':>5}")
print(f"{name:<10} | {95:>5}")

# 3. Walrus operator (:=)
text = "  python  "
if (cleaned := text.strip()):
    print("Cleaned string:", cleaned)
