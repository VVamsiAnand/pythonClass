#1. Length of a string

text = input("Enter a string: ")
print("Length of string:", len(text))


#2. Reverse a string

# Reverse without slicing
text = input("Enter a string: ")
rev = ""
for ch in text:
    rev = ch + rev
print("Reversed (loop):", rev)
# Reverse with slicing
print("Reversed (slicing):", text[::-1])


#3. Palindrome check

text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


#4. Uppercase and lowercase

text = input("Enter a string: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())


#5. Count vowels, consonants, digits, spaces

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
v_count = c_count = d_count = s_count = 0

for ch in text:
    if ch in vowels:
        v_count += 1
    elif ch.isalpha():
        c_count += 1
    elif ch.isdigit():
        d_count += 1
    elif ch.isspace():
        s_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
print("Digits:", d_count)
print("Spaces:", s_count)


'''output-
1)Enter a string: Hello world!
 Length of string: 12

2)Enter a string: GMR institute
 Reversed (loop): etutitsni RMG
 Reversed (slicing): etutitsni RMG
 
3)Enter a string: 12malayalam21
  Palindrome

4)Enter a string: Vamsi
 Uppercase: VAMSI
 Lowercase: vamsi

5)Enter a string: 1st prize winner
Vowels: 4
Consonants: 9
Digits: 1
Spaces: 2
'''
