# lab5_task1.py

# Global variable
counter = 0


def show_local():
    # Local variable with the same name
    counter = 10
    print("Local counter:", counter)


show_local()

# Accessing the global variable
print("Global counter:", counter)


# Output:
# Local counter: 10
# Global counter: 0
#
# Explanation:
# The counter inside show_local() is a local variable.
# It exists only inside the function and does not change
# the global counter.
#
# The counter outside the function is the global variable.
# Therefore, the two values are different.

# lab5_task2.py

# Global variable
counter = 0


def increment_counter():
    global counter
    counter += 1


# Call the function 5 times
for i in range(5):
    increment_counter()
    print("Counter after call", i + 1, ":", counter)


# Output:
# Counter after call 1 : 1
# Counter after call 2 : 2
# Counter after call 3 : 3
# Counter after call 4 : 4
# Counter after call 5 : 5

# lab5_task3.py

counter = 10


# This function causes UnboundLocalError
def wrong_function():
    counter = counter + 1
    print(counter)


print("Calling wrong_function():")

try:
    wrong_function()
except UnboundLocalError as e:
    print("Error:", e)


# Fixed function using global keyword
def correct_function():
    global counter
    counter = counter + 1
    print("Counter after correction:", counter)


correct_function()


# Output:
# Calling wrong_function():
# Error: cannot access local variable 'counter' where it is not associated with a value
# Counter after correction: 11
#
# Explanation:
# Python treats counter inside wrong_function() as a local variable
# because it is assigned a value there.
# Therefore, Python tries to read the local counter before it has
# been assigned, resulting in UnboundLocalError.
#
# Using the global keyword tells Python to use the global counter.


# lab5_task4.py

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


# Create a counter
counter = make_counter()

# Call the returned function multiple times
print("First call:", counter())
print("Second call:", counter())
print("Third call:", counter())
print("Fourth call:", counter())
print("Fifth call:", counter())


# Output:
# First call: 1
# Second call: 2
# Third call: 3
# Fourth call: 4
# Fifth call: 5
#
# Explanation:
# count is a local variable of make_counter().
# The inner increment() function uses nonlocal to modify count.
# Even after make_counter() finishes, count is remembered by
# the returned inner function.
# This is called a closure.


# lab5_task5.py

# Global balance
balance = 1000


def deposit(amount):
    global balance
    balance += amount
    print("Amount deposited:", amount)
    print("Current balance:", balance)


def withdraw(amount):
    global balance

    if amount > balance:
        print("Insufficient funds!")
        print("Current balance:", balance)
    else:
        balance -= amount
        print("Amount withdrawn:", amount)
        print("Current balance:", balance)


def check_balance():
    print("Current balance:", balance)


# Menu-driven program
while True:
    print("\n===== BANK ACCOUNT MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)

    elif choice == "3":
        check_balance()

    elif choice == "4":
        print("Thank you for using the bank service.")
        break

    else:
        print("Invalid choice!")


# Output:
# ===== BANK ACCOUNT MENU =====
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 1
# Enter deposit amount: 500
# Amount deposited: 500.0
# Current balance: 1500.0
#
# ===== BANK ACCOUNT MENU =====
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 2
# Enter withdrawal amount: 300
# Amount withdrawn: 300.0
# Current balance: 1200.0
#
# ===== BANK ACCOUNT MENU =====
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 3
# Current balance: 1200.0
#
# ===== BANK ACCOUNT MENU =====
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 2
# Enter withdrawal amount: 1500
# Insufficient funds!
# Current balance: 1200.0
#
# ===== BANK ACCOUNT MENU =====
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 4
# Thank you for using the bank service.
