import re


# TASK 1 - Basic Pattern Matching
print("\n===== TASK 1 =====")

sentence = "1024 requests were served in 3 seconds"

# match() checks only the beginning of the string.
m1 = re.match(r"\d", sentence)

if m1:
    print("The sentence starts with a digit.")
else:
    print("The sentence does not start with a digit.")

# search() looks anywhere in the string.
m2 = re.search(r"served", sentence)

if m2:
    print("The word 'served' is found at:", m2.span())
else:
    print("'served' was not found.")

# fullmatch() checks the ENTIRE string.
m3 = re.fullmatch(r"\d+", "12345")
m4 = re.fullmatch(r"\d+", "123a5")

print("12345 contains only digits:", m3 is not None)
print("123a5 contains only digits:", m4 is not None)

# match() only checks the beginning.
# fullmatch() checks the complete string.
# Therefore, a string can start with digits and still fail fullmatch()
# if it contains other characters later.



# TASK 2 - Finding All Matches
print("\n===== TASK 2 =====")

paragraph = """
ISRO and DRDO are working together.
Python is a powerful programming language.
Students are learning computer science.
"""

# findall() finds all words written in capital letters.
capital_words = re.findall(r"\b[A-Z]{2,}\b", paragraph)

print("Capital words:", capital_words)

# finditer() finds words longer than 6 characters.
# \w+ means one or more word characters.
# {7,} means 7 or more characters.
print("\nWords longer than 6 characters:")

for match in re.finditer(r"\b\w{7,}\b", paragraph):
    print(match.group(), "starts at index", match.start())


# Given prices
prices = "apples: $3.50, bananas: $1.20, mango: $4.75"

# \d+ means digits.
# \.\d+ means decimal part.
# Together this finds amounts such as 3.50.
amounts = re.findall(r"\$\d+\.\d+", prices)

print("\nDollar amounts:", amounts)

# len() tells how many matches were found.
print("Number of prices:", len(amounts))



# TASK 3 - Search and Replace
print("\n===== TASK 3 =====")

# 3.1 Hide email addresses

text = """
Contact john@gmail.com or mary@yahoo.com
for more information.
"""

# This pattern finds email addresses.
# [\w.-]+ means letters/numbers/underscore/dot/hyphen.
# @ means the @ symbol.
# [\w.-]+ means the domain name.
# \.\w+ means .com, .org, etc.
hidden_emails = re.sub(
    r"[\w.-]+@[\w.-]+\.\w+",
    "[EMAIL HIDDEN]",
    text
)

print("Email hidden:")
print(hidden_emails)



# 3.2 Convert "Doe, John" to "John Doe"

name = "Doe, John"

# (\w+) captures the last name.
# (\w+) captures the first name.
# \2 means first name.
# \1 means last name.
new_name = re.sub(r"(\w+),\s*(\w+)", r"\2 \1", name)

print("Original name:", name)
print("New name:", new_name)



# 3.3 Double every number

sentence = "I have 3 apples and 5 oranges."


def double_number(match):
    # match.group() gives the number found.
    number = int(match.group())
    return str(number * 2)


doubled = re.sub(r"\d+", double_number, sentence)

print("Original:", sentence)
print("Doubled:", doubled)



# 3.4 Collapse repeated punctuation

punctuation_text = "Wait!!! What??? Really!!!"

# ([!?]) captures ! or ?
# \1 means the same punctuation character.
# + means one or more repetitions.
collapsed, count = re.subn(r"([!?])\1+", r"\1", punctuation_text)

print("Original:", punctuation_text)
print("After removing repeated punctuation:", collapsed)
print("Number of replacements:", count)



# TASK 4 - Building Patterns

print("\n===== TASK 4 =====")



# 4.1 Python variable name

# A valid variable:
# - starts with a letter or underscore
# - followed by letters, digits, or underscores
variable_pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"

variables = ["_count2", "2fast", "total_sum"]

for variable in variables:

    if re.fullmatch(variable_pattern, variable):
        print(variable, "is a valid variable name.")
    else:
        print(variable, "is NOT a valid variable name.")



# 4.2 Match cat, dog, or bird

pets = "I have a cat, a dog, and a bird. My friend also has a cat."

# | means OR.
# \b makes sure we match complete words.
pet_pattern = r"\b(cat|dog|bird)\b"

found_pets = re.findall(pet_pattern, pets)

print("\nPets found:", found_pets)



# 4.3 Hexadecimal color codes

# A hex color has:
# # followed by either 3 or 6 hexadecimal characters.
#
# [0-9A-Fa-f] = hexadecimal characters
# {3}|{6} = either 3 OR 6 characters
color_pattern = r"^#[0-9A-Fa-f]{3}([0-9A-Fa-f]{3})?$"

colors = ["#FFAA00", "#000", "#12G", "#12345"]

for color in colors:

    if re.fullmatch(color_pattern, color):
        print(color, "is a valid hex color.")
    else:
        print(color, "is NOT a valid hex color.")



# 4.4 Parse a log line using named groups

log_line = "2024-06-01 08:15:32 ERROR Disk full"

log_pattern = (
    r"(?P<date>\d{4}-\d{2}-\d{2}) "
    r"(?P<time>\d{2}:\d{2}:\d{2}) "
    r"(?P<level>\w+) "
    r"(?P<message>.*)")

match = re.search(log_pattern, log_line)

if match:
    print("\nDate:", match.group("date"))
    print("Time:", match.group("time"))
    print("Level:", match.group("level"))
    print("Message:", match.group("message"))


# TASK 5 - Practical Applications
print("\n===== TASK 5 =====")


# 5.1 Email Validator

def is_valid_email(s):

    # \w+ means one or more letters/numbers/underscore.
    # [\w.]+ allows dots also.
    # @ is required.
    # Domain must contain a dot.
    # {2,6} means TLD must have 2 to 6 letters.

    pattern = r"^[\w.]+@[\w.-]+\.[A-Za-z]{2,6}$"

    return re.fullmatch(pattern, s) is not None


valid_emails = [
    "john@gmail.com",
    "student123@yahoo.com",
    "abc.def@college.edu",
    "hello@python.org"
]

invalid_emails = [
    "a@b.c",
    "no-at-sign.com",
    "hello@gmail",
    "@gmail.com"
]

print("\nValid email tests:")

for email in valid_emails:
    print(email, "->", is_valid_email(email))

print("\nInvalid email tests:")

for email in invalid_emails:
    print(email, "->", is_valid_email(email))


# 5.2 Phone Number Extractor

phone_text = """
Call 555-123-4567 or (555) 123-4567.
You can also call 555.123.4567.
"""

# This pattern accepts:
# 555-123-4567
# (555) 123-4567
# 555.123.4567
phone_pattern = r"\(?(\d{3})\)?[-.\s]+(\d{3})[-.\s]+(\d{4})"

phone_numbers = re.findall(phone_pattern, phone_text)

print("\nPhone numbers:")

for phone in phone_numbers:

    # findall() with groups gives tuples.
    # Example: ('555', '123', '4567')
    normalized = "-".join(phone)

    print(normalized)


# 5.3 Date Extraction and Reformatting

date_text = """
My birthday is 15/08/2005.
The exam is on 20/09/2026.
Another date is 01/01/2027.
"""

# Find dates in DD/MM/YYYY format.
dates = re.findall(r"(\d{2})/(\d{2})/(\d{4})", date_text)

print("\nDates found:")

for date in dates:
    print(date)


# Convert DD/MM/YYYY to YYYY-MM-DD.
new_dates = re.sub(
    r"(\d{2})/(\d{2})/(\d{4})",
    r"\3-\2-\1",
    date_text
)

print("\nDates after reformatting:")
print(new_dates)


# 5.4 Whitespace and HTML Cleanup

def clean_text(html):

    # Remove HTML tags such as <b>, </b>, <p>, etc.
    text = re.sub(r"<[^>]+>", "", html)

    # Replace multiple spaces, tabs and newlines with one space.
    text = re.sub(r"\s+", " ", text)

    # Remove spaces from beginning and end.
    return text.strip()


html = """
<p>Hello   <b>Python</b></p>
<p>Welcome    to Python!</p>
"""

cleaned = clean_text(html)

print("\nCleaned text:")
print(cleaned)


# 5.5 Password Strength Checker

def check_password(pw):

    failed_rules = []

    # Check minimum length.
    if len(pw) < 8:
        failed_rules.append("Password must contain at least 8 characters.")

    # Check uppercase letter.
    if not re.search(r"[A-Z]", pw):
        failed_rules.append("Password must contain an uppercase letter.")

    # Check lowercase letter.
    if not re.search(r"[a-z]", pw):
        failed_rules.append("Password must contain a lowercase letter.")

    # Check digit.
    if not re.search(r"\d", pw):
        failed_rules.append("Password must contain a digit.")

    # Check special symbol.
    if not re.search(r"[!@#$%^&*]", pw):
        failed_rules.append(
            "Password must contain a symbol from !@#$%^&*."
        )

    return failed_rules


passwords = [
    "Python@123",
    "hello",
    "Python123",
    "PASSWORD@123"
]

print("\nPassword tests:")

for password in passwords:

    errors = check_password(password)

    if len(errors) == 0:
        print(password, "-> Strong password")
    else:
        print(password, "-> Failed rules:")
        for error in errors:
            print("  -", error)
            


# TASK 6 - Challenge: Mini Log Parser

print("\n===== TASK 6 =====")


log = """
[2024-06-01 08:15:32] ERROR user=jsmith msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO user=agarcia msg="Login successful"
[2024-06-01 08:17:44] WARN user=jsmith msg="High memory usage"
"""


# Named groups:
# timestamp -> date and time
# level     -> ERROR / INFO / WARN
# user      -> username
# msg       -> message inside quotes
log_pattern = (
    r"\[(?P<timestamp>\d{4}-\d{2}-\d{2} "
    r"\d{2}:\d{2}:\d{2})\]\s+"
    r"(?P<level>\w+)\s+"
    r"user=(?P<user>\w+)\s+"
    r'msg="(?P<msg>[^"]*)"'
)


# Store all log entries in a list.
entries = []

for match in re.finditer(log_pattern, log):

    # groupdict() converts named groups into a dictionary.
    entry = match.groupdict()

    entries.append(entry)


print("\nParsed log entries:")

for entry in entries:
    print(entry)


# Count ERROR, WARN and INFO

error_count = 0
warn_count = 0
info_count = 0

for entry in entries:

    if entry["level"] == "ERROR":
        error_count += 1





'''===== TASK 1 =====
The sentence starts with a digit.
The word 'served' is found at: (19, 25)
12345 contains only digits: True
123a5 contains only digits: False

===== TASK 2 =====
Capital words: ['ISRO', 'DRDO']

Words longer than 6 characters:
working starts at index 19
together starts at index 27
powerful starts at index 49
programming starts at index 58
language starts at index 70
Students starts at index 80
learning starts at index 93
computer starts at index 102
science starts at index 111

Dollar amounts: ['$3.50', '$1.20', '$4.75']
Number of prices: 3

===== TASK 3 =====
Email hidden:

Contact [EMAIL HIDDEN] or [EMAIL HIDDEN]
for more information.

Original name: Doe, John
New name: John Doe
Original: I have 3 apples and 5 oranges.
Doubled: I have 6 apples and 10 oranges.
Original: Wait!!! What??? Really!!!
After removing repeated punctuation: Wait! What? Really!
Number of replacements: 3

===== TASK 4 =====
_count2 is a valid variable name.
2fast is NOT a valid variable name.
total_sum is a valid variable name.

Pets found: ['cat', 'dog', 'bird', 'cat']
#FFAA00 is a valid hex color.
#000 is a valid hex color.
#12G is NOT a valid hex color.
#12345 is NOT a valid hex color.

Date: 2024-06-01
Time: 08:15:32
Level: ERROR
Message: Disk full

===== TASK 5 =====

Valid email tests:
john@gmail.com -> True
student123@yahoo.com -> True
abc.def@college.edu -> True
hello@python.org -> True

Invalid email tests:
a@b.c -> False
no-at-sign.com -> False
hello@gmail -> False
@gmail.com -> False

Phone numbers:
555-123-4567
555-123-4567
555-123-4567

Dates found:
('15', '08', '2005')
('20', '09', '2026')
('01', '01', '2027')

Dates after reformatting:

My birthday is 2005-08-15.
The exam is on 2026-09-20.
Another date is 2027-01-01.


Cleaned text:
Hello Python Welcome to Python!

Password tests:
Python@123 -> Strong password
hello -> Failed rules:
  - Password must contain at least 8 characters.
  - Password must contain an uppercase letter.
  - Password must contain a digit.
  - Password must contain a symbol from !@#$%^&*.
Python123 -> Failed rules:
  - Password must contain a symbol from !@#$%^&*.
PASSWORD@123 -> Failed rules:
  - Password must contain a lowercase letter.

===== TASK 6 =====

Parsed log entries:
{'timestamp': '2024-06-01 08:15:32', 'level': 'ERROR', 'user': 'jsmith', 'msg': 'Disk quota exceeded'}
{'timestamp': '2024-06-01 08:16:05', 'level': 'INFO', 'user': 'agarcia', 'msg': 'Login successful'}
{'timestamp': '2024-06-01 08:17:44', 'level': 'WARN', 'user': 'jsmith', 'msg': 'High memory usage'}

Summary:
ERROR: 1
WARN : 1
INFO : 1

Redacted log:

[2024-06-01 08:15:32] ERROR user=<hidden> msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO user=<hidden> msg="Login successful"
[2024-06-01 08:17:44] WARN user=<hidden> msg="High memory usage"

ERROR entries for each user:
jsmith -> Disk quota exceeded



        

    elif entry["level"] == "WARN":
        warn_count += 1

    elif entry["level"] == "INFO":
        info_count += 1


print("\nSummary:")
print("ERROR:", error_count)
print("WARN :", warn_count)
print("INFO :", info_count)


# ------------------------------------------------------------
# Hide usernames
# ------------------------------------------------------------

redacted_log = re.sub(
    r"user=\w+",
    "user=<hidden>",
    log
)

print("\nRedacted log:")
print(redacted_log)


# ------------------------------------------------------------
# BONUS - Sort entries by username
# ------------------------------------------------------------

entries.sort(key=lambda x: x["user"])

print("ERROR entries for each user:")

for entry in entries:

    if entry["level"] == "ERROR":
        print(entry["user"], "->", entry["msg"])
'''        
