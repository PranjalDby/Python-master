# ---------------------- defining getter and setters for class ----------------------------------

from time import sleep
import functools
from typing import Any, Callable


class Circle:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self,value):
        self.__x = value;

    def get_y(self):
        return self.__y
    
    def set_y(self,value):
        self.__y = value



circle = Circle(33.3,42.1)

print(circle.get_y())

# modifying value of coordinate y
circle.set_y(32.12)
print(circle.get_y())


# Above practice is bad !. let do in pythonic way


# Using property()

class CicleRedefined:

    def __init__(self,radius = 0.0) -> None:
        self.__radius = radius

    # function object that would passed to the property

    def __get_radius(self):
        """Get the radius"""
        return self.__radius
    
    def __set_radius(self,val):
        """set the radius"""
        self.__radius = val

    
    # using lambda function inside the fget
    radius = property(fget=lambda self:self.__radius,fset=__set_radius,doc="radius property")


class CirclePropertyDeco:
    def __init__(self,radi):
        self.__radius = radi

    @property
    def radius(self):
        """radius property"""
        return self.__radius


class our_property:
    """Emulation of property class"""
    
    def __init__(self,fget=None,fset=None,fdel=None,doc=None) :
        
        """Attributes of 'our_decorator'
        fget
            function to be used for getting 
            an attribute value
        fset
            function to be used for setting 
            an attribute value
        fdel
            function to be used for deleting 
            an attribute
        doc
            the docstring
        """
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.doc = doc
        
        if self.fget is not None and doc is None :
            self.doc = fget.__doc__
            
    def __get__(self, instance, owner):
        """Get the attribute value"""
        print("__get__ is called")
        if instance is None:
            print("Instance is None")
            return self
        if self.fget is None:
            raise AttributeError("Can't get attribute")
        
        return self.fget(instance)
    
    def __set__(self, instance, value):
        """Set the attribute value"""
        if self.fset is None:
            raise AttributeError("Can't set attribute")
        self.fset(instance, value)
    
    def __delete__(self, instance):
        """Delete the attribute"""
        if self.fdel is None:
            raise AttributeError("Can't delete attribute")
        self.fdel(instance)

    def getter(self,fget):
        print("What is type self in getter in our custom property = ",type(self) )

        return type(self)(fget,self.fset,self.fdel,self.doc)
    
    def setter(self,fset):
        print("What is type self in setter in our custom property = ",type(self))
        return type(self)(self.fget,fset,self.fdel,self.doc)
    
    def deleter(self,fdel):
        return type(self)(self.fget,self.fset,fdel,self.doc)
    
    


class Rectangle:
    def __init__(self, l, b):
        self._length = l
        self._breadth = b


    @our_property
    def length(self):
        """length property"""
        return "Dummy"
    
    @length.getter
    def length(self):
        print("Haa.... 😊😊👌👌 Actual Getter.....")
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @our_property
    def breadth(self):
        """breadth property"""
        return self._breadth

    @breadth.setter
    def breadth(self, value):
        self._breadth = value

    # def __set_length(self,val):
    #     self.__length = val
    # length = our_property(lambda self: self.__length,__set_length)




# circle  = CicleRedefined(23.2)
# print("value of radius = ",circle.radius)
# circle.radius = 341.23
# print("value of setting the new value = ",circle.radius)
# # inspecting the property object
# print(circle)

# custom property

recx = Rectangle(23.2,33.3)


print("RUUFVSDFBIKOL;KKBNIKL -------------------------------------")
recx.length = 3423.22
print("lenght = ",recx.length,recx._breadth)

print("Breadth = ",recx.breadth)

# print(type(recx))



# providing Read-Only Attributes : ----- with custom exception with more elaborate and specific message


class CustomException(Exception):
    pass


class Point:
    def __init__(self,x,y):
        self._x = x
        self._y = y
        
    @property
    def x(self):
        """getter method for property x"""
        return self._x
    
    @property
    def y(self):
        """getter method for property y"""
        
        return self._y
    
    @x.setter
    def x(self,val):
        """setter Method for property x"""
        raise CustomException("x coordinate is a read-only attr.")
    
    
    @y.setter
    def y(self):
        """getter method for property y"""
        raise CustomException("y coordinate is a read-only attr.")
    


# --------------------------- creating a Read-Write attribute ------------------------------------------------------------------------

class Circle:
    def __init__(self,radius):
        self.__radius = radius
        
    @property
    def radius(self):
        """radius property"""
        return self.__radius
    
    @radius.setter
    def radius(self,val):
        self.__radius = val
        
        
    @property
    def diameter(self):
        """diameter property"""
        return self.__radius * 2
    
    @diameter.setter
    def diameter(self,v):
        self.__radius = v / 2 

point = Point(53.2,34.2)
print(point.x)
# point.x = 30
print(point.y)

# read-write property

circle = Circle(32.1)
print(circle.radius) # getter

circle.radius = 33
print(circle.radius) # setter


# ----------------------------- providing write-only attributes --------------------------------------------------------------------


import hashlib
import os

class User:
    
    def __init__(self,name,password):
        self.__name = name
        self.__password = password
        
    @property
    def password(self):
        """getter method doesn't work here. 🌋"""
        raise AttributeError("Password is write-only")
    
    @password.setter
    def password(self,plainText):
        salt = os.urandom(32)
        print(salt)
        """setter method"""
        self._hashed_password = hashlib.pbkdf2_hmac("sha256",plainText.encode('utf-8'),salt,100_000)
        
        

pranjal_ = User("Pranjal","#@24Sch92")
# print(user.password), throws error, becuase password is write-only

# print(pranjal_._hashed_password)
        
        
# ------------------------------------------ Python's property() Example ------------------------------------------------------


# Example 1 : validating input values


class PointWithValidation:
    
    def __init__(self,x,y):
        self.x = x # assigning the x and y property directly in constructor call ensures that validation also occurs during object initialization
        self.y = y # this attributes are now part of the property class 
        
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self,val):
        try:
            self._x = float(val)
            print("validated")
        except ValueError:
            raise ValueError('"x" must be a number') from None # it removes the previous exception from traceback
        
        
          
    @property  
    def y(self):
        return self._y
    
    @y.setter
    def y(self,val):
        try:
            self._y = float(val)
            print("validated")
        except ValueError:
            raise ValueError('"y" must be a number') from None  # it removes the previous exception from traceback
    
    
    
validation_p = PointWithValidation(20.2,33.2)
print(type(validation_p.x)(40))
print(validation_p.x)
# validation_p.x = "one"


# modifying the class to avoid repetition

class CoordinateDescriptor:
    def __set_name__(self,owner,name):
        self._name = name
        
    def __get__(self,instance,owner):
        print("Descriptor getter called.")
        return instance.__dict__[self._name]
    
    def __set__(self,instance,value):
        try:
            
            instance.__dict__[self._name] = float(value)
            print("Validate 🤫")
        except ValueError:
            raise ValueError(f'"{self._name}" must be a number') from None
        
        
class PointMdf:
    x = CoordinateDescriptor()
    y = CoordinateDescriptor()
    
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        
        
pm  = PointMdf(23.0,12.0)

print(pm.x)
pm.x = 11
print(pm.x)

# providing computed attributes

class Rectangle:
    def __init__(self,h,w) -> None:
        self.width = w
        self.h = h
        
        
    # computed attribute
    @property
    def area(self):
        return self.width * self.h
    
    
print("Computed attributes")
rr = Rectangle(33,12)
print(rr.area)


# Another common use case of computed attributes : to provide auto-formatted value for a given attribute:
import decimal
class Product:
    def __init__(self,name,price) -> None:
        self.__name = name
        self.__price = decimal.Decimal(price)
        
    @property
    def price(self):
        return f"${self.__price:.2f}"
    

pr = Product("Car",85000.3421)
print(pr.__dir__())


# ----------------------------------------------------- Caching Computed attributes ----------------------------------------------------------------

class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.__diameter = None # our cached property

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self,va):
        self.__radius = va
        self.__diameter = None

    @property
    def diameter(self):
        if self.__diameter is None:
            sleep(0.5) # Simulate a costly computation
            self.__diameter = self.radius * 2
        
        return self.__diameter
    

    """Warning!. even if this implementation of Circle caches computed attribute diameter,it has the drawback that
    if you ever change the value of .radius, then diameter won't return a correct value.
    to solve this we have two ways:
    1. we have to change the diameter every time user changes it radius only.

    2. another option to create a cached properties is to use functools.cached_property()
    """

rr = Circle(23.2)
print(rr.diameter)
rr.radius = 45.2
print(rr.diameter)

class CircleWithCaching:
    def __init__(self,radius) -> None:
        self.radius = radius

    
    @functools.cached_property
    def diameter(self):
        sleep(0.5)
        return self.radius * 2


circle_modified = CircleWithCaching(3.2)

print(circle_modified.radius)

print(circle_modified.diameter)

circle_modified.radius = 4.5
print(circle_modified.diameter)

# ----------------------------------- Logging Attribute Access And Mutation --------------------------------------------------
import logging

logging.basicConfig(
    format="%(asctime)s:%(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S"
)

class CircleLogged:
    def __init__(self,radius):
        self.__msg = '"radius" was %s.Current Value: %s'
        self.radius = radius

    @property
    def radius(self):
        """The Radius property."""
        logging.info(self.__msg % ("accessed",self.__radius))

        return self.__radius
    

    @radius.setter
    def radius(self,value):
        try:
            self.__radius = float(value)
            logging.info(self.__msg % ("mutated or updated",str(self.__radius)))

        except ValueError:
            logging.info("validation error while mutating radius")



circle_logged = CircleLogged(34.2)

# print(circle_logged.__dict__)


# ---------------------------------------- Managing attribute deletions --------------------------------------------------------
# 

class TreeNode:

    def __init__(self,data):
        self.__data = data
        self.__childrens = []

    @property
    def children(self):
        return self.__childrens
    
    @children.setter
    def children(self,val):
        
        if isinstance(val,list):
            self.__childrens = val
        
        else:
            del self.children
            self.__childrens.append(val)

    
    @children.deleter
    def children(self):
        self.__childrens.clear()


    
    def __str__(self) -> str:

        return f"{self.__class__.__name__}('{self.__data}')"
    
    def __repr__(self)->str:
        return f"{self.__class__.__name__}('{self.__data}')"

# Binary Tree
tree = TreeNode(34)
child1 = TreeNode(46)
child2 = TreeNode(31)

tree.children = [child1,child2]

# del tree.children
# print(tree)


#  ---------------------------------------- backward Compatible class API's -----------------------------------------------------


CENTS_PER_UNITS = 100
class Currency:
    
    def __init__(self,units,cents):
        self._total_cents = units * CENTS_PER_UNITS + cents
    
    @property
    def units(self):
        return self._total_cents // CENTS_PER_UNITS
    
    @units.setter
    def units(self,val):
        self._total_cents = self.cents + val * CENTS_PER_UNITS

    @property
    def cents(self):
        return self._total_cents % CENTS_PER_UNITS
    
    @cents.setter
    def cents(self,val):
        self._total_cents = self.units * CENTS_PER_UNITS + val



# Overriding Subclasses

class Person:
    def __init__(self,name):
        self.__name = name

    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value


    # Person imple;



class Employee(Person):
    @property
    def name(self):
        return super().name.upper()
    


emp = Employee("Pranjal")
print(emp.__dict__)
print(emp.name)

# setting an attribute
# emp.name = "JohnDoe" #; throws error: AttributeError: property 'name' of 'Employee' object has no setter

