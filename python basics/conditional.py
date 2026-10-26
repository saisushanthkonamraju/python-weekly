# If - else conditions

marks = 78

# Grading system
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Checking age with nested if
age = 20
has_voter_id = True

if age >= 18:
    if has_voter_id:
        print("Eligible to vote")
    else:
        print("Need voter ID to vote")
else:
    print("Not eligible to vote")

# Short hand if-else
result = "Pass" if marks >= 50 else "Fail"
print("Result:", result)
