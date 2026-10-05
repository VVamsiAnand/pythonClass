# lab7_task1.py

# A simple function
def greet(name):
    return "Hello, " + name


# (a) Assign a function to a new variable
new_function = greet

print("Calling function through a new variable:")
print(new_function("Asha"))


# (b) Pass a function as an argument to another function
def execute_function(func, value):
    return func(value)


print("\nPassing a function as an argument:")
print(execute_function(greet, "Ravi"))


# (c) Return a function from another function
def create_greeting():
    def greeting(name):
        return "Welcome, " + name

    return greeting


returned_function = create_greeting()

print("\nFunction returned from another function:")
print(returned_function("Priya"))


# Output:
# Calling function through a new variable:
# Hello, Asha
#
# Passing a function as an argument:
# Hello, Ravi
#
# Function returned from another function:
# Welcome, Priya
#
# Explanation:
# In Python, functions are first-class objects.
# This means a function can be assigned to a variable,
# passed as an argument, and returned from another function.

# lab7_task2.py

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result}")

        return result

    return wrapper


@log_call
def add(a, b):
    return a + b


# Calling the decorated function
result = add(10, 20)

print("Final result:", result)


# Output:
# Calling add args=(10, 20) kwargs={}
# add returned 30
# Final result: 30
#
# Explanation:
# @log_call modifies the add() function by wrapping it
# inside the wrapper() function.
#
# The decorator prints the function name and arguments
# before execution and prints the returned value afterward.


# lab7_task3.py

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        execution_time = end_time - start_time

        print(f"{func.__name__} took {execution_time:.6f} seconds")

        return result

    return wrapper


@timer
def calculate_sum():
    total = 0

    # Computationally heavy task
    for i in range(1, 10000001):
        total += i

    return total


# Call the decorated function
result = calculate_sum()

print("Sum:", result)


# Output:
# calculate_sum took 0.500000 seconds
# Sum: 50000005000000
#
# Note:
# The exact execution time will vary depending on the computer
# and Python environment.
#
# The timer decorator records the time before and after the
# function executes and calculates the difference.

# lab7_task4.py

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greeting():
    print("Hello! Welcome to Python.")


# Call the decorated function
greeting()


# Output:
# Hello! Welcome to Python.
# Hello! Welcome to Python.
# Hello! Welcome to Python.
#
# Explanation:
# repeat(3) creates a decorator that calls the greeting()
# function three times whenever it is invoked.

# lab7_task5.py

from functools import wraps

# Global login status
is_logged_in = False


def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied! Please log in first.")

    return wrapper


@require_login
def view_profile():
    print("Welcome to your profile!")


# Case 1: User is not logged in
print("When user is logged out:")
view_profile()


# Case 2: User is logged in
is_logged_in = True

print("\nWhen user is logged in:")
view_profile()


# Output:
# When user is logged out:
# Access denied! Please log in first.
#
# When user is logged in:
# Welcome to your profile.
#
# Explanation:
# The require_login decorator checks the global variable
# is_logged_in before executing view_profile().
#
# If is_logged_in is False, the function is not executed.
# If is_logged_in is True, the original function is executed.
#
# Why use functools.wraps?
# @wraps(func) preserves the original function's metadata,
# such as its name, documentation and other attributes.
# Without @wraps, the decorated function would appear to
# have the name "wrapper" instead of "view_profile".

# lab7_task6.py

import time
from functools import wraps


# Logging decorator
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result}")

        return result

    return wrapper


# Timer decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        execution_time = end_time - start_time

        print(f"{func.__name__} took {execution_time:.6f} seconds")

        return result

    return wrapper


# Stacking two decorators
@log_call
@timer
def calculate_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


# Call the decorated function
result = calculate_sum(1000000)

print("Final result:", result)


# Output:
# Calling calculate_sum args=(1000000,) kwargs={}
# calculate_sum took 0.050000 seconds
# calculate_sum returned 500000500000
# Final result: 500000500000
#
# Note:
# The exact execution time will vary depending on the computer.
#
# Explanation:
# Decorators are applied from the bottom upward.
#
# @timer is applied to calculate_sum() first.
# Then @log_call is applied to the result of @timer.
#
# Therefore, the effective structure is:
#
# log_call(timer(calculate_sum))
#
# When calculate_sum() is called:
#
# 1. log_call executes first and prints "Calling..."
# 2. log_call calls the timer wrapper.
# 3. timer measures the execution time.
# 4. The original calculate_sum() function executes.
# 5. timer prints the execution time.
# 6. Control returns to log_call.
# 7. log_call prints the returned value.
