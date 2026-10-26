# Working with CSV and JSON files

import csv
import json
import os

# --- CSV Example ---
csv_file = "students.csv"

# Writing to CSV
data = [
    ["Name", "Score", "City"],
    ["Sai", 92, "Hyderabad"],
    ["Ravi", 85, "Bangalore"]
]

with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Reading from CSV
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print("CSV Row:", row)


# --- JSON Example ---
json_file = "student.json"

student_data = {
    "name": "Sai",
    "age": 21,
    "skills": ["Python", "SQL", "Git"]
}

# Write JSON to file
with open(json_file, "w") as f:
    json.dump(student_data, f, indent=4)

# Read JSON from file
with open(json_file, "r") as f:
    loaded = json.load(f)
    print("Loaded JSON:", loaded["name"], loaded["skills"])

# Clean up files
for file in [csv_file, json_file]:
    if os.path.exists(file):
        os.remove(file)
