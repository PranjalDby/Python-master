# unpacking mappings

import re
import sys


def get_email(record:dict):
    match record:
        case {'type':'employee','role':'ML -- Engineer','email':[*emails]}:
            print(emails)

        case {'type':'employee','role':'Software-Engineer','email':[*emails]}:
            print(emails)

record = {}
record['type'] = 'employee'
record['role']  = 'ML -- Engineer'
record['email'] = ['dpranjal.099@gmail.com','pranjaldubey@outlook.com']

get_email(record)

food = dict(category='ice-cream',flavour = 'vanilla',cost = 199)
match food:
    case {'category':'ice-cream',**others}:
        print(others)

# mapping = {}
# worde_re = re.compile('\w+')
# with open(sys.argv[1],encoding='utf-8') as file:
#     for line_no,line in enumerate(file,1):
#         for match in worde_re.finditer(line):
#             word = match.group()
#             column = match.start() + 1
#             location = (line_no,column)
#             mapping.setdefault(word,[]).append(location)

# print(mapping)

# searching for non string key..

class StrDictKey0(dict):
    def __missing__(self,key):
        if isinstance(key,str):
            raise KeyError(key)
        
        return self[str(key)]
    
    def __contains__(self, __key: object) -> bool:
        return __key in self.keys() or str(__key) in self.keys()
    

d = StrDictKey0([('2','Two'),('4','Four')])
s:str = 'Pranjal'
print(d.get('4'))
print('4' in d.keys())