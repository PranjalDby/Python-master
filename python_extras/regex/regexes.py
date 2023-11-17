import re
import sys
# Meta-characters..
"""
some meta characters are 
. ^ $ * + ? { } [ ] '\' | ( )

"""

# r = re.compile(r'pranj$')
# print(r)
# for i in sys.argv[1:]:
#     pattern = r.finditer(i)

# for m in pattern:
#     print(m)


def is_in(*args):
    matches = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
    match_name = re.compile(r'[^a]st\w')
    with open('python_extras/regex/contacts.txt','r') as file:
        content = file.read()
        pt = match_name.finditer(content)
        for i in pt:
            print(i)

if __name__ == '__main__':
    ii = sys.argv[1:]
    is_in(*ii)


# some re methods in python

inp = str(input('Enter a Email Address: '))

matchs = re.search(r'[\s][@]\w*[.]\w++',inp)

if matchs:
    print('nice you use domain = ',matchs.group())
