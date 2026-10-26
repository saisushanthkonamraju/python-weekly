# Regular expressions (pattern matching)

import re

sample_text = "My name is Sai, phone: 9876543210, email: sai123@gmail.com"

# 1. Searching for a pattern (re.search)
phone_match = re.search(r"\d{10}", sample_text)
if phone_match:
    print("Found phone number:", phone_match.group())

# 2. Extracting email address
email_match = re.search(r"[\w.-]+@[\w.-]+\.\w+", sample_text)
if email_match:
    print("Found email:", email_match.group())

# 3. Finding all numbers in a string (re.findall)
msg = "Order 25 apples and 10 bananas"
numbers = re.findall(r"\d+", msg)
print("All numbers found:", numbers)

# 4. Replace pattern (re.sub)
# Replace digits with *
hidden = re.sub(r"\d", "*", sample_text)
print("Masked text:", hidden)
