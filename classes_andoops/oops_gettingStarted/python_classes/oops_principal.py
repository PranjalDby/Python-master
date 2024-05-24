# objects
import dis
import io
import operator
import os

import pickle

class Dog:
    # properties
    def __init__(self,name,color,bread,age) -> None:
        self.dog_name = name
        self.dog_color = color
        self.bread = bread
        self.age = age

    #behaviour

    def bark(self):
        print(f'{self.dog_name} barks....')



dg = Dog("Bruno","pale brown","St.Breanard",15)


print(dg.bark())


#! --------------------- Polymorphism ---------------------------------------------------------------

#!---OperatorOverloading

#! + operator adds two numbers
print(1 + 2)
#! + operator concatenate two strings
print("Hello " + "World Of Ai")

#! ----- custom class that supports operator overloading

class OperatorOverloading:
    def __init__(self,obj):
        self.ob1 = obj

    # implementin __add__

    def __add__(self,ob1):
        return self.ob1 + ob1.ob1
    
    def __str__(self):
        return self.ob1
    
    # overloading more operator

    def __lt__(self,other):
        return self.ob1 < other.ob1
    

    def __le__(self,other):
        return self.ob1 <= other.ob1
    
    def __neg__(self):
        return OperatorOverloading(self.ob1-1)
    



if __name__ == "__main__":
    ob1 = OperatorOverloading(12)
    ob2 = OperatorOverloading(23)

    obj1 = OperatorOverloading(45)

    print(obj1.ob1-1)
    print(obj1.ob1)
    #! for str types

    st1 = OperatorOverloading("Pranjal")
    st2 = OperatorOverloading("Dubey")
    print(st1,st2)


    #! more operator overloading

    print(ob1 <= ob2)
    if os.path.exists('__pycache__/oops_principal.cpython-311.txt'):
        with open('__pycache__/oops_principal.cpython-311.txt','w+') as f:
            dis.dis(OperatorOverloading,file=f)



#! ----------------------------------------------- classes in pythons ------------------------------------------------------
# Creating Circle class

import math
from typing import IO, Any
class Circle:
    # constructor
    def __init__(self,radius) -> None:
        #instance attribute
        self.radius = radius

    # method

    def calc_area(self)-> Any:
        return round(math.pi * (self.radius ** 2))



cir = Circle(34)
print(cir.calc_area())


#  ------------------------------------------ Naming Conventions in Python ----------------------------------------------------------------------------


class NamingConvenctions:
    __sessionID = "233-0001-192.168.1.1@pranjal"
    def __init__(self,name) -> None:
        self.user_name = name



ob = NamingConvenctions("Pranjal")


# ------------------------------- public and non-public names in modules and packages ----------------------------------------------------

_count = 0

def increment():
    global _count
    _count += 1

def decrement():
    global _count
    _count -=1

def get_count():
    return _count


# incrementing the counter
increment()
increment()
increment()

print(get_count())

# this conveys the message to other developers that is non-public constant
_PI = 3.141592653589793


class Circle:
    def __init__(self,radius) -> None:
        self.radius = _validate(radius)

    def calculate_area(self):
        return round(_PI * self.radius ** 2)
    
    

# --------------------------------- helper functions -----------------------------------------------------------
#$ and it is not a public functions..
def _validate(value):
    if not isinstance(value, (int|float)) or value <= 0:
        raise ValueError("positive number expected..")
    
    return value

circle = Circle(34)
print(circle.calculate_area())


#! ---------------------------- Class with Non-Public Members ----------------------------------------------------

class Point:
    
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.lambds = lambda x : x ** 2


    def __getstate__(self):
        attr = self.__dict__.copy()
        del attr['lambds']
        return attr
    
    def __setstate__(self,state):
        for st,val in state.items():
            setattr(self,st,val)
        setattr(self,'lambds',lambda x: x ** 2)
    #! getter
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self,value):
        self._x = _validate(value)

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self,value):
        self._y = _validate(value)

    


pp = Point(23.2,34.2)

#! accessing the attributes
print(pp.x,pp.y)

#! changing the value of attributes
pp.x = 12.2;pp.y = 56.2
print(pp.x,pp.y)

#Pickling -pickle is a module in python that is used to serialize and deserialize the python object
# serialization is the process of converting the object into a byte stream or in the form of a string
# deserialization is the process of converting the byte stream or string into the object

f = io.BytesIO(); #temporary file

pickle_obj = pickle.Pickler(f,pickle.HIGHEST_PROTOCOL)
pickle_obj.dump(pp) # serializing the object

f.seek(0)

unpickle_obj = pickle.Unpickler(f);
print(unpickle_obj.load().lambds(20)) # deserializing the object
