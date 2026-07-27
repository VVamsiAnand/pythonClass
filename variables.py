name = "Vamsi"
age = 18
height = 5.8
student = True

print("Name =", name, type(name))
print("Age =", age, type(age))
print("Height =", height, type(height))
print("Student =", student, type(student))

# 2. Multiple Assignment

a, b, c = 10, 20, 30
print("\na =", a, "b =", b, "c =", c)

a = b = c = 100
print("a =", a, "b =", b, "c =", c)

# 3(a). Swapping using a Temporary Variable

x = 5
y = 10

print("\nBefore Swapping:", x, y)

temp = x
x = y
y = temp

print("After Swapping (Temporary):", x, y)

# 3(b). Swapping using Tuple Unpacking

x = 5
y = 10

x, y = y, x

print("After Swapping (Tuple):", x, y)

# 4. Dynamic Typing

value = 25
print("\nValue =", value, type(value))

value = "Python"
print("Value =", value, type(value))

# output
#Name = Vamsi <class 'str'>
#Age = 18 <class 'int'>
#Height = 5.8 <class 'float'>
#Student = True <class 'bool'>

#a = 10 b = 20 c = 30
#a = 100 b = 100 c = 100

#Before Swapping: 5 10
#After Swapping (Temporary): 10 5
#After Swapping (Tuple): 10 5

#Value = 25 <class 'int'>
#Value = Python <class 'str'>
