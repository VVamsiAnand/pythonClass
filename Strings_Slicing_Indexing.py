#11. Extract first and last characters

text = input("Enter a string: ")
print("First character:", text[0])
print("Last character:", text[-1])


#12. Print every second character

text = input("Enter a string: ")
print("Every second character:", text[::2])


#13. Check if a substring exists

text = input("Enter a string: ")
sub = input("Enter substring to check: ")

if sub in text:
    print("Substring found")
else:
    print("Substring not found")

    
#14. Find index of first and last occurrence

text = input("Enter a string: ")
ch = input("Enter character to find: ")

first = text.find(ch)
last = text.rfind(ch)

if first != -1:
    print("First occurrence at index:", first)
    print("Last occurrence at index:", last)
else:
    print("Character not found")
'''output
Enter a string: vamsi
First character: v
Last character: i
Enter a string: anand
Every second character: aad
Enter a string: college
Enter substring to check: ege
Substring found
Enter a string: nanna 
Enter character to find: n
First occurrence at index: 0
Last occurrence at index: 3'''

