#15. Count the number of words

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))


#16. Find the longest word

sentence = input("Enter a sentence: ")
words = sentence.split()
longest = max(words, key=len)
print("Longest word:", longest)


#17. Reverse the order of words (not each word)

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_order = " ".join(words[::-1])
print("Reversed word order:", reversed_order)


#18. Capitalize first letter of every word (without .title())

sentence = input("Enter a sentence: ")
words = sentence.split()
capitalized = ""

for w in words:
    capitalized += w[0].upper() + w[1:].lower() + " "

print("Title Case:", capitalized.strip())


#19. Check if two strings are anagrams

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower()):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")



 '''output-
15)Enter a sentence: I love learning Python
Number of words: 4

16)Enter a sentence: Python programming is easy to learn
Longest word: programming

17)Enter a sentence: Python is used in AI
Reversed word order: AI in used is Python

18)Enter a sentence: python has many applications
Title Case: Python Has Many Applications

19)Enter first string: listen
Enter second string: silent
Strings are anagrams
'''



