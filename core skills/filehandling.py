# File handling practice

file_name = "notes.txt"

# 1. Writing to a file
with open(file_name, "w") as f:
    f.write("Line 1: Learning file handling\n")
    f.write("Line 2: Writing with python\n")

# 2. Appending new line
with open(file_name, "a") as f:
    f.write("Line 3: Appended extra line\n")

# 3. Reading full file
with open(file_name, "r") as f:
    content = f.read()
    print("File Content:\n", content)

# 4. Reading line by line
with open(file_name, "r") as f:
    for line in f:
        print("Reading:", line.strip())

# Clean up created file
import os
if os.path.exists(file_name):
    os.remove(file_name)
