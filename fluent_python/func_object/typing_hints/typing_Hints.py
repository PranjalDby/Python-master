# Gradual typing
import sys
from typing import Any
from pytest import mark
from typing import *
from collections import namedtuple
def show_count(count,singular,plural) -> str:
    if count == 1:
        print(f'1 {singular}')

    count_str  = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    
    return f'{count_str} {plural}'


def test_irregular():
    got = show_count(2,'apple',plural='apples')

# Using None as a default value for an argument is often a good choice when the

# Duck Typing
# The idea is that you can often avoid type checking by using isinstance to test
# for the presence of a certain attribute or method. This is often better than
# checking whether the argument is a duck (an instance of a particular class).\

# Example: that contrasts duck typing and normal typing, as well as static typing

# On Bird Module
# on Experiment we see on different modules bird.py, daffy.py, woody.py 
# we see that that duck typing is easier to get started and is more flexible, but allows unsupported operations to cause erors at runtime.
# Nominal typing is more verbose, but allows errors to be caught at compile time. but sometimes it rejects code that actually runs.

# Type Usable in annotations
# Types We can use with annotations

"""
😊typing.Any
• Simple types and classes
• typing.Optional and typing.Union
• Generic collections, including tuples and mappings
• Abstract base classes
• Generic iterables
• Parameterized generics and TypeVar
• typing.Protocols—the key to static duck typing
• typing.Callable
• typing.NoReturn—a good way to end this list
"""

# typing.Any - ignored but Important
# the keystone of any gradual typing system is the typing.Any type. also known as dynamic typing.
# it is compatible with every type.

def double(x):
    return x * 2

# it equivalent to:

def double_any(x:Any) -> Any:
    return x * 2

# Contrast 'any' with 'object'
# def double_with_obj(x:object) -> object:
#     return x * 2
# this functions also accepts arguments of every type, because every type is subtype-of object.

# Subtypes-of vs consistent-with
# traditional object-oriented nominal type system rely on the is subtype-of relation-ship.

# here given class T1 and subclass T2.then T2 is subtype-of T1, and T1 is supertype-of T2.
class T1:
    pass

class T2(T1):
    pass

def func(t:T2) -> None:
    pass

o1 = T1()
# func(o1)

# the call of f1(o1) is an applications of the Liskov Substitution Principle (LSP), which states that a function taking an argument of type T1 can also take an argument of type T2, if T2 is a subtype of T1.

# in a gradual typing system, there is another relation-ship:consistent-with, 
# which applies where-ever subtype-of applies:

# RULES:
# T2 is consistent-with T1 if T2 is a subtype of T1 or T1 is a subtype of T2.
# in other words, T1 and T2 are consistent-with each other if they are related by the is subtype-of relation-ship, or if they are unrelated.
# every type is consistent-with Any: you can pass objects of every type to a function that takes an argument of type Any.
# Any is consistent-with every type: you can pass an object of type Any  where an argument of another type is expected.

""" Simple types and classes"""
# the simplest types are the built-in types: int, float, bool, str, bytes, and None.
"""Optional and Union Types"""
# the typing module defines two special types that are useful in type annotations: Optional and Union.

""" There are three ways to annotate tuples :
1. Tuple as records
2. Tuples as record with named fields
3. Tuples as immutable sequences"""

# tuple as records
import geolib
from geolib import geohash as gh

def geohash(lat_lon: Tuple[float,float]) -> str:
    return gh.encode(*lat_lon,precision=9)

shan_lat_lon = (22.2758,114.1654)
print(geohash(shan_lat_lon))

# tuple as records with named fields
from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float

def geo_(lat_lon: Coordinate) -> str:
    return gh.encode(lat_lon.lat,lat_lon.lon,precision=9)

shanghai_lat_lon = Coordinate(22.2758,114.1654)
print(geo_(shanghai_lat_lon))

def display(lat_lon:tuple[float,float]) -> str:
    lat,lon = lat_lon
    ns = 'N' if lat >= 0 else 'S'
    we = 'E' if lon >= 0 else 'W'
    return f'{abs(lat):.1f}°{ns}, {abs(lon):.1f}°{we}'

print(display(shan_lat_lon))

# tuples as immutable sequences
"""to annotate a tuple of unspecified length that are used as immutable lists, you must specify a single type, followed by comma and ...."""

def columnize(sequence:Sequence[str],num_cols:int = 0) -> list[tuple[str,...]]:
    if num_cols == 0:
        num_cols = round(len(sequence) ** 0.5)
    
    num_rows,remainder = divmod(len(sequence),num_cols)
    num_rows += bool(remainder)
    return [tuple(sequence[i::num_rows]) for i in range(num_rows)]

animals =  'drake fawn heron ibex koala lynx tahr xerus yak zapus'.split()
cl_aa = columnize(animals)
for row in cl_aa:
    print("".join(f'{word:10}' for word in row))


# Generic Mappings

"""
generic mapping typer are annotated as  MappingType[keytype,valuetype].
"""
import unicodedata
import re
from collections.abc import Iterator
from random import sample, shuffle
from typing import TypeVar

RE_WORD = re.compile(r'\w+')
stop_code = sys.maxunicode + 1

def tokenize(text:str) -> Iterator[str]:
    for match in RE_WORD.finditer(text):
        yield match.group().upper()

def name_index(start=32,end=stop_code) -> dict[str,set[str]]:
    index:dict[str,set[str]] = {}
    for char in (chr(i) for i in range(start,end)):
        if name:= unicodedata.name(char,''):
            for word in tokenize(name):
                index.setdefault(word,set()).add(char)
            
    return index

index = name_index(32,65)


# Generic Iterables or Parameterized Generics and TypeVar

"""

A parameterized generic is a generic type, written as list[T], where T is a type vari‐
able that will be bound to a specific type with each usage. This allows a parameter
type to be reflected on the result type.

"""

T = TypeVar('T')

def sample(pop: Iterable[T],k:int) -> list[T]:
    if k < 1:
        raise ValueError(f'sample size must be positive,not {k}')
    
    resu = list(pop)
    shuffle(resu)
    return resu[:k]

"""
Important point:
• A restricted type variable will be set to one of the types named in the TypeVar
declaration.
• A bounded type variable will be set to the inferred type of the expression—as
long as the inferred type is consistent-with the boundary declared in the bound=
keyword argument of TypeVar
"""

# Protocol
"""
A protocol is a collection of methods and attributes that a class can implement to support a certain behavior.
Probelem solve with protocol
"""

def top(series:Iterable[T],length:int) -> list[T]:
    ordered = sorted(series,reverse=True)
    return ordered[:length]

l2 = [(len(s),s) for s in 'apple banana mango cherry'.split()]

# print(top(l2,2))


# Using Protocol

from typing import Protocol

class SupportLessThanType(Protocol):
    def __lt__(self,other:Any) -> bool:
        ...

LT = TypeVar('LT',bound=SupportLessThanType)

def new_top(series:Iterable[LT],length:int) -> list[LT]:
    ordered = sorted(series,reverse=True)
    return ordered[:length]


# Callable
"""
The Callable type is used to annotate functions that take arguments and return a value. It is a generic type, so you must specify the types of the arguments and the return value.

A callable type is written as Callable[[arg1type, arg2type], returntype]. The square brackets are required, even if there is only one argument.
The parameter list --[p1,p2] can have zero or more types

it is in collection.abc module
"""
from collections.abc import Callable
def update(
        probe:Callable[[],float],
        display:Callable[[float],None]
)-> None:
    temperature = probe()
    display(temperature)


def probe_ok() -> float:
    return 25.0

# function above is consitent-with Callable[[],float] because it takes no arguments and returns a float.

def display_wrong(temperature:int) -> None:
    print(f'Current temperature: {hex(temperature)}')

# update(probe_ok,display_wrong) Type Error

def display_ok(temperature:complex) -> None:
    print(f'Current temperature: {temperature}')

update(probe_ok,display_ok)

"""
formally we say that Callable[[],float] is  subtype-of Callable[[],float] as int is subtype of fl0at.
but...
formally Callable[[int],None] is not subtype-of Callable[[float],None] because int is not subtype of float.
in parametrized Callback type the relationship is reversed: Callable[[float],None] is subtype-of Callable[[int],None] because float is subtype of int. 
"""

# last special type NoReturn
"""This is special type used only annotate the return type of a function that never returns."""