#6. Count occurrences of a specific character

text = input("Enter a string: ")
ch = input("Enter a character to count: ")
count = text.count(ch)
print(f"'{ch}' occurs {count} times")


#7. Remove all whitespace

text = input("Enter a string: ")
no_space = text.replace(" ", "")
print("String without spaces:", no_space)


#8. Replace all occurrences

text = input("Enter a string: ")
old = input("Enter character/word to replace: ")
new = input("Enter new character/word: ")
result = text.replace(old, new)
print("After replacement:", result)


#9. Concatenate two strings (without +)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Using join
concat = "".join([s1, s2])
print("Concatenated string:", concat)


#10. Swap case of each character

text = input("Enter a string: ")
swapped = ""

for ch in text:
    if ch.islower():
        swapped += ch.upper()
    elif ch.isupper():
        swapped += ch.lower()
    else:
        swapped += ch

print("Swapped case:", swapped)


'''output-
6)Enter a string: Hello world!
 Enter a character to count: l
 'l' occurs 3 times
 
7)Enter a string: GMR Institute of Technology
String without spaces: GMRInstituteofTechnology

8)Enter a string: HP laptop
Enter character/word to replace: HP
Enter new character/word: HP Victus
After replacement: HP Victus laptop

9)Enter first string: Python programming
Enter second string: section-D
Concatenated string: Python programmingsection-D

10)Enter a string: Vamsi
Swapped case: vAMSI
'''


