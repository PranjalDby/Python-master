from unicodedata import name
import sys

START,END = ord(' '), sys.maxunicode + 1

def find(*query_words,start = START,end = END):
    query = {w.upper() for w in query_words}
    print(query_words)
    print(start)
    print(end)
    # print(name(chr(start)))
    for code in range(start,end):
        char = chr(code)
        u_name = name(char,None)
        if u_name and query.issubset(u_name.split()):
            print(f'U+{code:04x}\t{char}\t{u_name}')

def main(args):
    if args:
        find(*args)

if __name__ == "__main__":
    main(sys.argv[1:])