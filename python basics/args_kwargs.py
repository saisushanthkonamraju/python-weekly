# *args and **kwargs

# *args allows multiple positional arguments (passed as tuple)
def total_marks(*args):
    print("Args:", args)
    return sum(args)

print("Total:", total_marks(80, 90, 85))
print("Total:", total_marks(50, 60))

# **kwargs allows keyword arguments (passed as dictionary)
def print_student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_student_details(name="Sai", age=21, branch="CSE")

# Using both together
def student_info(roll_no, *subjects, **extra_info):
    print("Roll No:", roll_no)
    print("Subjects:", subjects)
    print("Extra Info:", extra_info)

student_info(101, "Python", "SQL", city="Hyderabad", grade="A")
