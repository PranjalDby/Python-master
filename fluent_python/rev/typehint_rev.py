from typing import Iterator, Optional, Sequence, Union
import re
import sys
import unicodedata
def showCount(count:int,singular:str,plural:Optional[str]=None) -> str:
    if count == 1:
        return f'1{singular}'
    
    count_str = str(count) if count else 'No'
    if not plural:
        plural = singular+'s'
        
    
    return f'{count_str} {plural}'
    
    

"example in contrasts of duck typing and nominal typing...."
class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print('Quack!!!! ')

def alert(birdie):
    birdie.quack()

def alert_duck(birdie:Duck):
    birdie.quack()

# @problamatic
# def alert_bird(birdie:Bird)->None:
#     birdie.quack()

"""
What information we can draw from above:
1.Duck is a subclass of Bird.
2.alert has no type hints, so the type checker ignores it.
3.alert_duck takes on argument of type Duck.
4.alert_bird takes one argument of type Bird.
"""


# type Usable in annotation......................
# Any :- Any is consistent-with every type
from typing import Any
class T1:
    pass
class T2(T1):
    pass
def f3(p:Any):
    print(p)

obj1 = object()
obj2 = T1()
obj3= T2()

# f3(obj1)#
# f3(obj2)#  all OK: Rule #2
# f3(obj3)#


# Optional and Union Typing
# type | type is short-hand trick for Using Optional  or Union
def showCount2(count:int,singular:str,plural:str|None = None)->str | None:
    if count == 1:
        return singular
    
    if plural != None:
        return f'{plural}'
    
    return f'{singular}s'

res = showCount2(len('Pranjal'),'Pranjal','Dubeys')
print(res)

def parseToken(token:str,id:Optional[int] = None) -> Union[str,float]:
    try:
        return float(token)
    
    except ValueError:
        return token
    
print(parseToken('10e9'))

# Tuples Types

# Tuple as Records:
""" if your are using tuple as records,use the tuple built-in and declare the types of the fields within []"""

# mapping cityName,population and country to Tuple
tup:tuple[str,float,str]

import geohash as gh #type:ignore

PRECESION = 9

def geohash(lat_lon:tuple[float,float]) -> str:
    return gh.encode(lat_lon[0],lat_lon[1],precision=PRECESION)

shanghai = 31.2304,121.4737

print(geohash(shanghai))

# Tuple as records with named fields

# Above geohash function representation using typing.NamedTuple
from typing import NamedTuple
class Coordinate(NamedTuple):
    lat:float
    lon:float


coordinate = Coordinate(31.22,121.23)
print(coordinate._fields)
print(geohash(coordinate))

def display(lat_lon:tuple[float,float])->str:
    lat,lon = lat_lon #unpack
    ns = 'N' if lat >=0 else 'S'
    we = 'E' if lon >= 0 else 'W'

    return f'{abs(lat):0.1f}deg {ns},{abs(lon):0.1f}deg {we}'

print(display(coordinate))

# Tuple as Immutable Sequences
"""To annotate tuples of unspecified length that are used as immutable lists, you must specify a single type,followed by a comma and ..."""

def columnize(items:Sequence[str],num_columns:int = 0) -> list[tuple[str,...]]:
    if num_columns == 0:
        num_columns = round(len(items) ** 0.5)

    num_rows,reminder = divmod(len(items),num_columns)
    print(num_rows)
    num_rows += bool(reminder)
    print(reminder)
    return [tuple(items[i::num_rows]) for i in range(num_rows)]


animals = 'drake fawn heron ibex koala lynx tahr xerus yak zapus'.split()

table = columnize(animals,4)
for row in table:
    print(''.join(f'{word:10}' for word in row))

RE_WORD = re.compile('\w+') # it matches one or more alphanumeric characters: Pattern Matching is greedy


for match in RE_WORD.finditer('ABC abc 123'):
    print(match.group().upper())


STOP_CODE = sys.maxunicode + 1
def tokenize(text:str)->Iterator[str]:
    """Return iterable of UpperCase Word"""
    for match in RE_WORD.finditer(text):
        yield match.group().upper()


def invertedUnicodeChar(start:int,end:int=STOP_CODE)->dict[str,set[str]]:
    char_store = [chr(char) for char in range(start,end+1)]
    index:dict[str,set[str]] = {}
    for char in char_store:
        if name:=unicodedata.name(char,''):
            for word in tokenize(name):
                print(word)
                index.setdefault(word,set()).add(char)
    
    return index

indx = invertedUnicodeChar(32,65)
print(indx['DIGIT'] & indx['EIGHT'])
from collections.abc import Iterable
# from collection.abc get Iterable:

fromTo = tuple[str,str] #fromTo is a type alias: I assigned tuple[str,str] to fromTo, to make the signature of zip_replace more readable

def zip_replace(text:str,changes:Iterable[fromTo]):
    for from_,to in changes:
        text = text.replace(from_,to)
    
    return text

l33t = [('a','4'),('e','3'),('i','1'),('o','0'),('u','2')]
text = 'mad skilled noob powned leet u'
print(zip_replace(text,l33t))




