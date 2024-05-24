# the operator module:
from decimal import Decimal
from functools import reduce

def factorial(n):
    return reduce(lambda a,b: a*b,range(1,n+1))# reduce is a higher order function that takes a function and a sequence and returns a single value by applying the function to all items in the sequence

print(factorial(5))

# operator module functions:
# rewritting the functions using operator module

from operator import *
def factorial_mm(n):
    return reduce(mul,range(1,n+1))

print('factorial using operator module: ',factorial_mm(5))

"""
Another group of one-trick lambdas that operator replaces are functions to pick
items from sequences or read attributes from objects: itemgetter and attrgetter
are factories that build custom functions to do that.
"""
metro = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)),
    ('Delhi NCR','IN',21.935,(28.613889,77.208889)),
    ('Mexico City','MX',20.142,(19.433333,-99.133333)),
    ('New York-Newark','US',20.104,(40.808611,-74.020386)),
    ('Sao Paulo','BR',19.649,(-23.547778,-46.635833)),
]

def sort_by_lat(mm):
    for city in sorted(mm,key=itemgetter(3)):
        # this creates a functions that, given a collections, returns the item at index 1
        print(city)


# sort_by_lat(metro)

# Because itemgetter uses the [] operator, it supports not only sequences but also mappings and any class that implements __getitem__.

# the sibling of itemgetter is attrgetter, which creates functions to extract object attributes by name. If several attributes are named, the function created by attrgetter() will return a tuple with all the values, and nested attribute lookup is also supported.

# example 7-14:
from collections import namedtuple

latlon = namedtuple('latlon','lat lon') # named fields

Metropolis = namedtuple('Metropolis','name cc pop coord')
print("Field names in Metropolis: ",Metropolis._fields)
metro_areas = [Metropolis(name,cc,pop,latlon(lat,lon)) for name,cc,pop,(lat,lon) in metro]

nam_lat = attrgetter('name','coord.lat')
for city in sorted(metro_areas,key=attrgetter('coord.lat')):
    print(f'city = {city}')
    print(nam_lat(city))

# Freezing argument with functools.partial

"""
the functools module provides several higher-order functions.
Another is partial:
given a callable, it produces a new callable with some of the arguments of the original
callable bound to predetermined values. This is useful to adapt a function that takes
one or more arguments to an API that requires a callback with fewer arguments.
"""
from functools import partial
trple = partial(mul,3)
print(trple(7))


# Example 7-16: Building a convenient Unicode normalizing function with partial
import unicodedata
nfc = partial(unicodedata.normalize,'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
print(nfc(s1))
# paritial() returns a functools.partial object has attributes providing access to the original function and the fixed arguments.

# inpt  = str(input("Enter a string: "))
# is_authenticated = (
#     inpt == 'pranjal112' 
# )
# if is_authenticated:
#     print("Welcome Pranjal")

