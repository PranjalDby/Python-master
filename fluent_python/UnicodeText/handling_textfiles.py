import locale
from unicodedata import name
import sys

"""
@doc
The Best practice of handling text I/O is the "Unicode sandwich" this means that bytes converted  to str as early as possible on input
. The Filling of sandwich is the bussiness logic of your propgram, where text handlings done xclusively on str objects


@Curiosity:::
# saas  palindroming string
# def check_is_palindrome(words:str):
#     if len(words) == 0 or len(words) == 1:
#         return True
    
#     if words[:1] == words[len(words)-1:]:
#         return check_is_palindrome(words[1:len(words)-1])
    
#     return False

# print(check_is_palindrome('saap'))

"""

with open('encode_text.txt','w+',encoding='utf-8') as file:
    file.write('café')

with open('encode_text.txt','r') as f:
    print(f.read())


# Beware of Encoding defaults

expressions = """
locale.getpreferredencoding()
type(my_file)
my_file.encoding
sys.stdout.isatty()
sys.stdout.encoding
sys.stdin.isatty()
sys.stdin.encoding
sys.stderr.isatty()
sys.stderr.encoding
sys.getdefaultencoding()
sys.getfilesystemencoding()
"""


# for exp in expressions.split():
#     value = eval(exp)
#     print(f"{exp:>30} -> {value!r}")

print(sys.version)
print()

print('sys.stdout.isatty():',sys.stdout.isatty())
print('sys.stdout.isatty():',sys.stdout.encoding)


test_chars = [
 '\N{HORIZONTAL ELLIPSIS}', # exists in cp1252, not in cp437
 '\N{INFINITY}', # exists in cp437, not in cp1252
 '\N{CIRCLED NUMBER FORTY TWO}', # not in cp437 or in cp1252
]

print(locale.getpreferredencoding())
with open('dummy1.txt','w+',encoding='cp437') as file:
    for char in ['\N{INFINITY}']:
        # print(f'Trying to output {name(char)}')
        # print(char)
        file.write(char)

