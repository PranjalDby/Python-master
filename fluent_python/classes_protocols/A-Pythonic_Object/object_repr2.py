import array
import math
from object_repr import Vector2DHashable
# Private and Protected Attributes in Python

# v1 = Vector2DHashable(3,5)
# print(v1.__dict__)
# print(v1._Vector2DHashable__x)


# Saving Memory with __slots__

class Pixel:
    __slots__ = ('x','y')

p = Pixel()
p.x = 10
p.y = 20
print(p.x,p.y)
# print(p.__dict__) # it raises an Attribute Error:no attribute __dict__

# Creating a subclass for Pixel

class OpenPixel(Pixel):
    ...

op = OpenPixel()
op.x = 40 # this is a instance attribute stored inside a hidden array of reference in the instance
op.color = 'Red'
op.name = 'Pranjal'
print(op.__dict__)

# subclass with its own __slot__ attribute
# Essentially , __slots__ of the superclasses are added to the __slots__ of the current class.Don't forget that single-item-tuple must have trailingc comma.
class ColorPixel(Pixel):
    __slots__ = ('color',)

cp = ColorPixel()
cp.color = 'Red'
# print(cp.__dir__())

# weakref revisited ...... 
import weakref

from typing import Any, Callable
class CFG:
    def __init__(self,string) -> None:
        self.s = string
   
    def __call__(self, *args: Any, **kwds: Any):
        print(*args)

def prints(str):
    print(str)

obj = CFG("Geekos Lotus")
# creating a normal list object
normal_list = obj
# print(f'this is a normal object: {normal_list}')

# creating a weak reference to the object
# the weakref.ref takes to argument an object or callable which is called when object is finallized
weakList = weakref.ref(obj,lambda : print('Object finalized'))
weaklist_obj = weakList() # object created using weak reference

# print(weaklist_obj('Pranjal'))

#  Simple Measures of __slot__ Savings.......................

class Vector2DSlotOptimized:
    __match_args__ = ('x','y') #postional pattern matching
    __slots__ = ('__x','__y')
    typecode = 'd'
    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)

    # Getter to the private properties
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    
    def __iter__(self):
        return (i for i in (self.x,self.y))
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name,*self)
    
    def __str__(self) -> str:
        return "Called __str__ "+str(tuple(self))
    

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array.array(self.typecode,self)))
    
    def __eq__(self, __value: object) -> bool:
        return tuple(self) == tuple(__value)
    
    def __abs__(self):
        return math.hypot(self.x,self.y)
    
    # making it hashable
    def __hash__(self) -> int:
        return hash((self.x,self.y))
    
    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        print(typecode)
        memv = memoryview(octets[1:]).cast(typecode) # to access the internal data of an object
        # changing the value
        return cls(*memv)
    

# Vector2d_opt = Vector2DSlotOptimized(23,44)
# print(Vector2d_opt.__dir__())

# Overriding Class Attributes Example:////
v1 = Vector2DSlotOptimized(1.2,3.4)

dumpd = bytes(v1)
print(dumpd)
print(
    f'it is a 17:bytes long and it is default...{len(dumpd)}'
)

v1.typecode = 'f' #'4byte single-precision value'
# it doesn't change the Vector2DSlotOptimized.typecode; only v1 instance uses typecode 'f'.

# to actually change the typecode of class attribute.we have to subclass it and then customize the class data attribute


