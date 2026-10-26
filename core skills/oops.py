# Object Oriented Programming (OOP)

# 1. Class and Object
class Student:
    school_name = "ABC High School"  # Class variable

    def __init__(self, name, marks):
        self.name = name              # Instance variable
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}, School: {self.school_name}")

s1 = Student("Sai", 88)
s1.display()

# 2. Inheritance
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()

# 3. Encapsulation (Private variable)
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print("Current balance:", account.get_balance())
