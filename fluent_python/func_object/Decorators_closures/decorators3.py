from decorators2 import modified_clock,clock

from functools import lru_cache

# ............................................implementing lru_cache.................................................#

"""
1.The functools.cache decorator is actually a simple wrapper around the older fuctools.lru_cache decorator.

2.the main advantage of functools.lru_cache is that its memory usage is bounded by the maxsize parameter. 

3.The acronym LRU stands for Least Recently Used, meaning that older entries that
have not been read for a while are discarded to make room for new ones

"""

@lru_cache
@clock
def lru_implemented_fibo(n):
    if n < 2:
        return n
    else:
        return lru_implemented_fibo(n-1) + lru_implemented_fibo(n-2)
    
# ............................................ implementing functools.singledispatch .................................................#

# Single dispatch generic functions

"""
The functools.singledispatch decorator allows different modules to contribute to
the overall solution, and lets you easily provide specialized functions even for types
that belong to third-party packages that you can’t edit. If you decorate a plain func‐
tion with @singledispatch, it becomes the entry point for a generic function: 
'a group of functions to perform the same operation in different ways, depending on the type
of the first argument.' This is what is meant by the term single dispatch. If more argu‐
ments were used to select the specific functions, we’d have multiple dispatch.

# type hinting is neccessary for singledispatch to work because it create function overload based on type of first argument
"""

import html

def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

# Example 9-20 : Using singledispatch to build a generic display function for different types

from functools import singledispatch
from collections import abc
import numbers
import fractions
import decimal

@singledispatch
def singledispatch_htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@singledispatch_htmlize.register
def _(text:str):
    content = html.escape(text).replace('\n','<br>\n')
    return '<p>{0}</p>'.format(content)

@singledispatch_htmlize.register
def _(n:numbers.Integral) -> str:
    return f'<pre>{n} (0x{n:x})</pre>'

@singledispatch_htmlize.register
def _(seq:abc.Sequence):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>'+inner+'</li>\n</ul>'

@singledispatch_htmlize.register 
def _(n: bool) -> str:
 return f'<pre>{n}</pre>'

# if dont want to use type hinting then use register function attribute like @<<base>>.register(type)

@singledispatch_htmlize.register(fractions.Fraction) 
def _(x) -> str:
 frac = fractions.Fraction(x)
 return f'<pre>{frac.numerator}/{frac.denominator}</pre>'


@singledispatch_htmlize.register(decimal.Decimal) 
@singledispatch_htmlize.register(float)
def _(x) -> str:
 frac = fractions.Fraction(x).limit_denominator()
 return f'<pre>{x} ({frac.numerator}/{frac.denominator})</pre>'


# Python Protocols # .....................................

# "In python Protocols refer to the concept introduced in python3.8 as a way to define a structural typing or duck typing within the language
# A protocol is a set of methods or attributes that an object must have in order to be considered compatible with that protocol.
# Protocols enable you to define interfaces without explicitly creating a class or inheriting from a specific base class.
# protocols are defined using typing.protocol class or the typing.Protocol decorator


# Defining Protocol:

from typing import Protocol

class Printable(Protocol):
   def print(self) -> None:
      pass
   
# in above class we define a protocol name printable that requires an object to have print method.The Protocol class allow you to define a abstract method

# implementing a protocol
#  To implement a protocol , we dont need to explicitly declare it,instead you can ensure that you must implement the method in class

class Book:
    
    def __init__(self,title:str) -> None:
      self.title = title
    
    # implementing protocol
    def print(self) -> None:
      print(f"Book Title: {self.title}")
      
# Any instance of Book class can be treated as printable object

# NOTE === Protocols are primarly used for type hinting and static type checking.
# We can use a protocol as type annotation to indicate that an argument or variable must conform to specific protocol

def print_object(obj:Printable) -> None:
   obj.print()


class CarRed:
    color = "RED"
    def __init__(self,name:str,id:int) -> None:
      self.name = name
      self.id = id
    
    def printColor(self):
       print(self.color)

# Multiple Protocols

# We can defines a protocol that combines multiple other protocols

def Serializable(Protocol):
    def serialize(self) -> str:
      pass

class PrintableAndSerializable(Printable,Serializable): # it impelements the methods and attributes of protocols Serializable and Printable
   pass
      

if __name__ == "__main__":
    # print("Fibonacci using lru_cache")
    # print(lru_implemented_fibo(56))
    # print(singledispatch_htmlize({1,2,3}))
    # print(singledispatch_htmlize(abs))
    # print(singledispatch_htmlize('Heimlich & Co.\n- a game'))
    print_object(Book("Pranjal The Warrior")) # passing valid object
    #print_object(CarRed("Mercedez Benz",1)) # passing an invalid object who doesn't have print() implemented



