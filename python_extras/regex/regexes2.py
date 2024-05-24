import re
# Repetition

# Things get More interesting when you use + and * to specify repetition in the pattern

# + means one or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
# * means zero or more occurrences of the pattern to its left
# ? means zero or one occurrences of the pattern to its left

# So the pattern 'ab*' means: an a followed by zero or more b's
# And the pattern 'ab+' means: an a followed by one or more b's
# And the pattern 'ab?' means: an a followed by zero or one b's

matches = re.search(r'pi+','piiggg')
print(matches)

m2 = re.search(r'\d\s*\d\s*\d','xx1 2   3xx')   
print(m2)

m3 = re.search(r'\w+\b','pranjal11@outlook.com')
print(m3)

# Email Extraction
# garbage_email = str(input('Enter a garbage email: '))
# m4 = re.search(r'[\w.]+\@\w+[.]\w+',garbage_email)
# print(m4)

# Group Extraction
"""
The "group" feature of a regular expression allows you to pick out parts of the matching text.
() - parenthesis are used to group the sub-patterns
"""
# garbage_email = str(input('Enter a garbage email: '))

# m5 = re.search(r'([\w.\d]+)@([\w.]+)',garbage_email)
# if m5:
#     print(m5.group())
#     print('Username: ',m5.group(1)) # username
#     print('Domain: ',m5.group(2)) # domain

# findall() method
"""
findall() method returns a list of strings containing all matches
"""
# m6 = str("".join(input('Enter a Garbage Email: ')))
# print(m6)

# fndall = re.findall(r'[\w.]+@[\w.]+',m6)

# print(fndall)

# findall with files
# findall() and Groups

# with open('python_extras/regex/contacts.txt','r') as file:
#     content = file.read()
#     # fndall2 = re.findall(r'[\w.]+@[\w.]+',content) GETTING ALL EMAIL
#     fndall2 = re.findall(r'([\w.\d]+)@([\w.]+)',content)
#     for username,host in fndall2:
#         print(f' Username: {username} \n Host: {host} \n')

"""
NOTE: 
Regular expression patterns pack a lot of meaning into just a few characters , but they are so dense, you can spend a lot of time debugging your patterns. Set up your runtime so you can run a pattern and print what it matches easily, for example by running it on a small test text and printing the result of findall(). If the pattern matches nothing, try weakening the pattern, removing parts of it so you get too many matches. When it's matching nothing, you can't make any progress since there's nothing concrete to look at. Once it's matching too much, then you can work on tightening it up incrementally to hit just what you want.
"""
# Options
"""
Regular expression patterns have a way to include "flags" which change how the patterns work. Flags are available in Python for some other regex engines, but they're called "modifiers" there.
1.IGNORCASE - makes the pattern case insensitive so that it matches strings of different capitalizations
2.DOTALL - makes the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except a newline.
3.MULTILINE - makes the '^' and '$' special characters match the start and end of any line in the string, not just the start and end of the whole string.
"""

# greedy vs non-greedy

# with open('python_extras/regex/baby1990.html') as file:
#     content = file.read()

#     year = re.findall(r'( \d\d\d\d)',content)
#     rank = re.findall(r'<\w.?>(\d+)',content)
#     name = re.findall(r'\d.*<\w.*>(\w+)',content)
#     name = sorted(name)
#     print(len(rank))
#     print(len(name))
#     combined = [] 
#     for i in range(len(name)):
#         if i < len(rank):
#             name[i] = name[i] +" "+ rank[i]

#     print(name)
