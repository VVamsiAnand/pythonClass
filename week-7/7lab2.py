# lab2_task1.py

def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)


# Calling using positional arguments
print("Using Positional Arguments:")
student_info("Asha", 101, "CSE")

# Calling using keyword arguments in a different order
print("\nUsing Keyword Arguments:")
student_info(branch="CSE", name="Asha", roll_no=101)

# Output:
# Using Positional Arguments:
# Name: Asha
# Roll No: 101
# Branch: CSE
#
# Using Keyword Arguments:
# Name: Asha
# Roll No: 101
# Branch: CSE

# lab2_task2.py

def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    total = price + tax
    final_price = total - discount
    return final_price


# (a) Only price
price1 = calculate_price(1000)
print("Price with default tax and discount:", price1)

# (b) Price and custom tax rate
price2 = calculate_price(1000, 10)
print("Price with custom tax:", price2)

# (c) All three arguments
price3 = calculate_price(1000, 10, 100)
print("Price with custom tax and discount:", price3)

# Output:
# Price with default tax and discount: 1180.0
# Price with custom tax: 1100.0
# Price with custom tax and discount: 1000.0


# lab2_task3.py

def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


# Test with 3 marks
total, average = total_marks(80, 75, 90)
print("For 3 marks:")
print("Total:", total)
print("Average:", average)

# Test with 5 marks
total, average = total_marks(80, 75, 90, 85, 95)
print("\nFor 5 marks:")
print("Total:", total)
print("Average:", average)

# Test with 1 mark
total, average = total_marks(88)
print("\nFor 1 mark:")
print("Total:", total)
print("Average:", average)

# Output:
# For 3 marks:
# Total: 245
# Average: 81.66666666666667
#
# For 5 marks:
# Total: 425
# Average: 85.0
#
# For 1 mark:
# Total: 88
# Average: 88.0


# lab2_task4.py

def build_profile(**details):
    print("---------- PROFILE CARD ----------")

    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

    print("----------------------------------")


# First profile
build_profile(
    name="Asha",
    age=20,
    city="Hyderabad",
    hobby="Reading"
)

# Second profile
print()
build_profile(
    name="Ravi",
    age=21,
    branch="CSE",
    city="Bangalore"
)

# Output:
# ---------- PROFILE CARD ----------
# Name: Asha
# Age: 20
# City: Hyderabad
# Hobby: Reading
# ----------------------------------
#
# ---------- PROFILE CARD ----------
# Name: Ravi
# Age: 21
# Branch: CSE
# City: Bangalore
# ----------------------------------


# lab2_task5.py

def order_summary(customer, *items, discount=0, **extra):
    print("========== ORDER SUMMARY ==========")

    # Customer name
    print("Customer:", customer)

    # Ordered items
    print("Items:")
    for item in items:
        print("-", item)

    # Discount
    print("Discount:", discount, "%")

    # Extra information
    print("Extra Information:")
    for key, value in extra.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")

    print("===================================")


# Calling with positional argument,
# variable-length arguments, keyword argument,
# and keyword variable-length arguments
order_summary(
    "Asha",
    "Laptop",
    "Wireless Mouse",
    "Keyboard",
    discount=10,
    delivery_address="Hyderabad",
    gift_wrap=True
)

# Output:
# ========== ORDER SUMMARY ==========
# Customer: Asha
# Items:
# - Laptop
# - Wireless Mouse
# - Keyboard
# Discount: 10 %
# Extra Information:
# Delivery address: Hyderabad
# Gift wrap: True
# ===================================

