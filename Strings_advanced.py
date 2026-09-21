#20. Remove duplicate characters
text = input("Enter a string: ")
result = ""
for ch in text:
    if ch not in result:
        result += ch
print("Without duplicates:", result)


#21. Check if string is digits, alphabets, or alphanumeric
text = input("Enter a string: ")

if text.isdigit():
    print("Only digits")
elif text.isalpha():
    print("Only alphabets")
elif text.isalnum():
    print("Alphanumeric")
else:
    print("Contains other characters")

    
#22. Find duplicate characters and their counts
text = input("Enter a string: ")
duplicates = {}

for ch in text:
    if text.count(ch) > 1:
        duplicates[ch] = text.count(ch)

print("Duplicate characters and counts:", duplicates)


#23. Convert string to list and back
text = input("Enter a string: ")

# String to list
char_list = list(text)
print("List of characters:", char_list)

# List back to string
new_text = "".join(char_list)
print("Back to string:", new_text)


#24. Check if string is a valid identifier
text = input("Enter a string: ")

if text.isidentifier():
    print("Valid identifier")
else:
    print("Invalid identifier")

    
#25. Own version of find() and count()
text = input("Enter a string: ")
sub = input("Enter substring: ")

# Custom find
def my_find(s, sub):
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            return i
    return -1

# Custom count
def my_count(s, sub):
    count = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            count += 1
    return count

print("First occurrence index:", my_find(text, sub))
print("Total occurrences:", my_count(text, sub))




'''output-
20)Enter a string: python programming
Without duplicates: python rgami

21)Enter a string: Vamsi@321
Contains other characters

22)Enter a string: Difficult
Duplicate characters and counts: {'i': 2, 'f': 2}

23)Enter a string: Hello world!
List of characters: ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']
Back to string: Hello world!

24)Enter a string: 3vamsi
Invalid identifier

25)Enter a string: Glass Plate
Enter substring: Plate
First occurrence index: 6
Total occurrences: 1
'''
