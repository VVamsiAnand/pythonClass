

percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance (%): "))

eligible = percentage > 75 and attendance > 90

print("Eligible for Scholarship:", eligible)

# Sample Output:
# Enter percentage: 82
# Enter attendance (%): 95
# Eligible for Scholarship: True
#
# Enter percentage: 70
# Enter attendance (%): 92
# Eligible for Scholarship: False