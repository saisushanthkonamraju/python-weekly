# Dictionaries (key-value pairs)

student = {
    "name": "Sai",
    "age": 21,
    "course": "Python"
}

# Accessing values
print(student["name"])
print(student.get("city", "Not Provided"))

# Adding and updating
student["marks"] = 92
student["age"] = 22
print(student)

# Removing a key
student.pop("course")

# Looping through a dictionary
for key, value in student.items():
    print(f"{key} -> {value}")

# Check if key exists
if "name" in student:
    print("Name is present in student record")
