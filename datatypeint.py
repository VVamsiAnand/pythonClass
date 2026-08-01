

age = 18
current_year = 2026
birth_year = current_year - age
print("Type of age:", type(age))
print("Type of current_year:", type(current_year))
print("Type of birth_year:", type(birth_year))
print("Age in 2050:", 2050 - birth_year)

x = 17
y = 5
print("Integer Division:", x // y)
print("Modulus:", x % y)
print("Exponent:", x ** 2)


first = "Vamsi"
last = "Anand"

full_name = first + " " + last

print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Title Case:", full_name.title())
print("Length:", len(full_name))
print("First Character:", full_name[0])
print("Last Character:", full_name[-1])

print("First Name:", full_name[:full_name.index(" ")])


is_raining = True
has_umbrella = False

print("Type of is_raining:", type(is_raining))
print("Type of has_umbrella:", type(has_umbrella))

print("is_raining and has_umbrella:", is_raining and has_umbrella)
print("is_raining or has_umbrella:", is_raining or has_umbrella)
print("not is_raining:", not is_raining)

print("True + True =", True + True)
print("False * 5 =", False * 5)