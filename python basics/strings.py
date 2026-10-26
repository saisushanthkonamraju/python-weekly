# Strings practice

text = "Python Programming"

# Slicing and indexing
print(text[0])       # P
print(text[-1])      # g
print(text[0:6])     # Python
print(text[::-1])    # reverse string

# Common string methods
msg = "  hello world  "
print(msg.strip())        # removes extra spaces
print(text.upper())
print(text.lower())
print(text.title())
print(text.replace("Python", "Java"))

# Split and Join
sentence = "Python is easy to learn"
words = sentence.split(" ")
print(words)

joined = "-".join(words)
print(joined)

# Checking string properties
print(text.startswith("Py"))
print(text.endswith("ing"))
print("123".isdigit())

# f-string formatting
student = "Sai"
marks = 85
print(f"Student: {student}, Marks: {marks}")
