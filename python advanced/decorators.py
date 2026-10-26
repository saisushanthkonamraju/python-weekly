# Decorators practice

# 1. Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before calling the function...")
        func()
        print("After calling the function...")
    return wrapper

@my_decorator
def greet():
    print("Hello from greet function!")

greet()

# 2. Decorator that accepts arguments
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__} with inputs:", args)
        result = func(*args, **kwargs)
        print("Output:", result)
        return result
    return wrapper

@log_function
def multiply(x, y):
    return x * y

multiply(5, 6)
