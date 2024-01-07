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
print(cp.__dir__())

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

print(weaklist_obj('Pranjal'))

