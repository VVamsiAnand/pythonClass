# Demonstrating Python's case sensitivity

Marks = 90
marks = 75

print("Marks =", Marks)
print("marks =", marks)
2value = 10      # Error: SyntaxError (invalid decimal literal)

value_2 = 20
print(value_2)

_hidden = 30
print(_hidden)

class = 40       # Error: SyntaxError (invalid syntax)

my-var = 50      # Error: SyntaxError (cannot assign to expression)

MyClass = 60
print(MyClass)

total$ = 70      # Error: SyntaxError (invalid syntax)
