from array import array
import math
import operator
import reprlib
# Notes of About Above Point
        
"""
#1 : the self._components instance "protected" attribute will hold an array with the VectorComponents

#2 : To Allow iteration, we return an iterator over self._components

#3 : User reprlib.repr() to get a limited-length representation of self._components

#4 : Remove the array('d', prefix, and the trailing ) before plugging the string into
a Vector constructor call

#5 : Build a bytes object directly from self._components.
"""


# Protocols & duck-typing

import collections
from typing import Any, NamedTuple, Protocol
Card = collections.namedtuple('Card',['ranks','suits'])


# This is sequence
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(ranks,suits) for suits in self.suits for ranks in self.ranks]

    
    def __len__(self)->int:
        return len(self._cards)
    
    def __getitem__(self,index):
        return self._cards[index]
    


# fdeck = FrenchDeck()

# print(fdeck._cards)
    
"""
The Above FrenchDeck class takes advantages of many python facilities, because it  implements the sequence protocol, even if that is not declared anywhere in the code.
FrenchDeck is a Sequence even if it subclasses object. We say that it is a sequence because it behaves like a sequence
"""


# Sliceable Sequences

# class VectorMultiDimensional:
#     typecode = 'd'
#     def __init__(self,components) -> None:
#         self._components = array(self.typecode,components) #1
#     def __iter__(self):
#         return iter(self._components) #2
    
#     def __repr__(self) -> str:
#         cmpnts = reprlib.repr(self._components)#3
#         cmpnts = cmpnts[cmpnts.find('['):-1]#4
#         return f'Vector({cmpnts})'
    
#     def __str__(self)->str:
#         return str(tuple(self))
    
#     def __bytes__(self):
#         return (bytes([ord(self.typecode)]) + bytes(self._components))#5
    
#     def __eq__(self,other):
#         return tuple(self) == tuple(other)
    
#     def __abs__(self):
#         return math.hypot(*self)
    
#     def __bool__(self):
#         return bool(abs(self))
    
#     # Making it - a Sliceable Sequences

#     def __getitem__(self,position):
#         return self._components[position]
    
#     def __len__(self)->int:
#         return len(self._components)
    
#     @classmethod
#     def frombytes(cls,octets):
#         typcode = chr(octets[0])
#         memv = memoryview(octets[1:]).cast(typcode)
#         cls(memv)

# How Slicing Works

class Myseq:
    def __getitem__(self,i):
        return i
    

# s = Myseq()
# print(s[1:5:2,7:9:1])


# # Inspecting the attributes of the slice clas
# print(dir(slice))
# print(help(slice.indices))

# # Example----------
# st = "Pranjal"
# print(st[1:4:2])


# Improved Vector.__getitem__ implementation

# class VectorMultiDimensional:
#     typecode = 'd'
#     def __init__(self,components) -> None:
#         self._components = array(self.typecode,components) #1
#     def __iter__(self):
#         return iter(self._components) #2
    
#     def __repr__(self) -> str:
#         cmpnts = reprlib.repr(self._components)#3
#         cmpnts = cmpnts[cmpnts.find('['):-1]#4
#         return f'Vector({cmpnts})'
    
#     def __str__(self)->str:
#         return str(tuple(self))
    
#     def __bytes__(self):
#         return (bytes([ord(self.typecode)]) + bytes(self._components))#5
    
#     def __eq__(self,other):
#         return tuple(self) == tuple(other)
    
#     def __abs__(self):
#         return math.hypot(*self)
    
#     def __bool__(self):
#         return bool(abs(self))
    
#     # Making it - a Sliceable Sequences

#     def __getitem__(self,key):
#         if isinstance(key,slice):
#             print('its a slice object')
#             cls = type(self)
#             return cls(self._components[key])

#         index = operator.index(key)
#         return self._components[index]
    

    
#     def __len__(self)->int:
#         return len(self._components)
    
#     @classmethod
#     def frombytes(cls,octets):
#         typcode = chr(octets[0])
#         memv = memoryview(octets[1:]).cast(typcode)
#         cls(memv)


# v1 = VectorMultiDimensional(range(10))
# print(type(v1[-1])) # an integer index retreives just one component value as a float.

# print(v1[1:6]) # This slice index creates a new VectorMultiDimensional.

# print(v1[-1:]) # A slice of len ==1  also creates VetcorMultiDimensional.

# print(v1[1,2]) # VectorMultiDimesional does not support multidimensional indexing . it throws typeError



# --------------------------------------------- Dynamic Attribute Access --         ----------------------------------------

 
class VectorMultiDimensional:
    # Positional pattern matching

    __match_args__ = ('x','y','z','t')

    typecode = 'd'
    def __init__(self,components) -> None:
        self._components = array(self.typecode,components)
    def __iter__(self):
        return iter(self._components) #2
    
    def __repr__(self) -> str:
        cmpnts = reprlib.repr(self._components)
        cmpnts = cmpnts[cmpnts.find('['):-1]
        return f'VectorMultiDimensional({cmpnts})'
    
    def __str__(self)->str:
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))#5
    
    def __eq__(self,other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(*self)
    
    def __bool__(self):
        return bool(abs(self))
    
    # implementing __getattr__ special method

    def __getattr__(self,name):
        cls = type(self)
        try:
            pos = cls.__match_args__.index(name)
        
        except ValueError:
            pos = -1

        if 0 <= pos <= len(self._components):
            return self._components[pos]
        
        msg = f'{cls.__name__!r} object has no attribute {name!r}' 
        raise AttributeError(msg)
    
    # Making it - a Sliceable Sequences

    def __getitem__(self,key):
        if isinstance(key,slice):
            print('its a slice object')
            cls = type(self)
            return cls(self._components[key])

        index = operator.index(key)
        return self._components[index]
    

    #Implementing __setattr__() to our class

    def __setattr__(self, __name: str, __value: Any) -> None:
        cls = type(self)
        if len(__name) == 1:
            if __name in cls.__match_args__:
                error = "readonly attribute {attr_name!r}"
            
            elif __name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            
            else:
                error = ''
            
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=__name)
                raise AttributeError(msg)
            
        
        super().__setattr__(__name,__value)


    def __len__(self)->int:
        return len(self._components)
    
    @classmethod
    def frombytes(cls,octets):
        typcode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typcode)
        cls(memv)


v = VectorMultiDimensional(range(1000))

# print(v.d) # Throws AttributeError

# Line 244 Implementing __setattr__()

v.d1 = 50 # Throws AttributeError
print(v.d1)