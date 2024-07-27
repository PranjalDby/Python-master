# class is a blueprint for real-world entity object. it defines the structure of an object
from tracemalloc import Traceback
from typing import Optional, Self


class Door:
    # attributes: instance attributes or class attributes
    def __init__(self,height,color,is_locked) -> None:
        # defining instance attributes
        self.height = height
        self.color = color
        self.is_locked = is_locked

    
    # behaviors or methods.
    def open(self):
        print("Door Opened!." if self.is_locked else "Door is Closed.")
        self.is_locked = False if self.is_locked else True 



# objects are unique in nature

door2 = Door(54,'red',True)
door2.open()

# ...................................... how class instance is created and initialized ................................................

class Point:
    # object creator __new__

    def __new__(cls,*args,**kwarg) -> Self:
        print("1.Create a new instance of Point.")
        print(f"{isinstance(super(),object)}")
        return super().__new__(cls)
    

    # constructor class

    def __init__(self,x,y):
        print("it initialize the new instance of the point.")
        self.x = x
        self.y = y


    def __str__(self) -> str:
        return f'{type(self).__name__}(x= {self.x} y= {self.y})'
    


"""
Subtle Note:
A subtle and important detail to note about .__new__() is that it can also return an instance of a class different from the class that implements the method itself(mean' it also returns an instance of different class). When that happens, Python doesn't call .__init__() in the current class, because there's no way to unambiguously know how to initialize an object of a different class.
"""

# Example

class A:
    #initializing the class A
    def __init__(self,a_val) -> None:
        print("Initialize the new instance of A.")
        self.a_value = a_val


class B:

    def __new__(cls,*args,**kwargs) -> Self:
        return A(22)
    
    #this doesn't call because instance of b is not created.
    def __init__(self,b_value) -> None:
        print("initializing the instance of B")
        self.b_val = b_value



b = B(12) # it refrence to instance of class A.

print(b.a_value)

p = Point(20,22.2)

# ------------------------------------------- Object initilization with .__init__() ----------------------------------------------------------------


class Rectangle:
    # def __init__(self,l:Optional[float | int],b:Optional[float | int]) -> None:
    #     # ------------------------------ type-validation -----------------------------------------------
    #     if not isinstance(l,(float,int)) or l < 0:
    #         raise ValueError('Positive value expected. got {}'.format(l))
        
    #     self.l = l
    #     if not isinstance(b,(float,int)) or b <0:
    #         raise ValueError('Positive value expected. got {}'.format(b))
        
    #     self.b  = b
    # type validation using python property()
    def __init__(self,l,b) -> None:
        self._l = l
        self._b = b

    def __checkType(self,val):
        if not isinstance(val,(int,float)) or val < 0:
            raise ValueError(f'+Ve value expected got {val}')
        
        return

    @property
    def length(self):
        print("length property.")
        self.__checkType(self._l)
        return self._l
    
    @length.setter
    def length(self,val):
        self.__checkType(val)
        self._l = val

    
    @property
    def breadth(self):
        print("breadth property.")
        self.__checkType(self._b)
        return self._b
    
    @breadth.setter
    def breadth(self,val):
        self.__checkType(val)
        self._b = val

    


# Building flexible object initializer:

class Cheque:
    BANK_NAME = "STATE BANK OF INDIA"
    ADDRESS = "BHELUPUR"
    PINCODE = "2233001"

    def __init__(self,amount,/,pay = 'self') -> None:
        self.__amount = amount
        self.pay = pay


    def _valid_amount(self)->bool:
        if self.__amount > 0 and self.__amount < 100000:
            return True
        
        else:
            raise ValueError("Transaction Failed.Please try after 24 hrs.")

    @property
    def amount(self):
        return self.__amount if self._valid_amount() else 0



pranjalChq = Cheque(1000,pay='self')
print(pranjalChq.amount)


class ABC:
    #creating new instance using __new__()
    def __new__(cls,*args,**kwargs) -> Self:
        instance = super().__new__(cls) #create an empyt object

        return instance