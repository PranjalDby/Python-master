"""
Type hints—a.k.a. type annotations—are ways to declare the expected type of func‐
tion arguments, return values, variables, and attributes.

NOTE: Type hints are not mandatory, and they are not enforced by the Python com‐
piler. Python will ignore them at runtime. They are just metadata attached to vari‐
ables and expressions, and they are accessible at runtime using the typing module’s
inspection tools.
"""

from typing import NamedTuple

class DemoPlainClass:
    a:int
    b:float = 1.1
    c = 'spam'

obj = DemoPlainClass()
print(obj.b)


# class created by extending typing.NamedTuple

class DemoNamedTuple(NamedTuple):
    a:int # instance attribute //in hidden it calls __init__ method
    b:float = 1.1 # instance attribute with default value
    c = 'spam'  

print(DemoNamedTuple.__annotations__) #only a and b are present in the annotations

print(DemoNamedTuple.a) # value of  attr a 

print(DemoNamedTuple.b) # value of attr b

print(DemoNamedTuple.c) # value of attr c


# Above a and b are acts as descriptors and its is immutable

demoNT = DemoNamedTuple(8,4.5)

print(demoNT.a) # value of  attr a
print(demoNT.b) # value of attr b


# Inspecting a class decorated with @dataclass

from dataclasses import dataclass, field

@dataclass
class DemoDataClass:
    a:int = 2.1
    b:float = 1.1
    c = 'spam'


print(DemoDataClass.__annotations__) #only a and b are present in the annotations

print(DemoDataClass.a)

@dataclass
class ClubMember:
    name:str
    guest:list = field(default_factory=list)
    athlete:bool = field(default=False,repr=False)

# Post init method
# Common use cases for __post_init__ are validation and computing field values
# based on other fields. We’ll study a simple example that uses __post_init__ for both
# of these reasons

@dataclass
class HackerClubMember(ClubMember):
    all_handles = set()
    handle:str = ''

    def __post_init__(self):
        if self.handle == '':
            self.handle = self.name.split()[0]
            print(self.handle)

        if self.handle in self.__class__.all_handles:
            raise ValueError(f'Handle {self.handle} already exists')
        
        self.__class__.all_handles.add(self.handle)

    

anna = HackerClubMember('Anna Hacker')
anna_marie = HackerClubMember('Anna Marie Hacker',handle='MarieAnna11')
print(anna_marie)