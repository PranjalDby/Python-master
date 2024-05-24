import functools
import itertools
import operator
from array import array
import reprlib,math
from typing import Any
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

    # implementing __hash__ method
        
    #Example 12-13: The VectorMultiDimensional using zip in for loop for more effecient comparison
    def __eq__(self,other)->bool:
        if len(self) != len(other):
            return False
        
        for a,b in zip(self,other):
            if a != b:
                return False
            
        return True
    
    # Updating genexp with Map()
    def __hash__(self) -> int:
        print("!!!Ignore: Just Flag.. __hash__ invoked")
        hashes = map(hash,self._components)
        return functools.reduce(operator.xor,hashes,0)

    def __len__(self)->int:
        return len(self._components)
    
    # Formatting
    def angle(self,n):
        r = math.hypot(*self[n:])
        a = math.atan2(r,self[n-1]) # generally it returns the arc tangent measurment
        if (n == len(self)-1) and (self[-1] < 0):
            return math.pi * 2 - a

        else:
            return a
        
    def angles(self):
        return (self.angle(n) for n in range(1,len(self)))
    
    def __format__(self,fmt_spec: str='') -> str:
        if fmt_spec.endswith('h'):
            # hypherspherical coordinates
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)],self.angles())
            outer_fmt = '<{}>'
        else:
            #if they are not hypherspherical coordinates then it will be euclidean coordinates
            coords = self
            outer_fmt = '({})'

        components = (format(c,fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))
    @classmethod
    def frombytes(cls,octets):
        typcode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typcode)
        cls(memv)


v = VectorMultiDimensional(range(10))
# Hashing and Faster ==

# Reducing Functions (functools.reduce() implementation)

#from functools import reduce

# Calculating Factorial of number using functool.reduce method
# number = int(input('Enter the Number: '))
# print(f'factorial of number using functools.reduce.... {reduce(lambda x,y:x * y,range(1,number + 1),0)}')

"""
# back to our hashing Problem;.........

#  There are the three ways of calculating the accumulated (xor) of integer from 0 to 5

# n = 0
# for i in range(1,6):
#     n^=i

# # print('n = {}'.format(n))

# # 2nd way is using functools.reduce()

# n = reduce(lambda a,b:a ^ b,range(1,6))
# print(n)

# # 3rd way os

# # back to our hashing Problem;.........

# #  There are the three ways of calculating the accumulated (xor) of integer from 0 to 5

# n = 0
# for i in range(1,6):
#     n^=i

# # print('n = {}'.format(n))

# # 2nd way is using functools.reduce()

# n = reduce(lambda a,b:a ^ b,range(1,6))
# print(n)

# # 3rd way by using operator.xor()

# n3 = reduce(operator.xor,range(1,6))
# print(n3)

# Implementing __hash__ method to our vector class

# practical on __eq__

v2 = VectorMultiDimensional(range(10))

print(hash(v2))
"""


# ---------------------------------------------- The Awesome zip ----------------------------------------------------

zp = zip(range(3),'ABC') # zip() will returns a generator that produces tuples on demand,Which we can then unpack into variables,one for each item in the parallel inputs
ls = [1,2,3,5]
print(list(zp))

print(list(zip(range(3),'ABC',[0.0,1.1,2.2,3.3]))) # zip stops without warning when one of the iterable exhausted


# itertools.zip_longest() functions behaves differently: it uses an optional 'fillvalue(None by default)' to complete missing values so it can generate tuples until the last iterable exhausted
from itertools import zip_longest
zp_lng = list(zip_longest(range(3),"ABC",[1,2,4,8],fillvalue = -1)) # type: ignore
print(zp_lng)

#zip function can also be used to transpose a matrix as nested iterables. for example

a = [(1,2,3),(4,5,6)]

print(list(zip(*a)))

b = [
    (1,2),
    (3,9),
    (5,6)
]
print(list(zip(*b)))

# enumerate

# for index,item in enumerate(b):
#     print(f'Element at {index} is {item}')


# VetcorTake #5: Formatting

v1 = VectorMultiDimensional([34,22])

print(format(v1,'eh'))